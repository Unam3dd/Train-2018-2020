# futhark
Latin to Elder Futhark Runes

## Exemple Usage :
```golang
package main

import (
	"fmt"

	"github.com/Unam3dd/futhark"
)

func main() {
	f := fmt.Sprintf("%s", futhark.TranslateToRunes("hello"))
	fmt.Println(f)
	L := fmt.Sprintf("%s", futhark.TranslateToLatin(f))
	fmt.Println(L)
	fmt.Println(futhark.AsciiToInt('a'))
	fmt.Println(futhark.IntToAscii(97))
}
```
