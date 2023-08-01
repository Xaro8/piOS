#ifndef DRIVER_KEYBOARD_H
#define DRIVER_KEYBOARD_H

#include <libk/types.h>

#define SCANCODE_ADDR (volatile u16*) 0x6
#define KEYBOARD_IRQ_ID 1

void print_scancode(uint8_t scancode);

#endif
