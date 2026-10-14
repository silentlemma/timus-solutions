package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	// a Fenwick tree over the circle: 1 for a soldier still marching
	tree := make([]int, n+1)
	for i := 1; i <= n; i++ {
		tree[i]++
		if p := i + i&-i; p <= n {
			tree[p] += tree[i]
		}
	}
	top := 1
	for top*2 <= n {
		top *= 2
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for rank, left := 0, n; left > 0; left-- {
		// the soldier k places ahead, counting among those still marching
		rank = (rank + k - 1) % left
		// descend to the (rank + 1)-th remaining soldier
		pos, need := 0, rank+1
		for step := top; step > 0; step /= 2 {
			if pos+step <= n && tree[pos+step] < need {
				pos += step
				need -= tree[pos]
			}
		}
		pos++
		out.WriteString(strconv.Itoa(pos))
		if left > 1 {
			out.WriteByte(' ')
		} else {
			out.WriteByte('\n')
		}
		for i := pos; i <= n; i += i & -i {
			tree[i]--
		}
	}
}
