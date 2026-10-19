package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 1000000007

func power(base, exponent int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent&1 != 0 {
			result = result * base % modulus
		}
		base = base * base % modulus
		exponent /= 2
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, selected int
	fmt.Fscan(in, &n, &selected)
	classes := make([]int, n)
	for i := range classes {
		fmt.Fscan(in, &classes[i])
	}
	var identified, position int
	fmt.Fscan(in, &identified, &position)
	lower, greater := 0, 0
	for _, value := range classes {
		if value < classes[identified-1] {
			lower++
		} else if value > classes[identified-1] {
			greater++
		}
	}
	factorial, inverse := make([]int64, n), make([]int64, n)
	factorial[0] = 1
	for i := 1; i < n; i++ {
		factorial[i] = factorial[i-1] * int64(i) % modulus
	}
	inverse[n-1] = power(factorial[n-1], modulus-2)
	for i := n - 1; i > 0; i-- {
		inverse[i-1] = inverse[i] * int64(i) % modulus
	}
	choose := func(total, take int) int64 {
		if take < 0 || take > total {
			return 0
		}
		return factorial[total] * inverse[take] % modulus * inverse[total-take] % modulus
	}
	others := n - 1
	bad := func(pool, threshold int) int64 {
		limit := selected - 1
		if pool < limit {
			limit = pool
		}
		result := int64(0)
		for count := threshold; count <= limit; count++ {
			result += choose(pool, count) * choose(others-pool, selected-1-count) % modulus
			result %= modulus
		}
		return result
	}
	answer := choose(others, selected-1)
	answer = (answer - bad(lower, position) + modulus) % modulus
	answer = (answer - bad(greater, selected-position+1) + modulus) % modulus
	fmt.Println(answer)
}
