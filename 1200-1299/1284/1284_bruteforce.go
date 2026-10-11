package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	top   = 101 // card values are 1..100
	suits = 11
)

// permutations calls visit with every ordering of a, rearranging it in place
func permutations(a []int, k int, visit func()) {
	if k == len(a) {
		visit()
		return
	}
	for i := k; i < len(a); i++ {
		a[k], a[i] = a[i], a[k]
		permutations(a, k+1, visit)
		a[k], a[i] = a[i], a[k]
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	values, kinds := make([]int, n), make([]int, n)
	seen := map[int]bool{}
	var blue, yellow []int
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &values[i], &kinds[i])
		if !seen[kinds[i]] {
			seen[kinds[i]] = true
			if kinds[i]%2 == 1 {
				blue = append(blue, kinds[i])
			} else {
				yellow = append(yellow, kinds[i])
			}
		}
	}
	// who starts: the larger colour group, or either when they are equal
	var starts [][2][]int
	if len(blue) >= len(yellow) {
		starts = append(starts, [2][]int{blue, yellow})
	}
	if len(yellow) >= len(blue) {
		starts = append(starts, [2][]int{yellow, blue})
	}
	best := 0
	var place [suits]int
	for _, pair := range starts {
		a, b := pair[0], pair[1]
		permutations(a, 0, func() {
			permutations(b, 0, func() {
				for i, s := range a {
					place[s] = 2 * i
				}
				for i, s := range b {
					place[s] = 2*i + 1
				}
				for _, sign := range []int{1, -1} {
					// cards that stay form an increasing run of target ranks
					var tails []int
					for i := 0; i < n; i++ {
						rank := place[kinds[i]]*top + sign*values[i]
						k := sort.SearchInts(tails, rank)
						if k == len(tails) {
							tails = append(tails, rank)
						} else {
							tails[k] = rank
						}
					}
					if len(tails) > best {
						best = len(tails)
					}
				}
			})
		})
	}
	fmt.Println(n - best)
}
