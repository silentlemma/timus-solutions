package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const mod int64 = 998244353
const root int64 = 3

func power(base, exponent int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent&1 != 0 {
			result = result * base % mod
		}
		base = base * base % mod
		exponent >>= 1
	}
	return result
}

func transform(a []int64, inverse bool) {
	size := len(a)
	for i, j := 1, 0; i < size; i++ {
		bit := size >> 1
		for j&bit != 0 {
			j ^= bit
			bit >>= 1
		}
		j ^= bit
		if i < j {
			a[i], a[j] = a[j], a[i]
		}
	}
	for length := 2; length <= size; length <<= 1 {
		step := power(root, (mod-1)/int64(length))
		if inverse {
			step = power(step, mod-2)
		}
		half := length / 2
		for start := 0; start < size; start += length {
			weight := int64(1)
			for j := 0; j < half; j++ {
				left := a[start+j]
				right := weight * a[start+j+half] % mod
				sum, difference := left+right, left-right
				if sum >= mod {
					sum -= mod
				}
				if difference < 0 {
					difference += mod
				}
				a[start+j], a[start+j+half] = sum, difference
				weight = weight * step % mod
			}
		}
	}
	if inverse {
		scale := power(int64(size), mod-2)
		for i := range a {
			a[i] = a[i] * scale % mod
		}
	}
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	next := func() int64 {
		for position < len(data) && data[position] <= ' ' {
			position++
		}
		value := int64(0)
		for position < len(data) && data[position] >= '0' && data[position] <= '9' {
			value = value*10 + int64(data[position]-'0')
			position++
		}
		return value
	}
	n, days := int(next()), next()
	size := 1
	for size < 2*n-1 {
		size <<= 1
	}
	values, kernel := make([]int64, size), make([]int64, size)
	inverses := make([]int64, n)
	for i := 0; i < n; i++ {
		values[i] = next()
	}
	inverses[1], kernel[0] = 1, 1
	// Repeated prefix sums have coefficients C(days + i - 1, i).
	for i := 1; i < n; i++ {
		if i > 1 {
			inverses[i] = mod - (mod/int64(i))*inverses[mod%int64(i)]%mod
		}
		kernel[i] = kernel[i-1] * (days + int64(i) - 1) % mod * inverses[i] % mod
	}
	transform(values, false)
	transform(kernel, false)
	for i := range values {
		values[i] = values[i] * kernel[i] % mod
	}
	transform(values, true)
	out := bufio.NewWriter(os.Stdout)
	for i := 0; i < n; i++ {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, values[i])
	}
	fmt.Fprintln(out)
	out.Flush()
}
