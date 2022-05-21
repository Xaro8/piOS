#include "sysd.h"

#include <driver/tty.h>
#include <proc/sched.h>
#include <proc/virtual.h>

#include <libk/con/blockq.h>
#include <libk/log.h>
#include <libk/kmalloc.h>

struct blockq syscall_q;

void process_syscall(struct proc* proc) {
    int sysno = proc->regs[0];
    switch (sysno) {
        case SYS_DUMP: {
            log("PID: %d DUMP r0:0x%x r1:0x%x r2:0x%x r3:0x%x r4:0x%x r5:0x%x r6:0x%x r7:0x%x vpc:0x%x",
                proc->pid, proc->regs[0], proc->regs[1], proc->regs[2], proc->regs[3], proc->regs[4], proc->regs[5],
                proc->regs[6], proc->regs[7], proc->pc);
            break;
        }
        case SYS_PRINT: {
            char* pb = kmalloc(proc->regs[2]);
            memcpy_from_userspace(pb, proc, proc->regs[1], proc->regs[2]);
            tty_direct_write(pb, proc->regs[2]);
            kfree(pb);
            break;
        }
        default: {
            log("PID: %d Illegal syscall (%d)", proc->pid, sysno);
            break;
        }
    }
}

__attribute__((noreturn)) void syscall_dispatcher() {
    for(;;) {
        int proc_pid;
        blockq_pop(&syscall_q, &proc_pid);
        struct proc* proc = proc_by_pid(proc_pid);
        process_syscall(proc);
        log("PID: %d resuming from syscall", proc_pid);
        proc->state = PROC_STATE_RUNNABLE;
    }
}

int sysd_submit(int pid) {
    if(syscall_q.size == syscall_q.max_size) {
        log_irq("[E] SYSQ is full. Dropping syscall");
        return -1;
    }

    blockq_push_nonblock(&syscall_q, &pid);
    current_proc->state = PROC_STATE_SYSCALL;
    return 0;
}

void sysd_init() {
    blockq_init(&syscall_q, 128, sizeof(int));
    make_kernel_thread("sysd", syscall_dispatcher);
}
