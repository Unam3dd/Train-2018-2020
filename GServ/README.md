# GServ
Get Service By Port Function in Golang for Windows


## Install

go get -v github.com/Unam3dd/GServ/

```go
package main

import (
      "fmt"
      "github.com/Unam3dd/GServ"
)

func main(){
  service, _ := GServ.GetServiceByPort(22)
  fmt.Printf("Port : 22 | Service : %s", service)
}
