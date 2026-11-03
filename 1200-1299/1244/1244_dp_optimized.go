package main

import (
	"bufio"
	"fmt"
	"os"
)

const many = 2

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var weight, n int
	fmt.Fscan(in, &weight, &n)
	cards := make([]int, n+1)
	total := 0
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &cards[i])
		total += cards[i]
	}
	selectMissing := total-weight < weight
	target := weight
	if total-weight < target {
		target = total - weight
	}
	ways, last := make([]byte, target+1), make([]byte, target+1)
	ways[0] = 1
	// Complementing subsets preserves uniqueness. Descending sums prevent
	// card reuse, and first-reach parents remain fixed for reconstruction.
	for i := 1; i <= n; i++ {
		for sum := target; sum >= cards[i]; sum-- {
			if ways[sum] == 0 && ways[sum-cards[i]] != 0 {
				last[sum] = byte(i)
			}
			count := ways[sum] + ways[sum-cards[i]]
			if count > many {
				count = many
			}
			ways[sum] = count
		}
		if ways[target] == many {
			fmt.Fprintln(out, -1)
			return
		}
	}
	if ways[target] == 0 {
		fmt.Fprintln(out, 0)
		return
	}
	chosen := make([]bool, n+1)
	for sum := target; sum > 0; sum -= cards[last[sum]] {
		chosen[last[sum]] = true
	}
	first := true
	for i := 1; i <= n; i++ {
		if chosen[i] == selectMissing {
			if !first {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, i)
			first = false
		}
	}
	fmt.Fprintln(out)
}
