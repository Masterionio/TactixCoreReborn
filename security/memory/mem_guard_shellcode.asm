section .data
    msg db "[Shellcode] Memory trap active", 0

section .text
    global _start
_start:
    mov eax, 4      ; sys_write
    mov ebx, 1      ; stdout
    mov ecx, msg
    mov edx, 27
    int 0x80

    mov eax, 1      ; sys_exit
    xor ebx, ebx
    int 0x80
