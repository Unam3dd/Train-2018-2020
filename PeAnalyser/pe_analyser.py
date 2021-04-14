#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author : Unam3dd

try:
    from panalyse import *
except ImportError:
    print("\033[38;5;196m[!] ImportError : panalyse not found !\033[00m")


banner = '''
\033[38;5;82m
___  ____    ____ _  _ ____ _    _   _ ____ ____ ____ 
|__] |___    |__| |\ | |__| |     \_/  [__  |___ |__/ 
|    |___    |  | | \| |  | |___   |   ___] |___ |  \ 
                                                      
            [     Github : \033[38;5;166mUnam3dd\033[38;5;82m    ]
            [ \033[38;5;196mSimple PE Analyser V0.1\033[38;5;82m ]
\033[00m
'''

if __name__ == "__main__":
    python_version()
    print(banner)
    if len(sys.argv) < 2:
        print("         \033[38;5;82musage : %s --help\033[00m" % (sys.argv[0]))
    else:
        if sys.argv[1] =="--help":
            print("            %s <pe> all      | Show All Informations" % (sys.argv[0]))
            print("            %s <pe> sections | Show sections" % (sys.argv[0]))
            print("            %s <pe> infos    | Show Infos by pefile" % (sys.argv[0]))
            print("            %s <pe> imports  | Show Imports" % (sys.argv[0]))
            print("            %s <pe> headers  | Show Headers" % (sys.argv[0]))
            print("            %s <pe> strings  | Show Strings\n\n" % (sys.argv[0]))
        else:
            filename = sys.argv[1]
            if len(sys.argv) == 3:
                mode = sys.argv[2]
                p = PE_Analyse(filename)
                if mode == "all":
                    p.get_headers()
                    p.show_sections()
                    p.show_imports()
                    for value in p.get_string():
                        print(value)
                else:
                    if mode =="sections":
                        p.show_sections()
                    
                    elif mode == "imports":
                        p.show_imports()
                    
                    elif mode =="infos":
                        p.print_infos()
                    
                    elif mode =="headers":
                        p.get_headers()
                    
                    elif mode =="strings":
                        for value in p.get_string():
                            print(value)

                    else:
                        print("\033[38;5;196m[!] Error Options for show help use %s --help" % (sys.argv[0]))
            else:
                p = PE_Analyse(filename)
                p.get_headers()
                p.show_sections()
                p.show_imports()
                for value in p.get_string():
                    print(value)