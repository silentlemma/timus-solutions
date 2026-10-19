package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxTerm = 300
const blockSize = 1 << 16
const ringSize = maxTerm + 1

func primesUpTo(bound int) []int {
	composite := make([]bool, bound+1)
	primes := []int{}
	for p := 2; p <= bound; p++ {
		if !composite[p] {
			primes = append(primes, p)
			for multiple := p * p; multiple <= bound; multiple += p {
				composite[multiple] = true
			}
		}
	}
	return primes
}

func divisorBlock(left, right int, primes []int) []uint16 {
	size := right - left + 1
	remaining := make([]int, size)
	counts := make([]uint16, size)
	for i := range counts {
		remaining[i] = left + i
		counts[i] = 1
	}
	for _, p := range primes {
		if p*p > right {
			break
		}
		for offset := (p - left%p) % p; offset < size; offset += p {
			exponent := uint16(0)
			for remaining[offset]%p == 0 {
				remaining[offset] /= p
				exponent++
			}
			counts[offset] *= exponent + 1
		}
	}
	for i, value := range remaining {
		if value > 1 {
			counts[i] *= 2
		}
	}
	return counts
}

func solve(n int) []int {
	limit, root := maxTerm*n, 1
	for (root+1)*(root+1) <= limit {
		root++
	}
	primes := primesUpTo(root)
	history := []uint16{}
	depth := make([]int, ringSize)
	for left := 1; left <= limit; left += blockSize {
		right := left + blockSize - 1
		if right > limit {
			right = limit
		}
		counts := divisorBlock(left, right, primes)
		for offset, raw := range counts {
			total, term := left+offset, int(raw)
			history = append(history, raw)
			current := 0
			if total <= maxTerm {
				current = 1
			}
			if term <= maxTerm && total > term {
				previous := depth[(total-term)%ringSize]
				if previous > 0 && previous+1 > current {
					current = previous + 1
				}
			}
			depth[total%ringSize] = current
			if current >= n {
				answer := make([]int, n)
				for i := n - 1; i > 0; i-- {
					answer[i] = int(history[total-1])
					total -= answer[i]
				}
				answer[0] = total
				return answer
			}
		}
	}
	return nil
}

func main() {
	var n int
	fmt.Fscan(os.Stdin, &n)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	answer := solve(n)
	if answer == nil {
		fmt.Fprintln(out, "Impossible")
		return
	}
	for i, value := range answer {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, value)
	}
	fmt.Fprintln(out)
}
