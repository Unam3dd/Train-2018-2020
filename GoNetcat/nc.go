package main

import (
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"

	"github.com/Unam3dd/nclib"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("usage : %s -h\n", os.Args[0])
		os.Exit(1)
	}

	if os.Args[1] == "-c" {
		if len(os.Args) >= 3 {

			s := make(chan os.Signal)
			signal.Notify(s, os.Interrupt, syscall.SIGTERM)

			go func() {
				<-s
				os.Exit(0)
			}()

			obj, err := nclib.Connect(os.Args[2], "tcp")

			if err != nil {
				log.Println(err)
			}

			log.Println("Connected to ", obj.RemoteAddr())

			go nclib.ProcessClient(obj, os.Stdout)
			go nclib.ProcessClient(os.Stdin, obj)
			for {
			}
		}
	} else if os.Args[1] == "-l" {
		fmt.Println("[+] Listening on ", os.Args[2])
		ln, err := nclib.Listen(os.Args[2], "tcp")

		if err != nil {
			log.Println(err)
		}

		s := make(chan os.Signal)
		signal.Notify(s, os.Interrupt, syscall.SIGTERM)

		go func() {
			<-s
			os.Exit(0)
		}()

		for {
			obj, err := ln.Accept()

			if err != nil {
				log.Println(err)
			}

			log.Println("New connection arrived ", obj.RemoteAddr())

			go nclib.ProcessClient(obj, os.Stdout)
			go nclib.ProcessClient(os.Stdin, obj)
			for {
			}
			break
		}
	} else {
		fmt.Println("[+] Help main :")
		fmt.Println("-l - Listen Connection")
		fmt.Println("-c - Connect to Host")
		fmt.Printf("usage : %s -l 127.0.0.1:5555\n", os.Args[0])
		fmt.Printf("usage : %s -c 127.0.0.1:5555\n", os.Args[0])
	}

}
