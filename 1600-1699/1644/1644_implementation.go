package main

import (
	"bufio"
	"fmt"
	"os"
)

const knownHungry, knownFull = 2, 10 // given in the statement

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	hungry, full := knownHungry, knownFull
	for i := 0; i < n; i++ {
		var count int
		var verdict string
		fmt.Fscan(in, &count, &verdict)
		if verdict == "hungry" {
			if count > hungry {
				hungry = count
			}
		} else if count < full {
			full = count
		}
	}
	// the smallest satisfying amount must exceed the largest hungry one
	if full > hungry {
		fmt.Println(full)
	} else {
		fmt.Println("Inconsistent")
	}
}
