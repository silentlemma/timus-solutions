package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// 2 * 3: both must be invertible modulo n
const bad = 6

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var n int
	fmt.Scan(&n)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	if gcd(n, bad) != 1 {
		fmt.Fprintln(writer, "No")
		return
	}
	// queen i on row 2i: rows 2i, diagonals 3i and anti-diagonals i are all
	// different modulo n
	fmt.Fprintln(writer, "Yes")
	for i := 0; i < n; i++ {
		if i > 0 {
			writer.WriteByte(' ')
		}
		writer.WriteString(strconv.Itoa(2*i%n + 1))
	}
	writer.WriteByte('\n')
}
