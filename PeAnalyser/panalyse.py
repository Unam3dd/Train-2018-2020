#-*- coding:utf-8 -*-

import sys
import os
import string

try:
    import pefile
except ImportError:
    print("\033[38;5;196m[!] ImportError : Pefile Not Found !\033[00m")

try:
    from tabulate import tabulate
except ImportError:
    print("\033[38;5;196m[!] ImportError : Tabulate Not Found !\033[00m")

try:
    import hashsum
except ImportError:
    print("\033[38;5;196m[!] ImportError : HashSum Not Found !\033[00m")

try:
    import binascii
except ImportError:
    print("\033[38;5;196m[!] ImportError : Binascii Not Found !\033[00m")

def python_version():
    if sys.version[0] =="2":
        sys.exit("\033[38;5;196m[!] Please Use Python 3.x\033[00m")


class PE_Analyse:

    def __init__(self,filename):
        self.filename = filename
        if self.check_file(self.filename) == True:
            print("[ \033[38;5;82mOK\033[00m ] TARGET FILE  : \033[38;5;82m%s \033[00m " % (self.filename))
            print("[ \033[38;5;214mINFO\033[00m ] MD5 BIN HASH : \033[38;5;82m%s \033[00m" % (hashsum.md5sum_bin(self.filename)))
            print("[ \033[38;5;214mINFO\033[00m ] MD5 RAW HASH : \033[38;5;82m%s \033[00m" % (hashsum.md5sum(self.filename)))
        else:
            print("[ \033[38;5;196mFAILED\033[00m ] \033[38;5;196m%s Not Found !\033[00m" % (self.filename))
            sys.exit(1)
    
    def check_file(self, filename):
        try:
            check_file = os.path.exists(filename)
            return check_file
        except Exception as error_check_file:
            print(error_check_file)
        
    def show_sections(self):
        try:
            p = pefile.PE(self.filename)
            
            sections_table = []

            for sections in p.sections:
                sec_name = sections.Name
            
                sections_table.append([sec_name.split(b"\x00")[0],hex(sections.VirtualAddress), sections.SizeOfRawData])
            
            print("[ \033[38;5;82mOK\033[00m ] Sections Have been Analyzed Wait Moment....")

            headers = ["Sections Name","VirtualAddress","Size Of Raw Data"]

            print(tabulate(sections_table,headers=headers,tablefmt="fancy_grid"))
        
        except Exception as error_show_sections:
            print(error_show_sections)
    

    def show_imports(self):
        try:
            p = pefile.PE(self.filename)

            entry_table = []

            headers = ["DLL","Imports Name","Imports Address"]

            for entry in p.DIRECTORY_ENTRY_IMPORT:
                for imports in entry.imports:
                    entry_table.append([entry.dll,imports.name,hex(imports.address)])
            
            print("[ \033[38;5;82mOK\033[00m ] Imports Have been Analyzed Wait Moment....")

            print(tabulate(entry_table,headers=headers,tablefmt="fancy_grid"))
        
        except Exception as error_show_imports:
            print(error_show_imports)
    
    def print_infos(self):
        try:
            p = pefile.PE(self.filename)
            p.print_info()
        except Exception as error_print_infos:
            print(error_print_infos)
    
    def get_headers(self):
        try:
            
            p = pefile.PE(self.filename)
            magic_number = hex(p.DOS_HEADER.e_magic)
            pointer_exe = hex(p.DOS_HEADER.e_lfanew)
            
            if magic_number =="0x5a4d":
                name_magic = "MZ"
            else:
                name_magic = "Other"
            

            addr_signed = p.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_SECURITY']].VirtualAddress
            if addr_signed == 0:
                signed_pe = "Unsigned"
                signature = hex(p.NT_HEADERS.Signature)
            else:
                signed_pe = "Signed"
                signature = hex(p.NT_HEADERS.Signature)
            
            if hex(p.FILE_HEADER.Machine) == '0x14c':
                arch = "x86 (32-bit binary)"
                hex_arch_value = hex(p.FILE_HEADER.Machine)
            else:
                arch = "x86_64 (64-bit binary)"
                hex_arch_value = hex(p.FILE_HEADER.Machine)
            
            time_date = p.FILE_HEADER.dump_dict()["TimeDateStamp"]["Value"].split('[')[1][:-1]

            number_sections = hex(p.FILE_HEADER.NumberOfSections)
            char_flags = hex(p.FILE_HEADER.Characteristics)
            image_base = hex(p.OPTIONAL_HEADER.ImageBase)
            size_image = hex(p.OPTIONAL_HEADER.SizeOfImage)


            headers_1 = ["Magic Number","Name","Headers","ImageBase","Size Of Image"]
            headers_2 = ["Signed","Signature"]
            headers_3 = ["Architecture","Architecture Hex Value","Time Date Stamp","Number Sections","Characteristics Flags"]

            headers_info = []
            headers_info_sign = []
            headers_info_headers = []

            headers_info.append([magic_number,name_magic,pointer_exe,image_base,size_image])
            headers_info_sign.append([signed_pe,signature])
            headers_info_headers.append([arch,hex_arch_value,time_date,number_sections,char_flags])
            print(tabulate(headers_info,headers=headers_1,tablefmt="fancy_grid"))
            print(tabulate(headers_info_sign,headers=headers_2,tablefmt="fancy_grid"))
            print(tabulate(headers_info_headers,headers=headers_3,tablefmt="fancy_grid"))
        
        except Exception as error_get_headers:
            print(error_get_headers)
    

    def get_string(self):
        with open(self.filename,"rb") as f:
            result = ""
            content = f.read().decode("cp437")
            for c in content:
                if c in string.printable:
                    result += c
                    continue
                if len(result) >= 4:
                    yield result
                    result = ""
                
                if len(result) >= 4:
                    yield result

    def get_strings(self):
        try:
            self.get_string()
            print("[ \033[38;5;82mOK\033[00m ] Imports Have been Analyzed Wait Moment....")
            print(string_ext)

        except Exception as error_get_strings:
            print(error_get_strings)
