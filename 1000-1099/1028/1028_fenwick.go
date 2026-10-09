package main

import (
	"bufio"
	"os"
	"strconv"
)

const maxCoord = 32000

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n := next()
	// stars come by y, then x: the level of a star is the number of stars
	// already seen with x not greater than its own; a Fenwick tree counts them
	tree := make([]int, maxCoord+2)
	count := make([]int, n)
	for i := 0; i < n; i++ {
		x := next()
		next()
		level := 0
		for j := x + 1; j > 0; j -= j & -j {
			level += tree[j]
		}
		count[level]++
		for j := x + 1; j <= maxCoord+1; j += j & -j {
			tree[j]++
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, c := range count {
		out.WriteString(strconv.Itoa(c))
		out.WriteByte('\n')
	}
}
