# CVector
Simple Vector implementation in C
Version : 0.1

```c
#include "vector.h"
#include <stdio.h>

int main(int argc, char **argv)
{
    Vector v;
    vector_object(&v);
    v.init(&v);
    v.push_back(&v,"Hello World");
    void * p = v.get(&v,0);
    printf("%s\n",p);
    int i = v.replace(&v,0,(int *)24);
    printf("%d\n",(void *)v.get(&v,0));
    v.push_back(&v,(double *)2);
    printf("%d\n",(void *)v.get(&v,1));
    printf("[+] Total items in arrays : %d\n",v.get_total(&v));
    printf("[+] Total Capacity of vector : %d\n",v.get_capacity(&v));
    v.pop_back(&v);
    v.replace(&v,0,"End");
    printf("%s\n",(void *)v.get(&v,0));
    printf("[+] Total items in arrays : %d\n",v.get_total(&v));
    printf("%d\n",v.isEmpty(&v));
    v.pop_back(&v);
    printf("%d\n",v.isEmpty(&v));
    v.push_back(&v,"Hello World");
    v.push_back(&v,"hl2");
    v.push_back(&v,"hl3");
    v.pop_back(&v);
    printf("%s\n",(void *)v.get(&v,0));
    void **items = v.get_items(&v);
    printf("%s\n",items[1]);
    v.free(&v);
    return (0);
}
```
