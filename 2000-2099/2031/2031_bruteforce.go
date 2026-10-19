package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const base = 10
const limit = base*base - 1
const turn = "01????9?86"

func solve(count int) string {
	run := 0
	for value := 1; value <= limit; value++ {
		if turn[value/base] != '?' && turn[value%base] != '?' {
			run++
		} else {
			run = 0
		}
		if run >= count {
			var answer strings.Builder
			for target := value; target > value-count; target-- {
				if answer.Len() != 0 {
					answer.WriteByte(' ')
				}
				answer.WriteByte(turn[target%base])
				answer.WriteByte(turn[target/base])
			}
			return answer.String()
		}
	}
	return "Glupenky Pierre"
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var count int
	if _, err := fmt.Fscan(reader, &count); err == nil {
		fmt.Println(solve(count))
	}
}
