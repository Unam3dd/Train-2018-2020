package displaynetwork

import (
	"context"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"net"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/Unam3dd/GServ"
	googlesearch "github.com/rocketlaunchr/google-search"
)

func GetPublicIp() (string, error) {
	resp, err := http.Get("https://ifconfig.me/ip")
	if err != nil {
		return "", err
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(body), nil
}

func HttpGet(link string) (string, error) {
	resp, err := http.Get(link)
	if err != nil {
		return "", err
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(body), nil
}

type HttpQ struct {
	StatusCode int
	Pmajor     int
	Pminor     int
	Status     string
	Useragent  string
	Body       string
	Host       string
	Proto      string
	Method     string
	RemoteAddr string
	Response   *http.Response
	Er         error
}

func HttpCurlGET(link string) HttpQ {
	resp, err := http.Get(link)

	if err != nil {
		e := HttpQ{
			Er: err,
		}
		return e
	}

	b, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		e := HttpQ{
			Er: err,
		}
		return e
	}

	s := HttpQ{
		StatusCode: resp.StatusCode,
		Pmajor:     resp.ProtoMajor,
		Pminor:     resp.ProtoMinor,
		Status:     resp.Status,
		Body:       string(b),
		Host:       resp.Request.Host,
		Proto:      resp.Proto,
		Method:     resp.Request.Method,
		RemoteAddr: resp.Request.RemoteAddr,
		Response:   resp.Request.Response,
		Er:         nil,
	}
	return s
}

func httpget(link string) ([]byte, error) {
	resp, err := http.Get(link)
	if err != nil {
		return nil, err
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	return body, nil
}

func GetLocalAddr() (string, error) {
	conn, err := net.Dial("udp", "8.8.8.8:80")

	if err != nil {
		return "", err
	}

	ip := conn.LocalAddr().String()
	return ip, nil
}

type IPConfig struct {
	Ip       string
	Hostname string
	City     string
	Region   string
	Country  string
	Loc      string
	Org      string
	Postal   string
	Timezone string
}

func GeoIP() {
	body, err := httpget("http://ipinfo.io/json")

	if err != nil {
		fmt.Println(err)
	}

	var config IPConfig
	e := json.Unmarshal(body, &config)

	if e != nil {
		fmt.Println(e)
	}

	fmt.Println("[+] IP :", config.Ip)
	fmt.Println("[+] Hostname :", config.Hostname)
	fmt.Println("[+] City :", config.City)
	fmt.Println("[+] Region :", config.Region)
	fmt.Println("[+] Country :", config.Country)
	fmt.Println("[+] Location :", config.Loc)
	fmt.Println("[+] Org :", config.Postal)
	fmt.Println("[+] Timezone :", config.Timezone)

}

func GetGeoIP(target string) {
	body, err := httpget("http://ipinfo.io/" + target + "/geo")

	if err != nil {
		fmt.Println(err)
	}

	var config IPConfig
	e := json.Unmarshal(body, &config)

	if e != nil {
		fmt.Println(e)
	}

	fmt.Println("[+] IP :", config.Ip)
	fmt.Println("[+] City :", config.City)
	fmt.Println("[+] Region :", config.Region)
	fmt.Println("[+] Country :", config.Country)
	fmt.Println("[+] Location :", config.Loc)
	fmt.Println("[+] Timezone :", config.Timezone)
}

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

func Googlesearch(search string, country string, lang string) {
	Banner := "0a202020202020202020202020201b5b313b39366d20645022226238201b5b313b39316d20645022596220201b5b313b39336d20645022596220201b5b313b39366d20645022226238201b5b313b39326d383820202020201b5b313b39316d3838383838381b5b30306d0a202020202020202020202020201b5b313b39366d64502020206022201b5b313b39316d64502020205962201b5b313b39336d64502020205962201b5b313b39366d64502020206022201b5b313b39326d383820202020201b5b313b39316d38385f5f1b5b30306d0a202020202020202020202020201b5b313b39366d59622020223838201b5b313b39316d59622020206450201b5b313b39336d59622020206450201b5b313b39366d59622020223838201b5b313b39326d383820202e6f201b5b313b39316d383822221b5b30306d0a202020202020202020202020201b5b313b39366d2059626f6f6450201b5b313b39316d2059626f645020201b5b313b39336d2059626f645020201b5b313b39366d2059626f6f6450201b5b313b39326d38386f6f6438201b5b313b39316d3838383838381b5b30306d0a"
	decoded, err := hex.DecodeString(Banner)

	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("%s\n", decoded)
	ctx := context.Background()
	options := googlesearch.SearchOptions{
		CountryCode:  country,
		LanguageCode: lang,
	}
	goo, _ := googlesearch.Search(ctx, search, options)

	for _, ss := range goo {
		t := time.Now()
		tt := fmt.Sprintf("%02d:%02d:%02d", t.Hour(), t.Minute(), t.Second())
		fmt.Printf("[\033[1;96m%s\033[00m] URL : \033[38;5;82m%s\033[00m\n[\033[1;96m%s\033[00m] Title : \033[38;5;82m%s\033[00m\n[\033[1;96m%s\033[00m] Description : \033[38;5;82m%s\033[00m\n[\033[1;96m%s\033[00m] Rank : \033[38;5;82m%d\033[00m\n\n", tt, ss.URL, tt, ss.Title, tt, ss.Description, tt, ss.Rank)
	}
}

func tcp_connect_port(host string, port int) int {
	a := fmt.Sprintf("%s:%d", host, port)
	_, err := net.Dial("tcp", a)

	if err != nil {
		return 0
	} else {
		return port
	}
}

func CheckPortConnect(host string, port int) int {
	a := fmt.Sprintf("%s:%d", host, port)
	_, err := net.Dial("tcp", a)

	if err != nil {
		return 0
	} else {
		return port
	}
}

func Lhost(host string) ([]string, error) {
	addrs, err := net.LookupHost(host)

	if err != nil {
		return []string{}, err
	}

	a := []string{}

	for _, i := range addrs {
		a = append(a, i)
	}
	//s := strings.Join(addr, "")
	return a, nil
}

func Laddr(addr string) ([]string, error) {
	hst, err := net.LookupNS(addr)

	if err != nil {
		return []string{}, err
	}

	a := []string{}

	for _, i := range hst {
		a = append(a, i.Host)
	}

	return a, nil
}

func PortScanner(host string, r string, ms string) {
	var wg sync.WaitGroup
	t := time.Now()
	RangePort, _ := strconv.Atoi(r)
	timeNow := fmt.Sprintf("%02d:%02d:%02d", t.Hour(), t.Minute(), t.Second())
	fmt.Printf("\033[38;5;87m[\033[38;5;82m%s\033[38;5;87m] \033[00mScanner Started !\n", timeNow)
	timeduration := ms + "ms"
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
			timeNow := fmt.Sprintf("%02d:%02d:%02d", t.Hour(), t.Minute(), t.Second())
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
