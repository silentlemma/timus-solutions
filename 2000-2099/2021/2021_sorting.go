package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func order(scores []int) []int {
	ids := make([]int, len(scores))
	for i := range ids {
		ids[i] = i
	}
	sort.Slice(ids, func(i, j int) bool {
		a, b := ids[i], ids[j]
		if scores[a] != scores[b] {
			return scores[a] < scores[b]
		}
		return a < b
	})
	return ids
}

func reverse(ids []int) {
	for i, j := 0, len(ids)-1; i < j; i, j = i+1, j-1 {
		ids[i], ids[j] = ids[j], ids[i]
	}
}

func solve(first, second []int) [][2]int {
	a, b := order(first), order(second)
	totalA, totalB := 0, 0
	for i := range first {
		totalA += first[i]
		totalB += second[i]
	}
	if totalA > totalB {
		reverse(b)
	} else if totalA < totalB {
		reverse(a)
	}
	answer := make([][2]int, len(first))
	for i := range answer {
		answer[i] = [2]int{a[i], b[i]}
	}
	return answer
}

func run(in *bufio.Reader, out *bufio.Writer) {
	var n int
	fmt.Fscan(in, &n)
	first, second := make([]int, n), make([]int, n)
	for i := range first {
		fmt.Fscan(in, &first[i])
	}
	for i := range second {
		fmt.Fscan(in, &second[i])
	}
	for _, row := range solve(first, second) {
		fmt.Fprintln(out, row[0]+1, row[1]+1)
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	run(in, out)
}
