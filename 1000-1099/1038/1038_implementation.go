package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	errors := 0
	// a new sentence waits for its first letter; inWord: the previous character
	// was a letter
	newSentence, inWord := true, false
	for _, c := range text {
		lower := c >= 'a' && c <= 'z'
		upper := c >= 'A' && c <= 'Z'
		if lower || upper {
			if lower && newSentence {
				errors++
			}
			if upper && inWord {
				errors++
			}
			newSentence, inWord = false, true
		} else {
			inWord = false
			if c == '.' || c == '?' || c == '!' {
				newSentence = true
			}
		}
	}
	fmt.Println(errors)
}
