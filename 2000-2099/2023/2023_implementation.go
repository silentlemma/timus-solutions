package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func solve(names []string) int {
	position, steps := 0, 0
	for _, name := range names {
		target := 2
		if strings.ContainsRune("APOR", rune(name[0])) {
			target = 0
		} else if strings.ContainsRune("BMS", rune(name[0])) {
			target = 1
		}
		difference := target - position
		if difference < 0 {
			difference = -difference
		}
		steps += difference
		position = target
	}
	return steps
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var count int
	if _, err := fmt.Fscan(in, &count); err != nil {
		return
	}
	names := make([]string, count)
	for index := range names {
		fmt.Fscan(in, &names[index])
	}
	fmt.Println(solve(names))
}
