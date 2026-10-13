package main

import "fmt"

const shift = 5 // added to the first letter
const letters = 26

func main() {
	var word string
	fmt.Scan(&word)
	// each code is the previous code plus the letter, modulo 26: take differences
	prev, plain := shift, make([]byte, len(word))
	for i := 0; i < len(word); i++ {
		code := int(word[i] - 'a')
		plain[i] = byte('a' + ((code-prev)%letters+letters)%letters)
		prev = code
	}
	fmt.Println(string(plain))
}
