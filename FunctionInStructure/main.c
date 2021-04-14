#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

// Author : Unam3dd - 2020 C Train

typedef struct mystruct {
    char name2[100];
    int number;
    char name[100];
    int (*func)(const char *const _Format, ...);
    int (*calc)(int a, int b);
} mystruct;

int add(int a, int b)
{
    return (a+b);
}

// Varidiac function with formats

void variadic_functions(mystruct *t,const char *format,...)
{
    char *buffer;
    int i;
    va_list params;
    va_start(params,format);

    while (*format != '\0')
    {
        if (*format == 's')
        {
            buffer = va_arg(params,char *);
            strcpy(t->name2,buffer);
        } else if (*format == 'i' || *format == 'd'){
            i = va_arg(params,int);
            t->number = i;
        }
        format++;
    }
    va_end(params);
}

int main()
{
    mystruct t;
    memset(&t,0,sizeof(t));
    strcpy(t.name,"Jean");
    t.func = printf;
    t.calc = add;
    t.func("hello %s\n",t.name);
    printf("%d\n",t.calc(2,2));
    variadic_functions(&t,"si","Unam3dd",2);
    printf("%s\n",t.name2);
    printf("%d\n",t.number);
    return (0);
}
