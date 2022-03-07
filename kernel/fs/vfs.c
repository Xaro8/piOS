#include "vfs.h"

#include <libk/assert.h>
#include <libk/list.h>
#include <libk/kmalloc.h>
#include <libk/string.h>

static int vfs_id = 0;

struct vfs_node {
    int vid;
    char* name;
    struct vfs_reg* handles;
    struct vfs_node* parent;

    struct list subdirs;

    char* path_search; // FIXME: find better way to do this
};

static struct vfs_node vfs_root;

void vfs_init() {
    vfs_root.name = kmalloc(2);
    vfs_root.parent = &vfs_root;
    strcpy(vfs_root.name, "/");
    vfs_root.handles = NULL;
}

struct vfs_node* vnode_tree_create(char* path);
struct vfs_node* vnode_tree_find(char* path);

int vfs_mount(char* path, struct vfs_reg* handles) {
    ASSERT(path[0] == '/');

    struct vfs_node* node = vnode_tree_create(path);
    node->handles = handles;
    node->vid = ++vfs_id;

    return 0;
}

int vfs_open(char* path) {
    struct vfs_node* vnode = vnode_tree_find(path);
    if(!vnode)
        return -ENOTFOUND;

    // call open on handle with suffix of path
    int file_inode = (*vnode->handles->open)(vnode->path_search);

    return -1;
}

struct vfs_node* vnode_tree_find(char* path) {
    struct vfs_node* node = &vfs_root;

    char* dirname = ++path;  // skip first slash (already matched in vfs_root)
    char* next_tok = path;
    while((next_tok = strchr(next_tok+1, '/')) != NULL) {
        int subdir_found = 0;
        // FIXME: support /.././
        list_foreach(&node->subdirs) {
            struct vfs_node* sub = LIST_FOREACH_VAL(struct vfs_node*);
            if(strncmp(dirname, sub->name, next_tok-dirname+1) == 0) {
                node = sub;
                node->path_search = next_tok;
                dirname = next_tok+1;
                subdir_found = 1;
                break;
            }
        }
        if(subdir_found)
            continue;

        // vnode not found -> use last vnode with handles set
        while(node != &vfs_root) {
            if(node->handles)
                return node;

            node = node->parent;
        }
        return NULL;
    }
    return node;
}

struct vfs_node* vnode_tree_create(char* path) {
    struct vfs_node* node = &vfs_root;

    char* dirname = ++path; // skip first slash (already matched in vfs_root)
    char* next_tok = path;
    while((next_tok = strchr(next_tok+1, '/')) != NULL) {
        int subdir_found = 0;
        list_foreach(&node->subdirs) {
            struct vfs_node* sub = LIST_FOREACH_VAL(struct vfs_node*);
            if(strncmp(dirname, sub->name, next_tok-dirname+1) == 0) {
                // enter next node in path
                node = sub;
                dirname = next_tok+1;
                subdir_found = 1;
                break;
            }
        }
        if(subdir_found)
            continue;

        // vnode for dir not found, create one
        struct vfs_node* new_node = kmalloc(sizeof(struct vfs_node));
        new_node->name = kmalloc(next_tok-path+2);
        new_node->parent = node;
        strprefcpy(new_node->name, dirname, next_tok-dirname+1);
        list_init(&new_node->subdirs);
        list_append(&node->subdirs, new_node);
        dirname = next_tok+1;
        node = new_node;
    }
    return node;
}

