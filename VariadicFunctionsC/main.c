#include <stdio.h>
#include <stdarg.h>

// wiki : https://fr.wikipedia.org/wiki/Fonction_variadique

int variadic_add(int n1, ...) // variadic functions
{
    va_list params;
    int c;
    int somme = 0;
    va_start(params, n1);
    somme = n1 + va_arg(params, int);
    va_end(params);
    return (somme);
}

int main()
{
    printf("%d\n", variadic_add(2,2));
    return (0);
}
