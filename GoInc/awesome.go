// command : go build -o awesome.lib -buildmode=c-shared .\awesome.go
package main

import "C"
import (
	"fmt"
	"os"
	"os/exec"
)

//export PopShell
func PopShell() {
	cmd := exec.Command("cmd.exe")
	cmd.Stderr = os.Stderr
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Run()
}

//export Add
func Add(a int, b int) int {
	return a + b
}

//export Say
func Say(message string) {
	fmt.Println(message)
}

func main() {}
