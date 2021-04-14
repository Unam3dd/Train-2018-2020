package futhark

import (
	"fmt"
	"strconv"
	"strings"
)

type RunesCipher struct {
	RawRunes string
}

var latin = []string{"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g",
	"h",
	"i",
	"j",
	"k",
	"l",
	"m",
	"n",
	"o",
	"p",
	"q",
	"r",
	"s",
	"t",
	"u",
	"v",
	"w",
	"x",
	"y",
	"z",
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
}

var latinA = []string{"A",
	"B",
	"C",
	"D",
	"E",
	"F",
	"G",
	"H",
	"I",
	"J",
	"K",
	"L",
	"M",
	"N",
	"O",
	"P",
	"Q",
	"R",
	"S",
	"T",
	"U",
	"V",
	"W",
	"X",
	"Y",
	"Z",
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
}

var runes = []string{"\u16a8",
	"\u16d2",
	"c",
	"\u16de",
	"\u16d6",
	"\u16a0",
	"\u16b7",
	"\u16ba",
	"\u16c1",
	"\u16c3",
	"\u16b2",
	"\u16da",
	"\u16d7",
	"\u16be",
	"\u16df",
	"\u16c8",
	"q",
	"\u16b1",
	"\u16ca",
	"\u16cf",
	"\u16a2",
	"v",
	"\u16b9",
	"x",
	"y",
	"\u16c9",
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
}

func ShowUnicode(lstr string) string {
	return fmt.Sprintf("%+q\n", lstr)
}

func ShowAllUnicode() {
	for i := 0; i < len(runes); i++ {
		fmt.Println(ShowUnicode(runes[i]))
	}
}

func TranslateToRunes(lstr string) string {
	var ss string = lstr
	for i := 0; i < len(runes); i++ {
		s := strings.ReplaceAll(ss, latin[i], runes[i])
		d := strings.ReplaceAll(s, latinA[i], runes[i])
		ss = d
	}
	return ss
}

func TranslateToLatin(futhark string) string {
	var ss string = futhark
	for i := 0; i < len(runes); i++ {
		s := strings.ReplaceAll(ss, runes[i], latin[i])
		d := strings.ReplaceAll(s, runes[i], latinA[i])
		ss = d
	}
	return ss
}

func AsciiToInt(a byte) int {
	ascii := int(a)
	d := fmt.Sprintf("%d", ascii)
	i, _ := strconv.Atoi(d)
	return i
}

func IntToAscii(a int8) string {
	return fmt.Sprintf("%c", a)
}
