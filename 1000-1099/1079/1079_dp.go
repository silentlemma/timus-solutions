package main

import (
	"bufio"
	"fmt"
	"os"
)

const top = 99999

func main() {
	a := make([]int, top+1)
	best := make([]int, top+1)
	a[1], best[1] = 1, 1
	for i := 2; i <= top; i++ {
		if i%2 == 0 {
			a[i] = a[i/2]
		} else {
			a[i] = a[i/2] + a[i/2+1]
		}
		best[i] = best[i-1]
		if a[i] > best[i] {
			best[i] = a[i]
		}
	}
	in := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	for {
		var n int
		if _, err := fmt.Fscan(in, &n); err != nil || n == 0 {
			break
		}
		fmt.Fprintln(w, best[n])
	}
}
