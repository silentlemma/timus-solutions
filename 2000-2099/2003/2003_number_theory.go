package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const persistentCount = 3

func solve(values []int) string {
	maximum := 0
	for _, value := range values {
		if value > maximum {
			maximum = value
		}
	}
	limit := 0
	for (limit+1)*(limit+1) <= maximum {
		limit++
	}
	composite := make([]bool, limit+1)
	primes := []int{}
	for prime := 2; prime <= limit; prime++ {
		if composite[prime] {
			continue
		}
		primes = append(primes, prime)
		for multiple := prime * prime; multiple <= limit; multiple += prime {
			composite[multiple] = true
		}
	}
	counts := make(map[int]int)
	best := 0
	for _, value := range values {
		for _, prime := range primes {
			if prime*prime > value {
				break
			}
			if value%prime != 0 {
				continue
			}
			counts[prime]++
			count := counts[prime]
			if count == persistentCount {
				return "infinity"
			}
			if count > best {
				best = count
			}
			for value%prime == 0 {
				value /= prime
			}
		}
		if value > 1 {
			counts[value]++
			count := counts[value]
			if count == persistentCount {
				return "infinity"
			}
			if count > best {
				best = count
			}
		}
	}
	return strconv.Itoa(best)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var size int
	fmt.Fscan(in, &size)
	values := make([]int, size)
	for i := range values {
		fmt.Fscan(in, &values[i])
	}
	fmt.Println(solve(values))
}
