package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func join(order []int) string {
	parts := make([]string, len(order))
	for i, v := range order {
		parts[i] = strconv.Itoa(v)
	}
	return strings.Join(parts, " ")
}

func main() {
	var n int
	fmt.Scan(&n)
	// the cheapest round trip, as a cycle through n: one side of n goes
	// 2, n - 2, 4, n - 4, ..., the other 1, n - 1, 3, n - 3, ...; step k
	// takes the pair k, k + 1 for odd k and n - k, n - k + 1 for even k
	used := make([]bool, n+1)
	used[n] = true
	var oneSide, otherSide []int
	for k := 1; ; k++ {
		a, b := k+1, k
		if k%2 == 0 {
			a, b = n-k, n-k+1
		}
		if a < 1 || used[a] || used[b] {
			break
		}
		oneSide = append(oneSide, a)
		otherSide = append(otherSide, b)
		used[a], used[b] = true, true
	}
	// the cycle: n, one side, the city left where the two sides meet if
	// any, and the other side back to n; it ends with city 1
	cycle := append([]int{n}, oneSide...)
	for v := 1; v < n; v++ {
		if !used[v] {
			cycle = append(cycle, v)
		}
	}
	for i := len(otherSide) - 1; i >= 0; i-- {
		cycle = append(cycle, otherSide[i])
	}
	cheap := append([]int{cycle[len(cycle)-1]}, cycle[:len(cycle)-1]...)
	// the dearest: odd numbers up, then even numbers down, so that every
	// city is next to the two closest in size
	var dear []int
	for v := 1; v <= n; v += 2 {
		dear = append(dear, v)
	}
	for v := n - n%2; v >= 2; v -= 2 {
		dear = append(dear, v)
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, join(cheap))
	fmt.Fprintln(out, join(dear))
}
