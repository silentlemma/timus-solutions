package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	// a word is a run of letters; anything else ends it
	words := strings.FieldsFunc(string(text), func(r rune) bool { return r < 'a' || r > 'z' })
	trams, trolleys := 0, 0
	for _, w := range words {
		if w == "tram" {
			trams++
		} else if w == "trolleybus" {
			trolleys++
		}
	}
	switch {
	case trams > trolleys:
		fmt.Println("Tram driver")
	case trolleys > trams:
		fmt.Println("Trolleybus driver")
	default:
		fmt.Println("Bus driver")
	}
}
