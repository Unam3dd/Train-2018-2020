package main

/*
#include <stdio.h>
#include <stdlib.h>
#include "hello.c"

void myprint(char* s) {
	printf("%s\n", s);
}
*/
import "C"

import "unsafe"

func main() {
	string := C.CString("Hello World\n")
	C.myprint(string)
	C.free(unsafe.Pointer(cs))
	C.Hello()
}
