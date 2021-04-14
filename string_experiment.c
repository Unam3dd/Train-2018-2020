#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct n{
    char name[80];
    char *n;
} n_t;

int main()
{
    // single character, integer type
    
    char letter = 'A'; // 65 (int) in ascii

    // string literal, stored as read-only data
    char *name1 = "Hello World";

    // character array initialized from string literal, copied to and stored on the stack
    char name2[] = "Hello World 2";

    // exact same as above
    char name3[] = {'H','E','L','O','W','O','R','L','D','\0'}; // with \0 for null terminated strings

    char name4[128];
    char *ptr = calloc(strlen(name1),sizeof(char));
    char *ptr2 = malloc(sizeof(char) * strlen(name1));
    
    memcpy(ptr2,name1,strlen(name1)); // copy memory of name1 
    
    strcpy(name4,"Hello World"); // Hello World\0 strcpy copy the string in name4
    ptr = name4;
    printf("%s\n",name4);
    printf("%d\n", strlen(name4));

    printf("%c\n",name4[0]);
    printf("%d\n",name4[0]);
    
    for (int x = 0;x<strlen(name4);x++)
    {
        printf("%d\t->\t%c\n",name4[x],name4[x]);
    }
    
    printf("%s\n",name4);
    printf("%s\n",name3);
    printf("Show Pointer Content => %s\n",ptr);
    printf("Show Pointer two => %s\n",ptr2);

    // change boundary of string
    name4[5] = '\0';

    printf("%s\n",name4);
    
    free(ptr);
    free(ptr2);

    n_t nn;
    nn.n = "test";
    strcpy(nn.name,"hello world from strcpy");

    printf("%s\n",nn.n);
    printf("%s\n",nn.name);

    return (EXIT_SUCCESS);
}