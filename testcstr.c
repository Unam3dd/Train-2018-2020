#include <stdio.h>
#include "cstr.h"

int main()
{
    char name[] = "Hello|World";
    char buffer[1024] = {0};
    char str1[] = "olo";
    char str2[] = "lol";
    char issou[10] = {0};
    stringcopy(buffer,name);
    printf("%s\n",buffer);
    printf("%d\n",stringlength(buffer));
    stringconcat(issou,"testKOFKEOFKEOPFKEPOFKZEFKPOKPOZEKFPOZEKFPOZEKFPOZEKFZEK");
    printf("%s\n",buffer);
    printf("%s\n",issou);
    
    if (stringcompare(str1,str2) != true)
        fprintf(stderr,"[-] %s not equal to %s\n",str1,str2);
    else
        printf("[+] Its Equal %s:%s\n",str1,str2);
    
    stringupper(str1,str1);
    printf("%s\n",str1);
    stringlower(str1,str1);
    printf("%s\n",str1);
    stringcharreplace(str1,'o','a',str1);
    printf("%s\n",str1);
    stringcharreplacepos(str1,'a','o',2,str1);
    printf("%s\n",str1);
    printf("%d\n",stringsearchchargetpos(str1,'o'));
    printf("%d\n",stringsubstr(name,"name"));
    char **out = splitchar(name,'|');
    printf("%s\n",out[0]);
    free(out);
    return (0);
}