package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	// a team that submitted more than once is the spammer; the teams are
	// printed in the order of their first submission
	count := map[string]int{}
	var order []string
	for i := 0; i < n; i++ {
		var team string
		fmt.Fscan(reader, &team)
		if count[team] == 0 {
			order = append(order, team)
		}
		count[team]++
	}
	for _, team := range order {
		if count[team] > 1 {
			fmt.Fprintln(writer, team)
		}
	}
}
