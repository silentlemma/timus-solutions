package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const most = 1000000000 // nobody but Vasily earns more; nobody earns less than 0

var (
	parent, sizes []int
	offset        []int64
)

func find(x int) int {
	var path []int
	for parent[x] != x {
		path = append(path, x)
		x = parent[x]
	}
	// compress: walk back from the node nearest to the root
	total := int64(0)
	for k := len(path) - 1; k >= 0; k-- {
		v := path[k]
		total += offset[v]
		offset[v] = total
		parent[v] = x
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, m int
	fmt.Fscan(in, &n, &m)
	// a weighted union-find: salary[x] = salary[root] + offset[x], and every
	// root keeps the range its own salary may take so that all salaries of
	// its set stay in [0, most]; Vasily (0) is pinned to 0
	parent, sizes, offset = make([]int, n), make([]int, n), make([]int64, n)
	low, high := make([]int64, n), make([]int64, n)
	for x := 0; x < n; x++ {
		parent[x], sizes[x], high[x] = x, 1, most
	}
	high[0] = 0
	for k := 1; k <= m; k++ {
		var i, j int
		var d int64
		fmt.Fscan(in, &i, &j, &d)
		ri, rj := find(i), find(j)
		// salary[i] - salary[j] = d means salary[rj] = salary[ri] + shift
		shift := offset[i] - offset[j] - d
		ok := shift == 0
		if ri != rj {
			if sizes[ri] < sizes[rj] {
				ri, rj, shift = rj, ri, -shift
			}
			// salary[rj] lies in [low[rj], high[rj]], so salary[ri] in that minus shift
			if low[rj]-shift > low[ri] {
				low[ri] = low[rj] - shift
			}
			if high[rj]-shift < high[ri] {
				high[ri] = high[rj] - shift
			}
			ok = low[ri] <= high[ri]
			parent[rj], offset[rj] = ri, shift
			sizes[ri] += sizes[rj]
		}
		if !ok {
			fmt.Fprintf(out, "Impossible after %d statements\n", k)
			return
		}
	}
	out.WriteString("Possible\n")
	for x := 0; x < n; x++ {
		r := find(x)
		out.WriteString(strconv.FormatInt(low[r]+offset[x], 10))
		out.WriteByte('\n')
	}
}
