; 00050004
; 0001000E
.romd


set_program_mem:
    srl r4, 1 ; save flags

    srs r1, 0x10 ; set page zero mapping

    ldi r3, 0 ; loop counter
    cl_set_program_mem_loop:
        ldo r2, r0, 0 ; load pointer - we need to access memory before setting memory override
        ldi r1, 0b1011 ; flags: SUP, IMO - InstructionMemoryOverride no memory access allowed later, and MEMory PAGing
        srs r1, 1
        sto r2, r3, 0 ; store in new block pointer from r0
        ldi r1, 0b1 ; diable IMO, MEMPG
        srs r1, 1
        adi r0, r0, 2 ; increment pointer (gcc bug +2)
        adi r3, r3, 1 ; increment loop counter
        cmi r3, 0x1000 ; page size
        jne cl_set_program_mem_loop

    srs r4, 1

    ldi r1, 0
    srs r1, 0x10 ; reset page zero mapping

    srs r6, 0 ; return

set_ram_mem:
    srl r4, 1
    ori r4, r4, 0x8 ; same as before but do not set instr override
    srs r4, 1

    srs r1, 0x10 ; set page zero mapping

    ldi r3, 0 ; loop counter
    cl_set_ram_mem_loop:
        ldo r2, r0, 0 ; this is fine - buffer not in page0
        sto r2, r3, 0 ; store in new block pointer from r0
        adi r0, r0, 2 ; increment pointer (gcc bug +2)
        adi r3, r3, 1 ; increment loop counter
        cmi r3, 0x1000 ; page size
        jne cl_set_ram_mem_loop

    ani r4, r4, 0xf7 ; disable MEMPAG
    srs r4, 1

    ldi r1, 0
    srs r1, 0x10 ; reset page zero mapping

    srs r6, 0 ; return

c_switch:
    srl r0, 1
    ori r0, r0, 0x4 ; enable mem paging
    srs r0, 1

    ldi r0, 0b10
    srs r0, 2 ; set jtr rom paging

    ; TODO: set registers

    jmp zero


.ramd