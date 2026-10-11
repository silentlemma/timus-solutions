package main

import (
	"io/ioutil"
	"os"
)

func letter(c byte) bool { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') }

func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	// every run of Latin letters is reversed in place; everything else stays
	for i := 0; i < len(text); i++ {
		j := i
		for j < len(text) && letter(text[j]) {
			j++
		}
		for a, b := i, j-1; a < b; a, b = a+1, b-1 {
			text[a], text[b] = text[b], text[a]
		}
		if j > i {
			i = j
		}
	}
	os.Stdout.Write(text)
}
