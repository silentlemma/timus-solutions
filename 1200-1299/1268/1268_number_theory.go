package main

import (
	"bufio"
	"os"
	"strconv"
)

const limit = 1 << 16 // N < 65536

func power(b, e, m int) int {
	r := 1
	for b %= m; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * b % m
		}
		b = b * b % m
	}
	return r
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// smallest prime factor of every number below the limit
	spf := make([]int, limit)
	for i := range spf {
		spf[i] = i
	}
	for i := 2; i*i < limit; i++ {
		if spf[i] == i {
			for j := i * i; j < limit; j += i {
				if spf[j] == j {
					spf[j] = i
				}
			}
		}
	}
	known := make([]int, limit)
	in.Scan()
	t, _ := strconv.Atoi(in.Text())
	for ; t > 0; t-- {
		in.Scan()
		p, _ := strconv.Atoi(in.Text())
		if known[p] == 0 {
			// g is a primitive root when no g^((p-1)/q) is 1 for a prime q | p-1
			var quotients []int
			for rest := p - 1; rest > 1; {
				q := spf[rest]
				quotients = append(quotients, (p-1)/q)
				for rest%q == 0 {
					rest /= q
				}
			}
			g := p - 1
			for ; ; g-- {
				root := true
				for _, e := range quotients {
					if power(g, e, p) == 1 {
						root = false
						break
					}
				}
				if root {
					break
				}
			}
			known[p] = g
		}
		out.WriteString(strconv.Itoa(known[p]))
		out.WriteString("\n")
	}
}
