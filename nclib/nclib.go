package nclib

import (
	"crypto/tls"
	"fmt"
	"io"
	"net"
	"os/exec"
	"syscall"
	"time"
)

var (
	MAXCON    int = 0 // if MAXCON is not set, by defaults MAXCON value is 100
	ConID         = make([]net.Conn, MAXCON)
	ErrID         = make([]error, MAXCON)
	ConAlives     = len(ConID)
)

type Client struct {
	ConnectionID net.Conn
}

type TLSClient struct {
	ConnectionID tls.Conn
}

func (s *Client) Send(data string) (int, error) {
	ok, err := s.ConnectionID.Write([]byte(data))

	if err != nil {
		return 0, err
	}

	return ok, nil
}

func Connect(host string, protocol string) (net.Conn, error) {
	c, err := net.Dial(protocol, host)

	if err != nil {
		return nil, err
	}

	return c, nil
}

func StreamProcess(c net.Conn, process string) error {
	cmd := exec.Command(process)

	cmd.Stdout = c
	cmd.Stderr = c
	cmd.Stdin = c
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}

	e := cmd.Run()

	if e != nil {
		return e
	}

	return nil
}

func ConnectTimeout(host string, protocol string, timeout int) (net.Conn, error) {
	c, err := net.DialTimeout(protocol, host, time.Duration(timeout)*time.Millisecond)

	if err != nil {
		return nil, err
	}

	return c, nil
}

func ConnectTls(address string, port string, protocol string) (*tls.Conn, error) {
	host := net.JoinHostPort(address, port)

	conf := &tls.Config{
		InsecureSkipVerify: true,
	}

	c, err := tls.Dial(protocol, host, conf)

	if err != nil {
		return nil, err
	}

	return c, nil
}

func Listen(address string, protocol string) (net.Listener, error) {
	ln, err := net.Listen(protocol, address)

	if err != nil {
		return nil, err
	}

	return ln, nil
}

func ListenTls(address string, protocol string) (net.Listener, error) {
	conf := &tls.Config{InsecureSkipVerify: true}
	ln, err := tls.Listen(protocol, address, conf)

	if err != nil {
		return nil, err
	}

	return ln, nil
}

func Accept(a net.Listener) (net.Conn, error) {
	conn, err := a.Accept()

	if err != nil {
		return nil, err
	}

	return conn, nil
}

func (s *TLSClient) TLSSend(data string) (int, error) {
	ok, err := s.ConnectionID.Write([]byte(data))

	if err != nil {
		return 0, err
	}

	return ok, nil
}

func (s *TLSClient) TLSSendTimeout(data string, timeout int) (int, error) {
	t := time.Duration(timeout)
	t = (t * time.Second)
	ok, err := s.ConnectionID.Write([]byte(data))
	time.Sleep(t)

	if err != nil {
		return 0, err
	}

	return ok, nil
}

func (s *TLSClient) TLSRecv(NumberBytes int) (string, error) {
	buffer := make([]byte, NumberBytes)
	r, err := s.ConnectionID.Read(buffer)

	if err != nil {
		return "", err
	}

	if r <= 0 {
		return "", nil
	}

	return string(buffer), nil
}

func (s *TLSClient) TLSRecvTimeout(NumberBytes int, timeout int) (string, error) {
	buffer := make([]byte, NumberBytes)
	d := time.Duration(timeout)
	time.Sleep(d * time.Second)
	r, err := s.ConnectionID.Read(buffer)

	if err != nil {
		return "", err
	}

	if r <= 0 {
		return "", nil
	}

	return string(buffer), nil
}

func (s *Client) SendTimeout(data string, timeout int) (int, error) {
	t := time.Duration(timeout)
	t = (t * time.Second)
	ok, err := s.ConnectionID.Write([]byte(data))
	time.Sleep(t)

	if err != nil {
		return 0, err
	}

	return ok, nil
}

func (s *Client) SendDeadline(data string, deadline int) (int, error) {
	d := time.Duration(deadline)
	s.ConnectionID.SetDeadline(time.Now().Add(d))
	ok, err := s.ConnectionID.Write([]byte(data))

	if err != nil {
		return 0, err
	}

	return ok, nil
}

func (s *Client) Recv(NumberBytes int) (string, error) {
	buffer := make([]byte, NumberBytes)
	r, err := s.ConnectionID.Read(buffer)

	if err != nil {
		return "", err
	}

	if r <= 0 {
		return "", nil
	}

	return string(buffer), nil
}

func (s *Client) RecvTimeout(NumberBytes int, timeout int) (string, error) {
	buffer := make([]byte, NumberBytes)
	d := time.Duration(timeout)
	time.Sleep(d * time.Second)
	r, err := s.ConnectionID.Read(buffer)

	if err != nil {
		return "", err
	}

	if r <= 0 {
		return "", nil
	}

	return string(buffer), nil
}

func (s *Client) RecvDeadline(NumberBytes int, deadline int) (string, error) {
	buffer := make([]byte, NumberBytes)
	d := time.Duration(deadline)
	s.ConnectionID.SetReadDeadline(time.Now().Add(d * time.Second))
	r, err := s.ConnectionID.Read(buffer)

	if err != nil {
		return "", err
	}

	if r <= 0 {
		return "", nil
	}

	return string(buffer), nil
}

func ListenMultiClient(ip string, protocol string, MaxCon bool) error {

	if MaxCon != false {

		if MAXCON == 0 {
			MAXCON = 100
		}

		c, err := net.Listen(protocol, ip)

		if err != nil {
			return err
		}

		for {
			conid, e := c.Accept()

			if e != nil {
				ErrID = append(ErrID, e)
			}

			if len(ConID) != MAXCON {
				ConID = append(ConID, conid)
				//fmt.Println("[+] New Connections : ", conid.RemoteAddr())
			} else {
				conid.Close()
			}
		}
	} else {
		c, err := net.Listen(protocol, ip)

		if err != nil {
			fmt.Println(err)
		}

		for {
			conid, e := c.Accept()

			if e != nil {
				ErrID = append(ErrID, e)
			}

			ConID = append(ConID, conid)
		}
	}

	return nil
}

func TLSListenMultiClient(ip string, protocol string, MaxCon bool) error {

	if MaxCon != false {

		if MAXCON == 0 {
			MAXCON = 100
		}

		conf := &tls.Config{InsecureSkipVerify: true}
		c, err := tls.Listen(protocol, ip, conf)

		if err != nil {
			return err
		}

		for {
			conid, e := c.Accept()

			if e != nil {
				ErrID = append(ErrID, e)
			}

			if len(ConID) != MAXCON {
				ConID = append(ConID, conid)
				//fmt.Println("[+] New Connections : ", conid.RemoteAddr())
			} else {
				conid.Close()
			}
		}
	} else {
		c, err := net.Listen(protocol, ip)

		if err != nil {
			fmt.Println(err)
		}

		for {
			conid, e := c.Accept()

			if e != nil {
				ErrID = append(ErrID, e)
			}

			ConID = append(ConID, conid)
		}
	}

	return nil
}

func ProcessClient(sstream io.Reader, dstream io.Writer) {
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
