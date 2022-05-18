#include "sched.h"

#include <libk/kmalloc.h>
#include <libk/string.h>
#include <libk/list.h>
#include <libk/assert.h>

/*
 * Very simple scheduler, just to keep going on threads
 * Use pick_next to set globally accessible current proc
 */

struct proc* current_proc;

struct list proc_list;
struct list_node* last_element = NULL;

int scheduling_enabled = 0;

int pid_now = 0;

// FIXME: Request pages from virtual memory manager
int first_free_page = 17;
int first_free_prog_page = 17;

extern void __attribute__((noreturn)) idle_task();
struct proc idle_struct;

void scheduler_init() {
    list_init(&proc_list);
    scheduling_enabled = 0;
    pid_now = 0;

    // init idle task
    idle_struct.pid = 0;
    idle_struct.state = PROC_STATE_RUNNABLE;
    idle_struct.type = PROC_TYPE_INIT;
    strcpy(idle_struct.name, "idle");
    idle_struct.pc = (int)idle_task+1;
    for(int i=0; i<16; i++)
        idle_struct.prog_pages[i] = i;
}

/* Set current_proc to next process */
void sched_pick_next() {
    ASSERT(proc_list.first != NULL);

    struct list_node* first_element = last_element;
    for(;;) {
        // if reached end of list return to beginning
        if (last_element == NULL || last_element->next == NULL)
            last_element = proc_list.first;
        else
            last_element = last_element->next;

        // check if valid to run
        struct proc* lproc = (struct proc*)last_element->val;

        // this process is valid to run
        if(lproc->state == PROC_STATE_RUNNABLE)
            break;

        if(lproc->state == PROC_STATE_BLOCKED) {
            // check if blocked process is unblocked now
            if(lproc->sema_blocked && lproc->sema_blocked->count > 0) {
                lproc->state = PROC_STATE_RUNNABLE;
                lproc->sema_blocked = NULL;
                break;
            }
        }

        if(last_element == first_element) {
            // if no process is currently available, set kernel idle task to allow device irq
            current_proc = &idle_struct;
            return;
        }
    }

    current_proc = ((struct proc*) last_element->val);
}

/* Prepare new kernel thread object and return its pid */
int make_kernel_thread(char* name, void __attribute__((noreturn)) (*entry)()) {
    struct proc* p = kmalloc(sizeof(struct proc));

    p->pid = ++pid_now;
    p->type = PROC_TYPE_KERNEL;

    for(int i=0; i<8; i++)
        p->regs[i] = 0;
    p->arith_flags = 0;

    // set virtual pages to kernel mapping
    for(int i=0; i<16; i++) {
        p->mem_pages[i] = i;
        p->prog_pages[i] = i;
    }

    // set stack page to new page (thread)
    p->mem_pages[15] = first_free_page++;
    // setup sp and fp
    p->regs[7] = 0xffff;
    p->regs[5] = 0xffff;

    /* assembly BUG to resolve */
    p->pc = (int)entry+1;

    // reset blocked status
    p->sema_blocked = NULL;

    // initialize fd table as free
    for(int i=0; i<PROC_MAX_FILES; i++)
        p->open_files[i].vnode = NULL;

    // thread is ready to execute now
    p->state = PROC_STATE_RUNNABLE;

    strcpy(p->name, name);

    list_append(&proc_list, p);

    return p->pid;
}

struct proc* sched_init_user_thread() {
    struct proc* p = kmalloc(sizeof(struct proc));

    p->pid = ++pid_now;
    p->type = PROC_TYPE_USER;

    for(int i=0; i<8; i++)
        p->regs[i] = 0;
    p->arith_flags = 0;
    p->pc = 0;

    // set invalid virtual pages
    for(int i=0; i<16; i++) {
        p->mem_pages[i] = 0xff;
        p->prog_pages[i] = 0xff;
    }

    // allocate stack page
    p->mem_pages[15] = first_free_page++;
    // sp & fp
    p->regs[7] = 0xffff;
    p->regs[5] = 0xffff;

    // initialize fd table as free
    for(int i=0; i<PROC_MAX_FILES; i++)
        p->open_files[i].vnode = NULL;
    p->sema_blocked = NULL;

    p->state = PROC_STATE_UNLOADED;
    p->name[0] = '\0';

    list_append(&proc_list, p);
    return p;
}
