package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	// the line has at most 10^5 pieces of each length, fewer than the
	// 9 * 10^5 numbers of six digits, so the answer has at most six digits
	digits = 6
	limit  = 1000000
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var s string
	if _, err := fmt.Fscan(reader, &s); err != nil {
		return
	}
	seen := make([]bool, limit+1)
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			continue
		}
		value := 0
		for j := i; j < len(s) && j < i+digits; j++ {
			value = value*10 + int(s[j]-'0')
			seen[value] = true
		}
	}
	answer := 1
	for seen[answer] {
		answer++
	}
	fmt.Println(answer)
}
