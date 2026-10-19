package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(state string) int64 {
	const pegSum = 3
	source := 0
	answer := int64(0)
	for disk := len(state) - 1; disk >= 0; disk-- {
		target := int(state[disk] - 'A')
		if target != source {
			answer += int64(1) << uint(disk)
			source = pegSum - source - target
		}
	}
	return answer
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var count int
	var state string
	if _, err := fmt.Fscan(in, &count, &state); err != nil {
		return
	}
	fmt.Println(solve(state))
}
