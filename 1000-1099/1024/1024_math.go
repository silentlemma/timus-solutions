package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	p := make([]int, n+1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &p[i])
	}
	// P^k is the identity exactly when k is a multiple of every cycle length:
	// the order is their least common multiple
	seen := make([]bool, n+1)
	order := int64(1)
	for i := 1; i <= n; i++ {
		length := int64(0)
		for j := i; !seen[j]; j = p[j] {
			seen[j] = true
			length++
		}
		if length > 0 {
			order = order / gcd(order, length) * length
		}
	}
	fmt.Println(order)
}
