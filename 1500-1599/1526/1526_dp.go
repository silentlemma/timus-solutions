package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var p, t, n, m int
	fmt.Fscan(in, &p, &t, &n, &m)
	half, full := t/2, 1<<uint(n)-1
	// after[x]: the dishes that may still be brought over a plate of dish x
	after := make([]int, n)
	for x := range after {
		after[x] = full
	}
	for k := 0; k < m; k++ {
		var i, j int
		fmt.Fscan(in, &i, &j)
		after[i-1] &^= 1 << uint(j-1)
	}
	// the count of time-tables depends only on the set of dishes that may be
	// brought; plates above a plate of x shrink that set to its part in after[x]
	seen := make([]bool, full+1)
	seen[full] = true
	stack, order := []int{full}, []int{}
	for len(stack) > 0 {
		allowed := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, allowed)
		for x := 0; x < n; x++ {
			if inner := allowed & after[x]; allowed>>uint(x)&1 == 1 && !seen[inner] {
				seen[inner] = true
				stack = append(stack, inner)
			}
		}
	}
	sort.Slice(order, func(a, b int) bool {
		return bits.OnesCount(uint(order[a])) < bits.OnesCount(uint(order[b]))
	})
	// ways[s][q]: time-tables of q dishes with the set s allowed
	ways := make([][]int, full+1)
	for _, allowed := range order {
		f := make([]int, half+1)
		tree := make([]int, half) // tree[q]: one plate with q dishes over it
		f[0] = 1
		for q := 1; q <= half; q++ {
			sum := 0
			for x := 0; x < n; x++ {
				if allowed>>uint(x)&1 == 1 {
					if inner := allowed & after[x]; inner == allowed {
						sum += f[q-1]
					} else {
						sum += ways[inner][q-1]
					}
				}
			}
			tree[q-1] = sum % p
			// the first plate holds a dishes over it, the rest follow it
			total := 0
			for a := 0; a < q; a++ {
				total = (total + tree[a]*f[q-1-a]) % p
			}
			f[q] = total
		}
		ways[allowed] = f
	}
	fmt.Println(ways[full][half] % p)
}
