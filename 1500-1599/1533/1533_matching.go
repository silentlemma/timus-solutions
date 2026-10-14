package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// heavier[i][j]: hobbit i is known to outweigh j
	heavier := make([][]bool, n)
	for i := range heavier {
		heavier[i] = make([]bool, n)
		for j := range heavier[i] {
			var x int
			fmt.Fscan(in, &x)
			heavier[i][j] = x == 1
		}
	}
	// the weighings are consistent, so the closure is a strict order
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			if heavier[i][k] {
				for j := 0; j < n; j++ {
					heavier[i][j] = heavier[i][j] || heavier[k][j]
				}
			}
		}
	}
	// by Dilworth, the largest set of incomparable hobbits is n minus a
	// maximum matching between "heavier" copies and "lighter" copies
	matchOf := make([]int, n) // the heavier hobbit matched to a lighter one
	for j := range matchOf {
		matchOf[j] = -1
	}
	var seen []bool
	var augment func(i int) bool
	augment = func(i int) bool {
		for j := 0; j < n; j++ {
			if heavier[i][j] && !seen[j] {
				seen[j] = true
				if matchOf[j] < 0 || augment(matchOf[j]) {
					matchOf[j] = i
					return true
				}
			}
		}
		return false
	}
	matched := make([]bool, n)
	for i := 0; i < n; i++ {
		seen = make([]bool, n)
		matched[i] = augment(i)
	}
	// Konig: walk alternating paths from the unmatched heavier copies; the
	// hobbits reached on the heavier side but not on the lighter side form
	// the answer, as everything else is a vertex cover
	left := make([]bool, n)
	right := make([]bool, n)
	var stack []int
	for i := 0; i < n; i++ {
		if !matched[i] {
			left[i] = true
			stack = append(stack, i)
		}
	}
	for len(stack) > 0 {
		i := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for j := 0; j < n; j++ {
			if heavier[i][j] && !right[j] {
				right[j] = true
				if owner := matchOf[j]; owner >= 0 && !left[owner] {
					left[owner] = true
					stack = append(stack, owner)
				}
			}
		}
	}
	var chosen []string
	for i := 0; i < n; i++ {
		if left[i] && !right[i] {
			chosen = append(chosen, fmt.Sprint(i+1))
		}
	}
	fmt.Println(len(chosen))
	fmt.Println(strings.Join(chosen, " "))
}
