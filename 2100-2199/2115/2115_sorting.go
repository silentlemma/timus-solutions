package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const swapped = 2 // a single swap changes exactly two places

func equal(a, b []int) bool {
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	ascending := append([]int(nil), a...)
	sort.Ints(ascending)
	descending := make([]int, n)
	for i, v := range ascending {
		descending[n-1-i] = v
	}
	if equal(a, ascending) || equal(a, descending) {
		fmt.Println("Nothing to do here")
		return
	}
	// one swap can only fix a line that differs from a sorted one in exactly
	// two places, and then the swap of those two places does it
	for _, t := range [][]int{ascending, descending} {
		var wrong []int
		for i := 0; i < n && len(wrong) <= swapped; i++ {
			if a[i] != t[i] {
				wrong = append(wrong, i)
			}
		}
		if len(wrong) != swapped {
			continue
		}
		i, j := wrong[0], wrong[1]
		if a[i] == t[j] && a[j] == t[i] {
			fmt.Println("Yes")
			fmt.Println(i+1, j+1)
			return
		}
	}
	fmt.Println("No hope")
}
