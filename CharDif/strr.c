#include <stdio.h>
#include <string.h>

// compile : gcc strr.c -S -masm=intel -o strr

int main()
{
	char *hl = "Hello World"; // char * hl = "Hello World" will store "Hello World in the .rodata section (read only data) this section is only available in read-only mode, hence the code dumped segmentation error when you want to modify (write) it.
	char hl2[] = "hello test"; // this == char hl2[5]; hl2[0] = 'h';
						 // hl2[1] = 'e'; hl2[2] = 'l'; hl2[3] = 'l'; hl2[4] = 'o';
	char hl3[100] = "This array contains 100 bytes cause (1 char = 1 byte)"; // as well as the previous variable the one if can be modified because it is not in the .rodata section.



	printf("%s\n",hl);
	hl = "lol";
	printf("%s\n",hl);
	puts(hl2);
	puts(hl3);
	//strcpy(hl,"lol2"); // segmentation error ! cause strcpy try write in hl
	//printf("%s\n",hl);
	strcpy(hl2,"New hello");
	printf("%s\n",hl2);
	strcpy(hl3,"New Hl3 variable");
	puts(hl3);
	return (0);
}