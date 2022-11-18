; 00050004
; 0001000E
.romd

; r0-data* r1-page r2-end_addr r3-off
set_program_mem:
    ; save pc on stack
    sto r6, r7, 0
    ; NOTE: We can't store flags on stack, because flags include paging, which we need to access stack to recover
    srl r4, 1
    mov r6, r4 ; save old flags

    ldi r1, 0b011 ; flags: SUP and MEMory PAGing

    ori r1, r1, 0x1000 ; set page 0 as load to program memory
    srs r1, 0x100 ; set page zero mapping

    mov r4, r2
    ; r3 - loop counter
    cl_set_program_mem_loop:
        ldo r2, r0, 0 ; load pointer - we need to access memory before setting memory override
        ldi r1, 0b01011 ; flags: SUP, IMO - InstructionMemoryOverride no memory access allowed later, and MEMory PAGing
        srs r1, 1
        sto r2, r3, 0 ; store in new block pointer from r0
        ldi r1, 0b10001 ; diable IMO, MEMPG and enable MEMSTD
        srs r1, 1
        adi r0, r0, 2 ; increment pointer (u16*)
        adi r3, r3, 1 ; increment loop counter
        cmp r3, r4 ; end addr
        jle cl_set_program_mem_loop

    srs r6, 1  ; recover old flags

    ldi r1, 0
    srs r1, 0x10 ; reset page zero mapping

    ldo r6, r7, 0 ; recover pc from stack
    srs r6, 0 ; return

; r0-data* r1-page r2-end_addr r3-off
set_ram_mem:
    sto r6, r7, 0 ; save pc on stack
    srl r4, 1
    mov r6, r4 ; save old flags
    ori r4, r4, 0x2 ; same as before but do not set instr override
    srs r4, 1

    srs r1, 0x100 ; set page zero mapping

    mov r1, r2

   ; r3 - loop counter
    cl_set_ram_mem_loop:
        ldo r2, r0, 0 ; this is fine - buffer must not be in page0
        sto r2, r3, 0 ; store in new block pointer from r0
        adi r0, r0, 2 ; increment pointer (u16*)
        adi r3, r3, 2 ; increment loop counter
        cmp r3, r1 ; end addr
        jle cl_set_ram_mem_loop

    ; load old flags
    srs r6, 1

    ldi r1, 0
    srs r1, 0x10 ; reset page zero mapping

    ldo r6, r7, 0 ; recover pc from stack
    srs r6, 0 ; return

; set virtual page mapping to values in struct
; @param r0 pointer to mem_pages*16 + prog_pages*16
set_mapping_from_struct:
    ldo r1, r0, 0
    srs r1, 0x200
    ldo r1, r0, 2
    srs r1, 0x201
    ldo r1, r0, 4
    srs r1, 0x202
    ldo r1, r0, 6
    srs r1, 0x203
    ldo r1, r0, 8
    srs r1, 0x204
    ldo r1, r0, 10
    srs r1, 0x205
    ldo r1, r0, 12
    srs r1, 0x206
    ldo r1, r0, 14
    srs r1, 0x207
    ldo r1, r0, 16
    srs r1, 0x208
    ldo r1, r0, 18
    srs r1, 0x209
    ldo r1, r0, 20
    srs r1, 0x20a
    ldo r1, r0, 22
    srs r1, 0x20b
    ldo r1, r0, 24
    srs r1, 0x20c
    ldo r1, r0, 26
    srs r1, 0x20d
    ldo r1, r0, 28
    srs r1, 0x20e
    ldo r1, r0, 30
    srs r1, 0x20f
    ldo r1, r0, 32
    srs r1, 0x100
    ldo r1, r0, 34
    srs r1, 0x101
    ldo r1, r0, 36
    srs r1, 0x102
    ldo r1, r0, 38
    srs r1, 0x103
    ldo r1, r0, 40
    srs r1, 0x104
    ldo r1, r0, 42
    srs r1, 0x105
    ldo r1, r0, 44
    srs r1, 0x106
    ldo r1, r0, 46
    srs r1, 0x107
    ldo r1, r0, 48
    srs r1, 0x108
    ldo r1, r0, 50
    srs r1, 0x109
    ldo r1, r0, 52
    srs r1, 0x10a
    ldo r1, r0, 54
    srs r1, 0x10b
    ldo r1, r0, 56
    srs r1, 0x10c
    ldo r1, r0, 58
    srs r1, 0x10d
    ldo r1, r0, 60
    srs r1, 0x10e
    ldo r1, r0, 62
    srs r1, 0x10f

    srs r6, 0 ; return 

; @param r0 ptr to registeres
c_switch:
    ; load arithmetic flags
    ldo r1, r0, 18
    srs r1, 4

    ; store pc to iret scratch register
    ldo r1, r0, 16
    srs r1, 3 

    ; save r0 to scratch reg for later recovery (where normal memory cannot be accessed)
    ldo r1, r0, 0
    srs r1, 6

    ; registers must be recovered from memory before mem paging is enabled
    ldo r1, r0, 2
    ldo r2, r0, 4
    ldo r3, r0, 6
    ldo r4, r0, 8
    ldo r5, r0, 10
    ldo r6, r0, 12
    ldo r7, r0, 14

    ldi r0, 0x3 ; enable ram paging and priv. *remember about arithmetic flags!*; irq is set by iret
    srs r0, 1

    ldi r0, 0x1
    srs r0, 2 ; set jtr rom paging

    srl r0, 6 ; recover r0 saved before paging enable

    irt ; jump to pc stored in sr3 and enable interrupts


enable_default_memory_paging_asm:
    ldi r1, 0x0 ; illegal page
    srs r1, 0x200
    ldi r1, 0x201 ; 2nd SDRAM page
    srs r1, 0x201
    ldi r1, 0x202
    srs r1, 0x202
    ldi r1, 0x203
    srs r1, 0x203
    ldi r1, 0x204
    srs r1, 0x204
    ldi r1, 0x205
    srs r1, 0x205
    ldi r1, 0x206
    srs r1, 0x206
    ldi r1, 0x207
    srs r1, 0x207
    ldi r1, 0x208
    srs r1, 0x208
    ldi r1, 0x209
    srs r1, 0x209
    ldi r1, 0x20a
    srs r1, 0x20a
    ldi r1, 0x20b
    srs r1, 0x20b
    ldi r1, 0x20c
    srs r1, 0x20c
    ldi r1, 0x20d
    srs r1, 0x20d
    ldi r1, 0x20e
    srs r1, 0x20e
    ldi r1, 0x20f
    srs r1, 0x20f

    srl r1, 1
    ori r1, r1, 0b10 ; enable  MEMory PAGing
    srs r1, 1

    srs r6, 0


; Thread to schedule when no process is ready. It is interruptable and not allowed to use memory
idle_task:
    ldi r0, 0
    idle_task_l:
        jmp idle_task_l

.ramd
