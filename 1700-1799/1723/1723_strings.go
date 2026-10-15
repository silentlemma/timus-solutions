package main

import "fmt"

const letters = 26

// every occurrence of a spell starts with an occurrence of its first
// letter, so a most frequent single letter is a strongest spell
func main() {
	var s string
	fmt.Scan(&s)
	var count [letters]int
	best := 0
	for _, c := range s {
		i := int(c - 'a')
		count[i]++
		if count[i] > count[best] {
			best = i
		}
	}
	fmt.Println(string(rune('a' + best)))
}
