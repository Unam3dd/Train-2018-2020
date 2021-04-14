package GServ

import (
	"bufio"
	"fmt"
	"os"
	"os/user"
	"strconv"
	"strings"
)

type GetServPortError struct{}

func (g *GetServPortError) Error() string {
	return "error the port is not associated with any services in the mapping"
}

func check_file(filename string) bool {
	_, err := os.Stat(filename)

	if os.IsNotExist(err) {
		return false
	}

	return true
}

func GetServiceByPort(port int) (string, error) {
	var Maps = make([]string, 1)
	var return_string = make([]string, 1)
	user, err := user.Current()

	if err != nil {
		fmt.Println(err)
	}
	split := strings.Split(user.Username, "\\")
	vv := fmt.Sprintf("C:\\users\\%s\\go\\src\\github.com\\Unam3dd\\GServ\\service_port.txt", split[1])
	if check_file(vv) == false {
		return "[+] File Not Found !", &GetServPortError{}
	}

	file, err := os.Open(vv)

	if err != nil {
		return "error", err
	}

	defer file.Close()

	read := bufio.NewScanner(file)

	for read.Scan() {
		Maps = append(Maps, read.Text())
	}

	ps := strconv.Itoa(port)
	for i := 0; i < len(Maps); i++ {
		str := Maps[i]
		s := strings.Split(str, "|")

		if ps == s[0] {
			return_string[0] = s[1]
			break
		}

		return_string[0] = "0"
	}

	if return_string[0] == "0" {
		return return_string[0], &GetServPortError{}
	}

	return return_string[0], nil
}
