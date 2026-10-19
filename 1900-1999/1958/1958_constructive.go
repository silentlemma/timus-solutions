package main

import (
	"bufio"
	"fmt"
	"os"
)

func sortOperations(permutation []int) []int {
	values := append([]int(nil), permutation...)
	n := len(values)
	operations := make([]int, 0, (n-1)*(2*n-1))
	flush := func() {
		for values[n-1] != n {
			value := values[n-1]
			values[n-1], values[value-1] = values[value-1], value
			operations = append(operations, value)
		}
	}
	flush()
	unfixed := n - 1
	for unfixed > 0 {
		for unfixed > 0 && values[unfixed-1] == unfixed {
			unfixed--
		}
		if unfixed == 0 {
			break
		}
		start := 0
		for values[start] != 1 {
			start++
		}
		for position := start; position+1 < n; position++ {
			values[position], values[position+1] = values[position+1], 1
			operations = append(operations, 1)
		}
		flush()
	}
	return operations
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	values := make([]int, n)
	for i := range values {
		fmt.Fscan(in, &values[i])
	}
	operations := sortOperations(values)
	fmt.Fprintln(out, len(operations))
	for _, value := range operations {
		fmt.Fprintln(out, value)
	}
}
