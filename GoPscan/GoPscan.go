package main

import (
	"flag"
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/Unam3dd/GServ"
)

var banner string = " ██████╗  ██████╗ ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗\n██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║\n██║  ███╗██║   ██║██████╔╝███████╗██║     ███████║██╔██╗ ██║\n██║   ██║██║   ██║██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║\n╚██████╔╝╚██████╔╝██║     ███████║╚██████╗██║  ██║██║ ╚████║\n ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝\n"

func tcp_connect_port(host string, port int) int {
	a := fmt.Sprintf("%s:%d", host, port)
	_, err := net.Dial("tcp", a)

	if err != nil {
		return 0
	} else {
		return port
	}
}

func usage() {
	fmt.Fprintf(os.Stderr, "\033[38;5;87musage : %s <\033[38;5;82mip\033[38;5;87m> <\033[38;5;82m0-range\033[38;5;87m> <\033[38;5;82mms\033[38;5;87m>\033[00m\n", os.Args[0])
	flag.PrintDefaults()
	os.Exit(-1)
}

func main() {
	fmt.Println("\033[38;5;87m" + banner + "\033[00m")
	flag.Usage = usage
	flag.Parse()
	allArgs := flag.Args()

	if len(allArgs) < 3 {
		flag.Usage()
		os.Exit(-1)
	}

	var wg sync.WaitGroup
	t := time.Now()
	host := os.Args[1]
	timeNow := fmt.Sprintf("%d:%d:%d", t.Hour(), t.Minute(), t.Second())
	fmt.Printf("\033[38;5;87m[\033[38;5;82m%s\033[38;5;87m] \033[00mScanner Started !\n", timeNow)
	RangePort, _ := strconv.Atoi(os.Args[2])
	timeduration := os.Args[3] + "ms"
	tt := strings.Split(timeduration, "ms")
	tos, _ := strconv.Atoi(tt[0])
	fmt.Printf("\033[38;5;87m[\033[38;5;82m%s\033[38;5;87m] \033[00mTarget : \033[38;5;82m%s\033[38;5;87m  | Range : 0-%d | ms : %d\033[00m\n", timeNow, host, RangePort, tos)
	fmt.Printf("\033[38;5;87mPORT    SERVICES     TIME\n")
	fmt.Printf("\033[38;5;87m==========================\033[00m\n")
	for i := 0; i < RangePort; i++ {
		wg.Add(1)
		go func() {
			x := tcp_connect_port(host, i)
			service, _ := GServ.GetServiceByPort(i)

			t := time.Now()
			timeNow := fmt.Sprintf("%d:%d:%d", t.Hour(), t.Minute(), t.Second())
			if x != 0 {
				fmt.Printf("\033[38;5;87mtcp/%d \033[38;5;82m  %s\033[38;5;87m  %s\033[00m\n", i, service, timeNow)
			}
			wg.Done()
		}()
		time.Sleep(time.Duration(tos) * time.Millisecond)
	}
	timeNowFinished := fmt.Sprintf("%d:%d:%d", t.Hour(), t.Minute(), t.Second())
	fmt.Printf("\033[38;5;87m[\033[38;5;82m%s\033[38;5;87m] Scanner Finished !\033[00m\n", timeNowFinished)
}
