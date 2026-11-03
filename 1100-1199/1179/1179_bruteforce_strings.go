package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const wall, smallest = 36, 2

func digit(c byte) int {
	if c >= '0' && c <= '9' {
		return int(c - '0')
	}
	if c >= 'A' && c <= 'Z' {
		return int(c-'A') + 10
	}
	return wall
}
func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	best, bestBase := -1, smallest
	for base := smallest; base <= wall; base++ {
		inside, count := false, 0
		for _, c := range text {
			current := digit(c) < base
			if current && !inside {
				count++
			}
			inside = current
		}
		if count > best {
			best, bestBase = count, base
		}
	}
	fmt.Println(bestBase, best)
}
