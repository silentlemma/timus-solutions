package main

import (
	"bufio"
	"fmt"
	"os"
)

type reading struct {
	displayed int
	entered   int
}

func requiredInput(current int, history []reading) int {
	answer := current - 2
	for _, entry := range history {
		answer += entry.displayed - entry.entered - 2
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count, current int
	fmt.Fscan(input, &count, &current)
	history := make([]reading, count)
	for index := range history {
		fmt.Fscan(input, &history[index].displayed, &history[index].entered)
	}
	answer := requiredInput(current, history)
	if answer >= 0 {
		fmt.Println(answer)
	} else {
		fmt.Println("Big Bang!")
	}
}
