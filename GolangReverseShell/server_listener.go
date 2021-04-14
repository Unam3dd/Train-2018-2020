package main

import (
	"flag"
	"fmt"
	"io"
	"net"
	"os"
)

var banner string = "  _______                             \n |   _   .-----.----.--.--.-----.----.\n |   1___|  -__|   _|  |  |  -__|   _|\n |____   |_____|__|  \\___/|_____|__|  \n |:  1   |                            \n |::.. . |                            \n `-------'                            \n\t\tGithub : Unam3dd\n\t\tusage : server_listener <host> <port>\n"

func RunServer(host string) {
	listener, err := net.Listen("tcp", host)

	if err != nil {
		fmt.Printf("[-] Error : ", err)
	}

	fmt.Println("[+] Listening on ", listener.Addr())

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("[+] Client not Accepted ! : ", err)
		} else {
			fmt.Println("[+] New Client Connected => ", conn.RemoteAddr())
			go processClient(conn, os.Stdout) // Go Routine processClient
			go processClient(os.Stdin, conn)  // Go Routine processClient
		}
	}
}

func processClient(sstream io.Reader, dstream io.Writer) {
	buffer := make([]byte, 1024) // make Slices of 1024 Bytes (Slices == vector in C++)
	for {
		var NumberBytes int
		var err error
		NumberBytes, err = sstream.Read(buffer)
		if err != nil {
			if err != io.EOF {
				fmt.Printf("[+] Read error : %s\n", err)
			}
			break
		}

		_, err = dstream.Write(buffer[0:NumberBytes]) // _ for not get value
		if err != nil {
			fmt.Printf("[+] Write Error : %s\n", err)
		}
	}
}

func main() {
	fmt.Println(banner)
	flag.Parse()
	if len(flag.Args()) < 2 {
		fmt.Println("usage : server_listener <host> <port>")
		return
	}

	sh := flag.Arg(0)
	sp := flag.Arg(1)
	address_listening := fmt.Sprintf("%s:%s", sh, sp)
	RunServer(address_listening)
}
