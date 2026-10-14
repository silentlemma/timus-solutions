package main

import (
	"bufio"
	"os"
	"strconv"
)

const most = 4 // the highest K asked for

func power(b, e, mod int64) int64 {
	r := int64(1)
	for b %= mod; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * b % mod
		}
		b = b * b % mod
	}
	return r
}

func main() {
	in := bufio.NewScanner(bufio.NewReader(os.Stdin))
	in.Split(bufio.ScanWords)
	word := func() string {
		in.Scan()
		return in.Text()
	}
	number := func() int64 {
		v, _ := strconv.Atoi(word())
		return int64(v)
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	n, m, mod := int(number()), int(number()), number()
	values := make([]int64, n+1)
	// trees[j] is a Fenwick tree of the power sums of a^j for j = 1..4; the
	// sums stay unreduced and are only reduced when a query reads them
	trees := make([][]int64, most+1)
	for j := range trees {
		trees[j] = make([]int64, n+1)
	}
	for i := 1; i <= n; i++ {
		values[i] = (number()%mod + mod) % mod
		p := int64(1)
		for j := 1; j <= most; j++ {
			p = p * values[i] % mod
			trees[j][i] += p
		}
	}
	for j := 1; j <= most; j++ {
		for i := 1; i <= n; i++ {
			if up := i + i&-i; up <= n {
				trees[j][up] += trees[j][i]
			}
		}
	}
	var inverse [most + 1]int64
	for k := 1; k <= most; k++ {
		inverse[k] = power(int64(k), mod-2, mod)
	}
	for q := 0; q < m; q++ {
		if word() == "I" {
			i, delta := int(number()), number()
			old := values[i]
			now := ((old+delta)%mod + mod) % mod
			values[i] = now
			po, pn := int64(1), int64(1)
			for j := 1; j <= most; j++ {
				po, pn = po*old%mod, pn*now%mod
				for k := i; k <= n; k += k & -k {
					trees[j][k] += pn - po
				}
			}
			continue
		}
		left, right, top := int(number()), int(number()), int(number())
		var sums, e [most + 1]int64
		for j := 1; j <= top; j++ {
			total := int64(0)
			for k := right; k > 0; k -= k & -k {
				total += trees[j][k]
			}
			for k := left - 1; k > 0; k -= k & -k {
				total -= trees[j][k]
			}
			sums[j] = (total%mod + mod) % mod
		}
		// Newton's identities: k e(k) is the alternating sum of e(k - i) p(i)
		e[0] = 1
		for k := 1; k <= top; k++ {
			acc := int64(0)
			for i := 1; i <= k; i++ {
				term := e[k-i] * sums[i] % mod
				if i%2 == 1 {
					acc += term
				} else {
					acc += mod - term
				}
			}
			e[k] = acc % mod * inverse[k] % mod
		}
		for k := 0; k <= top; k++ {
			if k > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.FormatInt(e[k], 10))
		}
		out.WriteByte('\n')
	}
}
