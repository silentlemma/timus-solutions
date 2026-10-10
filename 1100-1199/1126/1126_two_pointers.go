package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var m int
	fmt.Fscan(in, &m)
	var values []int
	for {
		var v int
		if _, err := fmt.Fscan(in, &v); err != nil || v < 0 {
			break
		}
		values = append(values, v)
	}
	// indices of the window whose values decrease from front to back: the
	// front is the maximum, and a value never matters once a later one is larger
	window := make([]int, 0, len(values))
	head := 0
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i, v := range values {
		for len(window) > head && values[window[len(window)-1]] <= v {
			window = window[:len(window)-1]
		}
		window = append(window, i)
		if window[head] <= i-m {
			head++
		}
		if i >= m-1 {
			out.WriteString(strconv.Itoa(values[window[head]]) + "\n")
		}
	}
}
