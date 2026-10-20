package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	a := make([]int64, n)
	b := make([]int64, n)
	for i := range a {
		fmt.Fscan(reader, &a[i])
	}
	for i := range b {
		fmt.Fscan(reader, &b[i])
	}
	var p int64
	fmt.Fscan(reader, &p)
	sort.Slice(a, func(i, j int) bool { return a[i] < a[j] })
	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
	// The i-th weakest student can take any of the problems they can solve,
	// except the i problems already taken by weaker students.
	ways := 1 % p
	solvable := 0
	for i := 0; i < n; i++ {
		for solvable < n && b[solvable] <= a[i] {
			solvable++
		}
		ways = ways * (int64(solvable-i) % p) % p
	}
	fmt.Println(ways)
}
