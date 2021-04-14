; nasm -f elf32 hl.asm -o hello_world.o
; ld -m elf_i386 -o hello_world hello_world.o

global _start

section .text
_start:
	mov eax, 0x4 	 ; syscall_write (0x4)
	mov ebx, 1   	 ; stdout file descriptor (fd)
	mov ecx, message ; message
	mov edx, size    ; size of message
	int 0x80         ; call syscall


	mov eax,0x1    	; syscall (sys_exit) = 0x01
	mov ebx,0       ; status exit (0)
	int 0x80        ; call syscall

section .data
	message db "Hello World Assembly",0xa
	size equ $ - message
