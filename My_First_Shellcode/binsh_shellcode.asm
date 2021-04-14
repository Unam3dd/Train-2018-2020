; nasm -f elf64 binsh_shellcode && ld binsh_shellcode.o -o binssh
BITS 64

global _start

section .data
    string_exec db `//bin/sh`
    size_string equ $-string_exec

section .text
_start:
    mov rax, 59 ; syscall
    mov rdi, string_exec ; /bin/sh
    mov rsi, 0x0 ; NULL
    mov rdx, 0x0 ; NULL
    syscall
    jmp _exit

_exit:
    mov rax, 60
    mov rdi, 0
    syscall