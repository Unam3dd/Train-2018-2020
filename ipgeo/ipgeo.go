package ipgeo

// Simple Implementation of ipinfo.io By Unam3dd

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
)

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

func GetLocalAddr() (string, error) {
	conn, err := net.Dial("udp", "8.8.8.8:80")

	if err != nil {
		return "", err
	}

	ip := conn.LocalAddr().String()
	return ip, nil
}

func ShowMyGeoIP() {
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

func ShowGeoIP(target string) {
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

func GetMyGeoIp() ([]string, error) {
	body, err := httpget("http://ipinfo.io/json")

	if err != nil {
		return []string{}, err
	}

	var config IPConfig
	e := json.Unmarshal(body, &config)

	if e != nil {
		return []string{}, e
	}

	c := []string{config.Ip, config.Hostname, config.Region, config.City, config.Country, config.Loc, config.Postal, config.Org, config.Timezone}
	return c, nil
}

func GetGeoIP(target string) ([]string, error) {
	body, err := httpget("http://ipinfo.io/" + target + "/geo")

	if err != nil {
		return []string{}, err
	}

	var config IPConfig
	e := json.Unmarshal(body, &config)

	if e != nil {
		return []string{}, err
	}

	c := []string{config.Ip, config.City, config.Region, config.Country, config.Loc}
	return c, nil
}
