package main

import (
	"fmt"
	"unicode"
)

const (
	name  = "Sandro"
	coins = 5
)

func main() {
	var text string
	if _, err := fmt.Scan(&text); err != nil {
		return
	}
	best := -1
	for start := 0; start+len(name) <= len(text); start++ {
		cost := 0
		for k := 0; k < len(name); k++ {
			a, b := rune(text[start+k]), rune(name[k])
			// one fee for the wrong case, one for the wrong letter
			if unicode.IsUpper(a) != unicode.IsUpper(b) {
				cost += coins
			}
			if unicode.ToLower(a) != unicode.ToLower(b) {
				cost += coins
			}
		}
		if best < 0 || cost < best {
			best = cost
		}
	}
	fmt.Println(best)
}
