package main

import (
	"bufio"
	"os"
	"strconv"
)

// moduli are below this bound
const limit = 32768

func power(b, e, p int64) int64 {
	r := int64(1)
	for b %= p; e > 0; e, b = e/2, b*b%p {
		if e%2 == 1 {
			r = r * b % p
		}
	}
	return r
}

// sqrtMod is Tonelli-Shanks for an odd prime p = q * 2^s + 1, a quadratic
// residue a and a non-residue z
func sqrtMod(a, p, z int64) int64 {
	q, s := p-1, int64(0)
	for q%2 == 0 {
		q /= 2
		s++
	}
	c, t, r := power(z, q, p), power(a, q, p), power(a, (q+1)/2, p)
	for t != 1 {
		// the order of t is 2^i with i < s; b fixes the top bits
		i, tt := int64(0), t
		for tt != 1 {
			tt = tt * tt % p
			i++
		}
		b := power(c, int64(1)<<uint(s-i-1), p)
		s, c = i, b*b%p
		t, r = t*c%p, r*b%p
	}
	return r
}

func readInt(in *bufio.Reader) int64 {
	c, _ := in.ReadByte()
	for c == ' ' || c == '\n' || c == '\r' {
		c, _ = in.ReadByte()
	}
	n := int64(0)
	for ; c >= '0' && c <= '9'; c, _ = in.ReadByte() {
		n = n*10 + int64(c-'0')
	}
	return n
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	k := readInt(in)
	nonResidue := make([]int64, limit)
	for ; k > 0; k-- {
		a, p := readInt(in), readInt(in)
		a %= p
		if p == 2 {
			out.WriteString("1\n")
			continue
		}
		half := (p - 1) / 2
		if power(a, half, p) != 1 {
			out.WriteString("No root\n")
			continue
		}
		if nonResidue[p] == 0 {
			z := int64(2)
			for power(z, half, p) != p-1 {
				z++
			}
			nonResidue[p] = z
		}
		r := sqrtMod(a, p, nonResidue[p])
		lo, hi := r, p-r
		if lo > hi {
			lo, hi = hi, lo
		}
		out.WriteString(strconv.FormatInt(lo, 10) + " " + strconv.FormatInt(hi, 10) + "\n")
	}
}
