#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys

try:
    from datetime import datetime
    import psutil
    import platform
    import os
    import signal
    from tabulate import tabulate
except ImportError as error_module:
    print("[!] Error Import : %s" % (error_module))


class PNMon:
    def __init__(self):
        pass


    def check_python_version(self):
        if sys.version[0] == "2":
            sys.exit("[*] Python3 Required !")

    def get_network_process(self,iface=None,filter_=None):
        if iface ==None:
            if filter_ ==None:
                table = []
                headers = ["PID/NAME","PPID/PNAME","Address Family","Socket Type","Listening Address:Port","Remote Address:Port","Status"]
                p = psutil.net_connections()
                for instance in p:
                    pid = instance[6]
                    if psutil.Process(int(pid)).parent():
                        ppid = psutil.Process(int(pid)).parent().pid
                    else:
                        ppid = 0

                    laddr_section = instance[3]
                    raddr_section = instance[4]
                    pid_name = self.get_pid_name(pid)
                    if ppid !=0:
                        ppid_name = psutil.Process(int(pid)).parent().name()
                    else:
                        ppid_name = "System"
                    spid = "%d/%s" % (pid,pid_name)
                    sppid = "%d/%s" % (ppid,ppid_name)
                    family_addr = instance[1].name
                    socket_type = instance[2].name
                
                    if laddr_section:
                        laddr = laddr_section[0]
                        lport = laddr_section[1]
                        saddr_port = "%s:%s" % (laddr,lport)
                    else:
                        laddr = "NULL"
                        lport = "NULL"
                        saddr_port = "%s:%s" % (laddr,lport)
                
                    if raddr_section:
                        raddr = raddr_section[0]
                        rport = raddr_section[1]
                        taddr_port = "%s:%s" % (raddr,rport)
                    else:
                        raddr = "NULL" 
                        rport = "NULL"
                        taddr_port = "%s:%s" % (raddr,rport)
                

                    status = instance[5]
                    table.append([spid,sppid,family_addr,socket_type,saddr_port,taddr_port,status])

                print(tabulate(table,headers=headers,tablefmt="fancy_grid"))
            else:
                f = filter_
                table = []
                headers = ["PID/NAME","PPID/PNAME","Address Family","Socket Type","Listening Address:Port","Remote Address:Port","Status"]
                p = psutil.net_connections()
                for instance in p:
                    pid = instance[6]
                    if psutil.Process(int(pid)).parent():
                        ppid = psutil.Process(int(pid)).parent().pid
                    else:
                        ppid = 0

                    laddr_section = instance[3]
                    raddr_section = instance[4]
                    pid_name = self.get_pid_name(pid)
                    if ppid !=0:
                        ppid_name = psutil.Process(int(pid)).parent().name()
                    else:
                        ppid_name = "System"

                    spid = "%d/%s" % (pid,pid_name)
                    sppid = "%d/%s" % (ppid,ppid_name)
                    family_addr = instance[1].name
                    socket_type = instance[2].name
                
                    if laddr_section:
                        laddr = laddr_section[0]
                        lport = laddr_section[1]
                        saddr_port = "%s:%s" % (laddr,lport)
                    else:
                        laddr = "NULL"
                        lport = "NULL"
                        saddr_port = "%s:%s" % (laddr,lport)
                
                    if raddr_section:
                        raddr = raddr_section[0]
                        rport = raddr_section[1]
                        taddr_port = "%s:%s" % (raddr,rport)
                    else:
                        raddr = "NULL" 
                        rport = "NULL"
                        taddr_port = "%s:%s" % (raddr,rport)
                

                    status = instance[5]
                    if pid_name == f:
                        table.append([spid,sppid,family_addr,socket_type,saddr_port,taddr_port,status])
                    else:
                        pass

                print(tabulate(table,headers=headers,tablefmt="fancy_grid"))
        
        else:
            if filter_ ==None:
                table = []
                headers = ["PID/NAME","PPID/PNAME","Address Family","Socket Type","Listening Address:Port","Remote Address:Port","Status"]
                p = psutil.net_connections(iface)
                for instance in p:
                    pid = instance[6]
                    if psutil.Process(int(pid)).parent():
                        ppid = psutil.Process(int(pid)).parent().pid
                    else:
                        ppid = 0
                    ppid = psutil.Process(int(pid)).parent().pid
                    laddr_section = instance[3]
                    raddr_section = instance[4]
                    pid_name = self.get_pid_name(pid)
                    if ppid !=0:
                        ppid_name = psutil.Process(int(pid)).parent().name()
                    else:
                        ppid_name = "System"
                    spid = "%d/%s" % (pid,pid_name)
                    sppid = "%d/%s" % (ppid,ppid_name)
                    family_addr = instance[1].name
                    socket_type = instance[2].name
                
                    if laddr_section:
                        laddr = laddr_section[0]
                        lport = laddr_section[1]
                        saddr_port = "%s:%s" % (laddr,lport)
                    else:
                        laddr = "NULL"
                        lport = "NULL"
                        saddr_port = "%s:%s" % (laddr,lport)
                
                    if raddr_section:
                        raddr = raddr_section[0]
                        rport = raddr_section[1]
                        taddr_port = "%s:%s" % (raddr,rport)
                    else:
                        raddr = "NULL" 
                        rport = "NULL"
                        taddr_port = "%s:%s" % (raddr,rport)
                

                    status = instance[5]
                    table.append([spid,sppid,family_addr,socket_type,saddr_port,taddr_port,status])

                print(tabulate(table,headers=headers,tablefmt="fancy_grid"))
            
            else:
                f = filter_
                table = []
                headers = ["PID/NAME","PPID/PNAME","Address Family","Socket Type","Listening Address:Port","Remote Address:Port","Status"]
                p = psutil.net_connections()
                for instance in p:
                    pid = instance[6]
                    if psutil.Process(int(pid)).parent():
                        ppid = psutil.Process(int(pid)).parent().pid
                    else:
                        ppid = 0
                    ppid = psutil.Process(int(pid)).parent().pid
                    laddr_section = instance[3]
                    raddr_section = instance[4]
                    pid_name = self.get_pid_name(pid)
                    if ppid !=0:
                        ppid_name = psutil.Process(int(pid)).parent().name()
                    else:
                        ppid_name = "System"

                    spid = "%d/%s" % (pid,pid_name)
                    sppid = "%d/%s" % (ppid,ppid_name)
                    family_addr = instance[1].name
                    socket_type = instance[2].name
                
                    if laddr_section:
                        laddr = laddr_section[0]
                        lport = laddr_section[1]
                        saddr_port = "%s:%s" % (laddr,lport)
                    else:
                        laddr = "NULL"
                        lport = "NULL"
                        saddr_port = "%s:%s" % (laddr,lport)
                
                    if raddr_section:
                        raddr = raddr_section[0]
                        rport = raddr_section[1]
                        taddr_port = "%s:%s" % (raddr,rport)
                    else:
                        raddr = "NULL" 
                        rport = "NULL"
                        taddr_port = "%s:%s" % (raddr,rport)
                

                    status = instance[5]
                    if pid_name == f:
                        table.append([spid,sppid,family_addr,socket_type,saddr_port,taddr_port,status])
                    else:
                        pass

                print(tabulate(table,headers=headers,tablefmt="fancy_grid"))
    

    def get_pid_name(self,pid):
        try:
            proc_name = psutil.Process(pid).name()
            return proc_name
        except Exception as error_get_pid_name:
            return error_get_pid_name
    

    def show_dll(self,pid):
        try:
            p = psutil.Process(pid)
            g_name = self.get_pid_name(pid)
            pp_name = "%d/%s" % (pid,g_name)
            table = []
            headers = ["PID/NAME","DLL Loadeds"]
            for dll in p.memory_maps():
                table.append([pp_name,dll.path])
            
            print(tabulate(table,headers=headers,tablefmt="fancy_grid"))
        
        except Exception as error_show_dll:
            print("[!] Error in : %s " % (error_show_dll))
    

    def kill_process(self,pid):
        try:
            #psutil.Process(pid).terminate()
            os.kill(pid,signal.SIGTERM)
            return True
        except:
            return False