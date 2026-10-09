package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, k int
	fmt.Fscan(in, &n)
	base := make([]int, n)
	for i := range base {
		fmt.Fscan(in, &base[i])
	}
	var separator string
	fmt.Fscan(in, &separator, &k)
	// the i-th smallest element is the i-th element of the sorted database
	sort.Ints(base)
	for q := 0; q < k; q++ {
		var i int
		fmt.Fscan(in, &i)
		fmt.Fprintln(out, base[i-1])
	}
}
