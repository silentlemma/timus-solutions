package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const modulus = 998244353
const primitiveRoot = 3
const directLimit = 32
const decimalBase = 10

func power(base, exponent int) int {
	result := 1
	for exponent > 0 {
		if exponent&1 != 0 {
			result = int(int64(result) * int64(base) % modulus)
		}
		base = int(int64(base) * int64(base) % modulus)
		exponent >>= 1
	}
	return result
}

func transform(data []int, inverse bool) {
	n := len(data)
	for i, j := 1, 0; i < n; i++ {
		bit := n >> 1
		for j&bit != 0 {
			j ^= bit
			bit >>= 1
		}
		j ^= bit
		if i < j {
			data[i], data[j] = data[j], data[i]
		}
	}
	for length := 2; length <= n; length <<= 1 {
		root := power(primitiveRoot, (modulus-1)/length)
		if inverse {
			root = power(root, modulus-2)
		}
		for start := 0; start < n; start += length {
			factor := 1
			for j := 0; j < length/2; j++ {
				first := data[start+j]
				second := int(int64(data[start+j+length/2]) * int64(factor) % modulus)
				sum := first + second
				if sum >= modulus {
					sum -= modulus
				}
				difference := first - second
				if difference < 0 {
					difference += modulus
				}
				data[start+j] = sum
				data[start+j+length/2] = difference
				factor = int(int64(factor) * int64(root) % modulus)
			}
		}
	}
	if inverse {
		scale := power(n, modulus-2)
		for i := range data {
			data[i] = int(int64(data[i]) * int64(scale) % modulus)
		}
	}
}

func matches(a, b []int) []int {
	prefix := make([]int, len(b))
	for i, j := 1, 0; i < len(b); i++ {
		for j > 0 && b[i]>>1 != b[j]>>1 {
			j = prefix[j-1]
		}
		if b[i]>>1 == b[j]>>1 {
			j++
		}
		prefix[i] = j
	}
	starts := make([]int, 0)
	for i, j := 0, 0; i < len(a); i++ {
		for j > 0 && a[i]>>1 != b[j]>>1 {
			j = prefix[j-1]
		}
		if a[i]>>1 == b[j]>>1 {
			j++
		}
		if j == len(b) {
			starts = append(starts, i-len(b)+1)
			j = prefix[j-1]
		}
	}
	return starts
}

func solve(a, b []int) (int, int) {
	n, m := len(a), len(b)
	if m > n {
		return -1, -1
	}
	starts := matches(a, b)
	if len(starts) == 0 {
		return -1, -1
	}
	best, answer := m+1, -1
	if len(starts) <= directLimit {
		for _, start := range starts {
			changes := 0
			for j := 0; j < m; j++ {
				changes += (a[start+j] ^ b[j]) & 1
			}
			if changes < best {
				best, answer = changes, start+1
			}
		}
		return best, answer
	}
	size := 1
	for size < n+m-1 {
		size <<= 1
	}
	first, second, prefix := make([]int, size), make([]int, size), make([]int, n+1)
	for i, value := range a {
		first[i] = value & 1
		prefix[i+1] = prefix[i] + first[i]
	}
	ones := 0
	for i, value := range b {
		second[m-1-i] = value & 1
		ones += value & 1
	}
	transform(first, false)
	transform(second, false)
	for i := range first {
		first[i] = int(int64(first[i]) * int64(second[i]) % modulus)
	}
	transform(first, true)
	for _, start := range starts {
		changes := prefix[start+m] - prefix[start] + ones - 2*first[start+m-1]
		if changes < best {
			best, answer = changes, start+1
		}
	}
	return best, answer
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	next := func(base int) int {
		for position < len(data) && data[position] <= ' ' {
			position++
		}
		value := 0
		for position < len(data) && data[position] > ' ' {
			value = value*base + int(data[position]-'0')
			position++
		}
		return value
	}
	n, m := next(decimalBase), next(decimalBase)
	a, b := make([]int, n), make([]int, m)
	for i := range a {
		a[i] = next(2)
	}
	for i := range b {
		b[i] = next(2)
	}
	best, start := solve(a, b)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if best < 0 {
		fmt.Fprintln(out, "No")
	} else {
		fmt.Fprintln(out, "Yes")
		fmt.Fprintln(out, best, start)
	}
}
