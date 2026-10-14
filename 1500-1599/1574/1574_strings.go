package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var line string
	fmt.Fscan(bufio.NewReader(os.Stdin), &line)
	// the balance after each prefix; a shift that starts right after a prefix
	// of the lowest balance never goes below zero, any other shift does
	balance, lowest, count := 0, 0, 0
	for i, c := range line {
		if c == '(' {
			balance++
		} else {
			balance--
		}
		if i == 0 || balance < lowest {
			lowest, count = balance, 1
		} else if balance == lowest {
			count++
		}
	}
	if balance != 0 {
		count = 0
	}
	fmt.Println(count)
}
