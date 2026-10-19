package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	champion = "Isenbaev"
	team     = 3
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var teams int
	if _, err := fmt.Fscan(in, &teams); err != nil {
		return
	}
	mates := map[string][]string{}
	for t := 0; t < teams; t++ {
		names := make([]string, team)
		for i := range names {
			fmt.Fscan(in, &names[i])
		}
		for _, name := range names {
			mates[name] = append(mates[name], names...)
		}
	}
	// breadth-first search from the champion over shared teams
	number := map[string]int{}
	if _, ok := mates[champion]; ok {
		number[champion] = 0
		queue := []string{champion}
		for len(queue) > 0 {
			name := queue[0]
			queue = queue[1:]
			for _, mate := range mates[name] {
				if _, seen := number[mate]; !seen {
					number[mate] = number[name] + 1
					queue = append(queue, mate)
				}
			}
		}
	}
	names := make([]string, 0, len(mates))
	for name := range mates {
		names = append(names, name)
	}
	sort.Strings(names)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, name := range names {
		if v, ok := number[name]; ok {
			fmt.Fprintln(out, name, v)
		} else {
			fmt.Fprintln(out, name, "undefined")
		}
	}
}
