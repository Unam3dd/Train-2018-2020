# infom
Simple package in golang for display message (Success,Error,Info,Warning)

## Install :
  go get -v github.com/Unam3dd/infom

```golang
package main

import "github.com/Unam3dd/infom"

func main(){
  infom.Success("test")
  infom.TimeSuccess("test")
  infom.InfoSuccess("test")
  infom.BasicSuccess("test")
  infom.Error("test")
  infom.TimeError("test")
  infom.InfoError("test")
  infom.BasicError("test")
  infom.Info("test")
  infom.TimeInfo("test")
  infom.InfoInfo("test")
  infom.Warning("test")
}
