package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n, k int
	fmt.Fscan(reader, &n, &k)
	ending := make([][]int, n+1) // the cuts u-v with u < v, kept at v
	for i := 0; i < k; i++ {
		var a, b int
		fmt.Fscan(reader, &a, &b)
		if a > b {
			a, b = b, a
		}
		ending[b] = append(ending[b], a)
	}
	var cuts [][2]int
	// a convex face is cut into triangles by diagonals from its first
	// vertex; the first and the last of its sides already exist
	fan := func(face []int) {
		for i := 2; i+1 < len(face); i++ {
			cuts = append(cuts, [2]int{face[0], face[i]})
		}
	}
	// walk the vertices in order: a cut u-v closes the face formed by u,
	// the vertices still stacked above it, and v; nearer u first
	var stack []int
	for v := 1; v <= n; v++ {
		stack = append(stack, v)
		sort.Sort(sort.Reverse(sort.IntSlice(ending[v])))
		for _, u := range ending[v] {
			stack = stack[:len(stack)-1]
			start := len(stack) - 1
			for stack[start] != u {
				start--
			}
			face := append(append([]int(nil), stack[start:]...), v)
			fan(face)
			stack = append(stack[:start+1], v)
		}
	}
	fan(stack) // the last face, closed by the side n-1
	writer.WriteString(strconv.Itoa(len(cuts)) + "\n")
	for _, c := range cuts {
		writer.WriteString(strconv.Itoa(c[0]) + " " + strconv.Itoa(c[1]) + "\n")
	}
}
