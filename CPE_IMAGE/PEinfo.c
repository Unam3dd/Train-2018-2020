#include <stdio.h>
#include <windows.h>

int main(int argc, char *argv[])
{

    if (argc < 2)
        printf("usage : %s <PE>\n",__FILE__);

    IMAGE_DOS_HEADER Dosheader = {0};
    PIMAGE_DOS_HEADER Pdosheader = {0};
    IMAGE_FILE_HEADER Fileheader = {0};
    IMAGE_OPTIONAL_HEADER Optionalheader = {0};
    FILE *fp;
    DWORD FPos,HeadersAddress,Signature;
    size_t SizeOfPEHeaders = sizeof(IMAGE_DOS_HEADER) + sizeof(IMAGE_NT_HEADERS);

    // Open File

    fp = fopen(argv[1],"rb"); // open filename in read binary mode

    if (fp == NULL){
        fprintf(stderr,"[-] Error : %s not found !",argv[1]);
        exit(-1);
    }

    if (fseek(fp,0,SEEK_END) != 0){
        fprintf(stderr,"[-] Error : moves the file pointer to a specifed location."); // moves the file pointer to a specifed location with fseek
        exit(-2);
    }

    FPos = ftell(fp); // returns the position of the argv[1]
    printf("[+] Current File Position : %#x\n",FPos);
    printf("[+] Size Of IMAGE_DOS_HEADER : %#x\n",sizeof(IMAGE_DOS_HEADER));
    printf("[+] Size Of IMAGE_NT_HEADERS : %#x\n",sizeof(IMAGE_NT_HEADERS));
    printf("[+] Total Size Of PE Headers : %#x\n",SizeOfPEHeaders);

    if (FPos < SizeOfPEHeaders){
        fprintf(stderr,"[-] Error : This file is not PE file !\n"); // Check if the header is inferior to that of a PE
        exit(-3);
    }

    // Reading PE
    fseek(fp,0,SEEK_SET);
    fread(&Dosheader,sizeof(Dosheader),1,fp); // puts and read fp to Dosheader

    // Check Magic Number

    if (Dosheader.e_magic != IMAGE_DOS_SIGNATURE){
        fprintf(stderr,"[-] Error : This file is not PE file ! cause DOS SIGNATURE is %#x != %#x\n",Dosheader.e_magic,IMAGE_DOS_SIGNATURE);
        exit(-4);
    }

    HeadersAddress = Dosheader.e_lfanew;

    printf("\n\n///////////////////////////////\n");
    printf("//       DOS HEADER         //\n");
    printf("/////////////////////////////\n");
    printf("\n");
    printf("[+] MZ DOS : %#x\n",Dosheader.e_magic);
    printf("[+] Address of PE Header : %#x\n\n\n",HeadersAddress);
    printf("[+] HeadersAddress Sizeof IMAGE_NT_HEADERS : %#x\n",HeadersAddress + sizeof(IMAGE_NT_HEADERS));

    if (FPos <= HeadersAddress + sizeof(IMAGE_NT_HEADERS)){
        fprintf(stderr,"[-] Error : This file is not PE file ! cause DOS SIGNATURE is %#x != %#x\n",Dosheader.e_magic,IMAGE_DOS_SIGNATURE);
        exit(-5);
    }

    fseek(fp,HeadersAddress,SEEK_SET);
    fread(&Signature,sizeof(DWORD),1,fp);
    printf("[+] Signature : %#x\n",Signature);

    fread(&Fileheader,sizeof(Fileheader),1,fp);
    fread(&Optionalheader,sizeof(Optionalheader),1,fp);
    printf("[+] Sections Number : %d\n",Fileheader.NumberOfSections);
    printf("[+] Size Of Optional Header : %d\n",Fileheader.SizeOfOptionalHeader);
    printf("[+] Address of EntryPoint : %#x\n",Optionalheader.AddressOfEntryPoint);
    printf("[+] Image Base : %#x\n",Optionalheader.ImageBase);
    printf("[+] Size of Image : %#x\n",Optionalheader.SizeOfImage);

    fclose(fp); // close file


    return (0);
}