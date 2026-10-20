package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	a := make([]int64, n)
	for i := range a {
		fmt.Fscan(reader, &a[i])
	}
	// Around the circle the rises and the falls cancel out, so the
	// conversations where the next friend is less interesting sum to the same
	// as those where the next one is more interesting; equal neighbours add 0.
	var falls, rises, ties []int
	for i := 0; i < n; i++ {
		next := a[(i+1)%n]
		switch {
		case a[i] > next:
			falls = append(falls, i+1)
		case a[i] < next:
			rises = append(rises, i+1)
		default:
			ties = append(ties, i+1)
		}
	}
	if len(falls) == 0 {
		// every difference is 0: one conversation against all the others
		falls = append(falls, ties[len(ties)-1])
		ties = ties[:len(ties)-1]
	}
	rises = append(rises, ties...)
	writer.WriteString("YES\n")
	for _, part := range [][]int{falls, rises} {
		writer.WriteString(strconv.Itoa(len(part)) + "\n")
		for i, x := range part {
			if i > 0 {
				writer.WriteByte(' ')
			}
			writer.WriteString(strconv.Itoa(x))
		}
		writer.WriteByte('\n')
	}
}
