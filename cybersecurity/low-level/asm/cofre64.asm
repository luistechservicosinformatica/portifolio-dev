section .data
secret db “senha123”, 0
secretlen equ $ - secret


openmsg db “segredo descoberto”, 0
openmsglen equ $ - openmsg


section .text
global _start


_start:
mov rax, [rsp]
cmp rax, 1
jle end
mov rsi, [rsp+16]
mov rdi, secret


compare_loop:
mov al, [rsi]
mov ah, [rdi]
cmp al, ah
jne end
cmp ah, 0
je open
inc rsi
inc rdi
jmp compare_loop


open:


mov rax,0x01
mov rdi, 1
mov rci, openmsg
mov rdx, openmsglen
syscall


end:
mov rax, 0x3c
mov rdi, 0
syscall
