package main

import (
	"io/ioutil"
	"os"
	"strings"
)

const ends = ".!?" // marks that end a sentence

func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	start := true // the next letter opens a sentence
	for i, c := range text {
		if c >= 'A' && c <= 'Z' {
			if !start {
				text[i] = c + 'a' - 'A'
			}
			start = false
		} else if strings.IndexByte(ends, c) >= 0 {
			start = true
		}
	}
	os.Stdout.Write(text)
}
