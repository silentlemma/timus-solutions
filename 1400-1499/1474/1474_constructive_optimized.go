package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var n int
	fmt.Scan(&n)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.Itoa(n*(n+2)) + "\n")

	tokens := make([]string, 2*n+1)
	for i := range tokens {
		tokens[i] = strconv.Itoa(i)
	}
	hole, direction := n, 1
	for run := 0; run <= 2*n; run++ {
		length, slide := n, -1
		// Rising runs slide last and falling runs slide first.
		if run < n {
			length, slide = run+1, run
		} else if run > n {
			length, slide = 2*n-run+1, 0
		}
		for i := 0; i < length; i++ {
			distance := 2
			if i == slide {
				distance = 1
			}
			hole += distance * direction
			if run != 0 {
				out.WriteByte(' ')
			}
			out.WriteString(tokens[hole])
		}
		direction = -direction
	}
	out.WriteByte('\n')
}
