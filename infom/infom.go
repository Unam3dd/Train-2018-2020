package infom

import (
	"fmt"
	"time"
)

func Success(message string) {
	fmt.Println("[\033[38;5;82m\u2713\033[00m]", message)
}

func TimeSuccess(message string) {
	t := time.Now()
	timeNow := fmt.Sprintf("%d:%d:%d", t.Hour(), t.Minute(), t.Second())
	fmt.Println("[\033[38;5;82m", timeNow, "\033[00m]", message)
}

func InfoSuccess(message string) {
	fmt.Println("[\033[38;5;82mSUCCESS\033[00m]", message)
}

func BasicSuccess(message string) {
	fmt.Println("[\033[38;5;82m+\033[00m]", message)
}

func Error(message string) {
	fmt.Println("[\033[38;5;196mX\033[00m]", message)
}

func TimeError(message string) {
	t := time.Now()
	timeNow := fmt.Sprintf("%d:%d:%d", t.Hour(), t.Minute(), t.Second())
	fmt.Println("[\033[38;5;196m", timeNow, "\033[00m]", message)
}

func InfoError(message string) {
	fmt.Println("[\033[38;5;196mERROR\033[00m]", message)
}

func BasicError(message string) {
	fmt.Println("[\033[38;5;196mx\033[00m]", message)
}

func Info(message string) {
	fmt.Println("[\033[1;94mi\033[00m]", message)
}

func TimeInfo(message string) {
	t := time.Now()
	timeNow := fmt.Sprintf("%d:%d:%d", t.Hour(), t.Minute(), t.Second())
	fmt.Println("[\033[1;94m", timeNow, "\033[00m]", message)
}

func InfoInfo(message string) {
	fmt.Println("[\033[1:94mINFO\033[00m]", message)
}

func Warning(message string) {
	fmt.Println("[\033[38;5;214mWARNING\033[00m", message)
}
