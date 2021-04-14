package system

import (
	"fmt"
	"image"
	"image/png"
	"io/ioutil"
	"math"
	"os"
	"os/exec"
	"os/user"
	"path/filepath"
	"runtime"
	"strings"

	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/host"
	"github.com/shirou/gopsutil/mem"
)

func System(command string) {
	if runtime.GOOS == "windows" {
		cmd := exec.Command("cmd", "/c", command)
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmd.Run()
	} else {
		cmd := exec.Command("bash", "-c", command)
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmd.Run()
	}
}

func ClearConsole() {
	if runtime.GOOS == "windows" {
		System("cls")
	} else {
		System("clear")
	}
}

func ExecuteProcess(process string) {
	cmd := exec.Command(process)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.Stdin = os.Stdin
	cmd.Run()
}

func Pwd() (string, error) {
	getcwd, err := os.Getwd()
	if err != nil {
		return "", err
	}
	return getcwd, nil
}

func CD(path string) bool {
	_, err := os.Stat(path)

	if os.IsNotExist(err) {
		return false
	}

	os.Chdir(path)
	return true
}

func GetNameInformations() ([]string, error) {
	user, err := user.Current()

	if err != nil {
		return []string{"nil"}, err
	}

	if runtime.GOOS == "windows" {
		split := strings.Split(user.Username, "\\")
		return split, nil
	} else {
		username := string(user.Username)
		return []string{username}, nil
	}
}

func Ls(path string) ([]os.FileInfo, error) {
	files, err := ioutil.ReadDir(path)

	if err != nil {
		return nil, err
	}

	return files, nil
}

func Cat(path string) {
	content, err := ioutil.ReadFile(path)

	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(content))
}

func Mkdir(dir string) error {

	err := os.MkdirAll(dir, os.ModeDir)

	if err == nil || os.IsExist(err) {
		return nil
	} else {
		return err
	}
}

func Rm(file string) error {
	err := os.Remove(file)

	if err != nil {
		return err
	}

	return nil
}

func RmDir(path string) error {
	err := os.RemoveAll(path)

	if err != nil {
		return err
	}

	return nil
}

func Rename(file string, newfile string) error {
	err := os.Rename(file, newfile)
	if err != nil {
		return err
	}

	return nil
}

func Create(file string) error {
	c, err := os.Create(file)
	defer c.Close()

	if err != nil {
		return err
	}

	return nil
}

func WriteFile(file string, data []byte) error {
	_, err := os.Stat(file)

	if os.IsNotExist(err) {
		return err
	}

	write := ioutil.WriteFile(file, data, 0644)

	if write != nil {
		return write
	}
	return nil
}

func SaveSreenshot(img *image.RGBA, filename string) {
	file, err := os.Create(filename)

	if err != nil {
		panic(err)
	}

	defer file.Close()
	png.Encode(file, img)
}

type SysInfo struct {
	Hostname string
	Platform string
	CPU      string
	RAM      uint64
	Disk     uint64
}

func GetSystemInfo() {
	hostStat, _ := host.Info()
	cpuStat, _ := cpu.Info()
	vmStat, _ := mem.VirtualMemory()
	diskStat, _ := disk.Usage("\\") // If you're in Unix change this "\\" for "/"
	//diskStatLinux, _ := disk.Usage("/")

	info := new(SysInfo)

	info.Hostname = hostStat.Hostname
	info.Platform = hostStat.Platform
	info.RAM = vmStat.Total / 1024 / 1024
	info.Disk = diskStat.Total / 1024 / 1024

	fmt.Println("[+] OS :", hostStat.OS)
	fmt.Println("[+] Platform :", hostStat.Platform)
	fmt.Println("[+] Platform Version :", hostStat.PlatformVersion)
	fmt.Println("[+] Platform Family :", hostStat.PlatformFamily)
	fmt.Println("[+] Hostname : ", hostStat.Hostname)

	if len(cpuStat) >= 1 {
		for _, ii := range cpuStat {
			fmt.Println("[+] CPU Vendor ID :", ii.VendorID)
			fmt.Println("[+] CPU Family :", ii.Family)
			fmt.Println("[+] CPU Model :", ii.Model)
			fmt.Println("[+] CPU Stepping :", ii.Stepping)
			fmt.Println("[+] CPU ModelName :", ii.ModelName)
			fmt.Println("[+] CPU Cores :", ii.Cores)
		}
	} else {
		fmt.Println("[+] CPU Error !")
	}

	fmt.Println("[+] Total Memory (RAM) :", vmStat.Total/1024/1024, " Mo")
	fmt.Printf("[+] Memory Used : %d Mo (%v)\n", vmStat.Used/1024/1024, vmStat.UsedPercent)
	fmt.Println("[+] Disk Space Total :", diskStat.Total/1024/1024, " GB")
	fmt.Printf("[+] Disk Space Used : %d GB (%v)\n", diskStat.Used/1024/1024, math.Round(diskStat.UsedPercent))
}

func Rmr(dir string) error {
	files, err := filepath.Glob(filepath.Join(dir, "*"))
	if err != nil {
		return err
	}
	for _, file := range files {
		err = os.RemoveAll(file)
		if err != nil {
			return err
		}
	}
	return nil
}
