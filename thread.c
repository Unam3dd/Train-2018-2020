#include <stdio.h>
#include <stdlib.h>
#include <process.h>
#include <windows.h>

DWORD WINAPI p(LPVOID lParam)
{
    for (int i = 0;i<10;i++)
    {
        printf("p->[%d]\n",i);
        Sleep(3000);
    }
}

DWORD WINAPI pp(LPVOID lParam)
{
    for (int i = 0;i<10;i++)
    {
        printf("pp->[%d]\n",i);
        Sleep(2000);
    }
}

void ThreadFirst()
{
    DWORD threadid1 = 0;
    DWORD threadid2 = 1;
    HANDLE hThread1 = CreateThread(NULL,0,&p,NULL,0,&threadid1);
    HANDLE hThread2 = CreateThread(NULL,0,&pp,NULL,0,&threadid2);
    printf("Hello World");
    WaitForSingleObject(hThread1,INFINITE);
    WaitForSingleObject(hThread2,INFINITE);
    CloseHandle(hThread1);
    CloseHandle(hThread2);
}

DWORD WINAPI show_hello()
{
    for (int x = 0;x<10;x++)
    {
        printf("Hello World\n");
        Sleep(1000);
    }
}

int main()
{
    //ThreadFirst();
    DWORD threadid1 = 0;
    DWORD threadid2 = 1;
    DWORD threadid3 = 3;
    HANDLE hThread1 = CreateThread(NULL,0,&p,NULL,0,&threadid1);
    HANDLE hThread2 = CreateThread(NULL,0,&pp,NULL,0,&threadid2);
    HANDLE hThread3 = CreateThread(NULL,0,&show_hello,NULL,0,&threadid3);
    // Check Thread Priority https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadpriority
    SetThreadPriority(hThread3,THREAD_PRIORITY_NORMAL); // hThread as THREAD_PRIORITY_NORMAL value by defaults
    int  Priority = GetThreadPriority(hThread3);
    printf("%d\n",Priority);
    HANDLE ThreadTab[3] = {hThread1,hThread2,hThread3};
    WaitForMultipleObjects(3,ThreadTab,TRUE,INFINITE);
    CloseHandle(hThread1);
    CloseHandle(hThread2);
    CloseHandle(hThread3);
}