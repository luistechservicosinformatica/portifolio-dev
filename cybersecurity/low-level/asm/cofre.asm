section .data
secret db “senha123”, 0
secretlen equ $ - secret


openmsg db “segredo descoberto”, 0
openmsglen equ $ - openmsg


section .text
global _start


_start:
mov eax, [esp]
cmp eax, 1
jle end
mov esi, [esp+8]
mov edi, secret


compare_loop:
mov al, [esi]
mov ah, [edi]
cmp al, ah
jne end
cmp ah, 0
je open
inc esi
inc edi
jmp compare_loop


open:


mov eax,0x04
mov ebx, 1
mov ecx, openmsg
mov edx, openmsglen
int 0x80


end:
mov eax, 0x01
mov ebx, 0
int 0x80
