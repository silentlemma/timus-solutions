package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const choices = 3 // names offered for every problem

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	names := make([][]string, n)
	for i := range names {
		names[i] = make([]string, choices)
		for j := range names[i] {
			fmt.Fscan(reader, &names[i][j])
		}
		sort.Strings(names[i])
	}
	// in the given order, the least name above the previous one leaves the
	// most room for the problems still to come
	var chosen []string
	last := ""
	for i := 0; i < n; i++ {
		var p int
		fmt.Fscan(reader, &p)
		next := ""
		for _, name := range names[p-1] {
			if name > last {
				next = name
				break
			}
		}
		if next == "" {
			fmt.Fprintln(writer, "IMPOSSIBLE")
			return
		}
		last = next
		chosen = append(chosen, last)
	}
	for _, name := range chosen {
		fmt.Fprintln(writer, name)
	}
}
