package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	short  = 32 // cycles up to this length are summed directly
	primes = 3
	root   = 3
	span   = 3 // a product of L and 2L numbers has fewer than 3L
)

var mods = [primes]uint64{998244353, 167772161, 469762049} // NTT primes, root 3

func power(b, e, mod uint64) uint64 {
	r := uint64(1)
	for b %= mod; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * b % mod
		}
		b = b * b % mod
	}
	return r
}

func ntt(a []uint64, invert bool, mod uint64) {
	n := len(a)
	for i, j := 1, 0; i < n; i++ {
		bit := n >> 1
		for ; j&bit != 0; bit >>= 1 {
			j ^= bit
		}
		j ^= bit
		if i < j {
			a[i], a[j] = a[j], a[i]
		}
	}
	for length := 2; length <= n; length <<= 1 {
		w := power(root, (mod-1)/uint64(length), mod)
		if invert {
			w = power(w, mod-2, mod)
		}
		half := length / 2
		for i := 0; i < n; i += length {
			wn := uint64(1)
			for k := 0; k < half; k++ {
				u, v := a[i+k], a[i+k+half]*wn%mod
				a[i+k] = (u + v) % mod
				a[i+k+half] = (u + mod - v) % mod
				wn = wn * w % mod
			}
		}
	}
	if invert {
		inv := power(uint64(n), mod-2, mod)
		for i := range a {
			a[i] = a[i] * inv % mod
		}
	}
}

// cyclic gives out[s] = sum over r of fold[r] * cycle[(s + r) mod L]; every sum is below 2^63
func cyclic(fold, cycle []uint64) []uint64 {
	size := len(cycle)
	out := make([]uint64, size)
	if size <= short {
		for s := 0; s < size; s++ {
			for r := 0; r < size; r++ {
				out[s] += fold[r] * cycle[(s+r)%size]
			}
		}
		return out
	}
	// reversed fold times the cycle written twice, modulo three primes,
	// put together by Garner's method; wrapping 64-bit arithmetic is exact here
	n := 1
	for n < span*size {
		n <<= 1
	}
	var residue [primes][]uint64
	for k, mod := range mods {
		a, b := make([]uint64, n), make([]uint64, n)
		for r := 0; r < size; r++ {
			a[size-1-r] = fold[r] % mod
		}
		for i := 0; i < 2*size; i++ {
			b[i] = cycle[i%size] % mod
		}
		ntt(a, false, mod)
		ntt(b, false, mod)
		for i := range a {
			a[i] = a[i] * b[i] % mod
		}
		ntt(a, true, mod)
		residue[k] = a
	}
	m0, m1, m2 := mods[0], mods[1], mods[2]
	inv01, inv012 := power(m0%m1, m1-2, m1), power(m0*m1%m2, m2-2, m2)
	for s := 0; s < size; s++ {
		i := s + size - 1
		x0 := residue[0][i]
		x1 := (residue[1][i] + m1 - x0%m1) % m1 * inv01 % m1
		low := (x0 + x1*m0) % m2
		x2 := (residue[2][i] + m2 - low) % m2 * inv012 % m2
		out[s] = x0 + x1*m0 + x2*m0*m1
	}
	return out
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() uint64 {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return uint64(v)
	}
	m, n := int(next()), int(next())
	p := make([]int, n)
	for i := range p {
		p[i] = int(next()) - 1
	}
	byYear := make([]uint64, m+1) // byYear[t] = q_t
	for t := 1; t <= m; t++ {
		byYear[t] = next()
	}
	// the year t row is p applied t times, so the answer at j is the sum of
	// q_t p^t(j); along a cycle of p this is a cyclic correlation
	answer := make([]uint64, n)
	seen := make([]bool, n)
	folds := map[int][]uint64{} // cycle length -> sums of q_t over t with equal remainders
	for start := 0; start < n; start++ {
		if seen[start] {
			continue
		}
		var cycle []int
		for j := start; !seen[j]; j = p[j] {
			seen[j] = true
			cycle = append(cycle, j)
		}
		size := len(cycle)
		if _, ok := folds[size]; !ok {
			fold := make([]uint64, size)
			for t := 1; t <= m; t++ {
				fold[t%size] += byYear[t]
			}
			folds[size] = fold
		}
		values := make([]uint64, size)
		for s, j := range cycle {
			values[s] = uint64(j + 1)
		}
		values = cyclic(folds[size], values)
		for s, j := range cycle {
			answer[j] = values[s]
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for j, v := range answer {
		if j > 0 {
			out.WriteByte(' ')
		}
		out.WriteString(strconv.FormatUint(v, 10))
	}
	out.WriteByte('\n')
}
