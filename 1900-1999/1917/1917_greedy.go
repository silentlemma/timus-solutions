package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func safeRemovals(values []int, budget int64) (int, int) {
	sort.Ints(values)
	removed, spells, active := 0, 0, 0
	for start := 0; start < len(values); {
		end := start + 1
		for end < len(values) && values[end] == values[start] {
			end++
		}
		count, threshold := end-start, int64(values[start])
		if int64(count)*threshold > budget {
			break
		}
		if int64(active+count)*threshold > budget {
			spells++
			active = 0
		}
		active += count
		removed += count
		start = end
	}
	if active > 0 {
		spells++
	}
	return removed, spells
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var count int
	var budget int64
	fmt.Fscan(in, &count, &budget)
	values := make([]int, count)
	for index := range values {
		fmt.Fscan(in, &values[index])
	}
	removed, spells := safeRemovals(values, budget)
	fmt.Println(removed, spells)
}
