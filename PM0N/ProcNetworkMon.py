#!/usr/bin/python3
#-*- coding:utf-8 -*-

try:
    from Pmon import *
except ImportError:
    print("[!] Error Module : Pmon not found !")


__VERSION__ = "0.1"

banner = '''
\t___  _  _ _  _ ____ _  _ 
\t|__] |\ | |\/| |  | |\ | 
\t|    | \| |  | |__| | \|\n\n
\t\tAuthor : Unam3dd
\t\tGithub : https://github.com/Unam3dd
\t\tVersion : %s
                         
''' % (__VERSION__)

if __name__ == "__main__":
    a = PNMon()
    a.check_python_version()
    print(banner)
    if len(sys.argv) < 2:
        print("usage : %s -h" % (sys.argv[0]))
        print("        %s scan " % (sys.argv[0]))
        print("        %s scan <interface>" % (sys.argv[0]))
        print("        %s scan filter <process>" % (sys.argv[0]))
        print("        %s scan dll <pid>" % (sys.argv[0]))
        print("        %s kill <pid>\n\n" % (sys.argv[0]))
    else:
        if sys.argv[1] =="scan":
            if len(sys.argv) >=3:
                options = sys.argv[2]
                if options =="filter":
                    process = sys.argv[3]
                    a.get_network_process(iface=None,filter_=process)
                
                elif options =="dll":
                    a.show_dll(int(sys.argv[3]))
            else:
                a.get_network_process(iface=None,filter_=None)
        
        elif sys.argv[1] =="kill":
            if len(sys.argv) ==3:
                pid = sys.argv[2]
                p = a.kill_process(int(pid))
                if p ==True:
                    print("[*] %s Killed " % (pid))
                else:
                    print("[!] %s Not Killed " % (pid))

            else:
                print("[!] Error Options !")
        
        elif sys.argv[1] =="-h":
            print("usage : %s -h" % (sys.argv[0]))
            print("        %s scan " % (sys.argv[0]))
            print("        %s scan <interface>" % (sys.argv[0]))
            print("        %s scan filter <process>" % (sys.argv[0]))
            print("        %s scan dll <pid>" % (sys.argv[0]))
            print("        %s kill <pid>\n\n" % (sys.argv[0]))
        else:
            print("[!] Invalid Options")
