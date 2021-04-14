#include <stdio.h>
#include "awesome.h"

int main(){
    PopShell();
    GoInt a = Add(1,1);
    printf("%d\n",a);
    GoString s = {"Hello",6};
    Say(s);
    return 0;
}