.386
.model flat, stdcall


include C:/masm32/include/user32.inc
includelib C:/masm32/lib/user32.lib


include C:/masm32/include/kernel32.inc
includelib C:/masm32/lib/kernel32.lib


.data
command db “calc.exe”, 0


.code
start:
push 1
push offset command
call WinExec


push 0
call ExitProcess


end start
