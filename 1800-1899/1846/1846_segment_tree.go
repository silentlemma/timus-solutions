package main

import (
	"bufio"
	"os"
	"strconv"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() string {
		in.Scan()
		return in.Text()
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	q, _ := strconv.Atoi(next())
	size := 1
	for size < q {
		size *= 2
	}
	// every addition gets its own leaf; an empty leaf holds 0, which does
	// not change a gcd
	tree := make([]int, 2*size)
	leaves := map[int][]int{} // value -> leaves that hold it
	for k := 0; k < q; k++ {
		sign := next()
		x, _ := strconv.Atoi(next())
		var v, value int
		if sign == "+" {
			leaves[x] = append(leaves[x], k)
			v, value = k+size, x
		} else {
			held := leaves[x]
			v = held[len(held)-1] + size
			leaves[x] = held[:len(held)-1]
		}
		tree[v] = value
		// once a node keeps its value, so do all above it
		for v /= 2; v > 0; v /= 2 {
			g := gcd(tree[2*v], tree[2*v+1])
			if tree[v] == g {
				break
			}
			tree[v] = g
		}
		answer := tree[1]
		if answer == 0 {
			answer = 1
		}
		out.WriteString(strconv.Itoa(answer))
		out.WriteByte('\n')
	}
}
