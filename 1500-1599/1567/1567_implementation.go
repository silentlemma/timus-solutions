package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// keys holds the characters of each key in the order of presses; the space
// has a key of its own
var keys = []string{"abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", ".,!", " "}

func main() {
	// the whole first line, spaces included; anything else costs nothing
	line, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	total := 0
	for _, c := range line {
		for _, key := range keys {
			if at := strings.IndexRune(key, c); at >= 0 {
				total += at + 1
			}
		}
	}
	fmt.Println(total)
}
