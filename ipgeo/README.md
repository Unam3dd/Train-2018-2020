# ipgeo
Simple package to do IP geolocation

## Install
    go get -v github.com/Unam3dd/ipgeo


## Documentations
```golang
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
```
```golang
package main

//Author : Unam3dd

import (
	"fmt"

	"github.com/Unam3dd/ipgeo"
)

func main() {
	pip, epib := ipgeo.GetPublicIp() // Get Your Public IP

	if epib != nil {
		fmt.Println(epib)
	}

	lip, elip := ipgeo.GetLocalAddr() // Get Your Local Address

	if elip != nil {
		fmt.Println(elip)
	}

	fmt.Println("[+] My Public IP : ", pip)
	fmt.Println("[+] My Local IP : ", lip)

	fmt.Println("[+] Your Location !")
	ipgeo.ShowMyGeoIP() // Show Your Locations by IP

	fmt.Println("[+] Location of ", pip)
	ipgeo.ShowGeoIP(pip) // Show Target Geolocation

	gmy, egip := ipgeo.GetMyGeoIp() // Get Your Location, but return an array of your location

	if egip != nil {
		fmt.Println(egip)
	}

	fmt.Println("Your Ip is : ", gmy[0])
	fmt.Println("Your Hostname is : ", gmy[1])
	fmt.Println("Your City is : ", gmy[2]) // etc...

	// for show all informations from array

	for _, i := range gmy {
		fmt.Println(i)
	}

	gip, eip := ipgeo.GetGeoIP(pip) // return array for location of target IP

	if eip != nil {
		fmt.Println(eip)
	}

	for _, x := range gip {
		fmt.Println(x)
	}

	fmt.Printf("Target Country of %s is %s", pip, gip[3])
}
```
