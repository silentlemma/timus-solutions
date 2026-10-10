package main

import (
	"fmt"
	"math/big"
	"strings"
)

// inc gives x + 1 for a decimal string
func inc(x string) string {
	b := []byte(x)
	k := len(b) - 1
	for k >= 0 && b[k] == '9' {
		b[k] = '0'
		k--
	}
	if k < 0 {
		return "1" + string(b)
	}
	b[k]++
	return string(b)
}

// dec gives x - 1 for a positive decimal string
func dec(x string) string {
	b := []byte(x)
	k := len(b) - 1
	for b[k] == '0' {
		b[k] = '9'
		k--
	}
	b[k]--
	if b[0] == '0' && len(b) > 1 {
		b = b[1:]
	}
	return string(b)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// position in S of the digit s places before the start of x; the numbers
// below 10^(d-1) take (d-1)·10^(d-1) - R(d-1) digits, where R(t) is the
// repunit of t ones, which leaves d·x + 1 - R(d) for x itself
func position(x string, s int) *big.Int {
	d := len(x)
	v, _ := new(big.Int).SetString(x, 10)
	r, _ := new(big.Int).SetString(strings.Repeat("1", d), 10)
	v.Mul(v, big.NewInt(int64(d)))
	v.Sub(v, r)
	return v.Add(v, big.NewInt(int64(1-s)))
}

// fits tells whether the number x can begin at position s of a, with its
// neighbours filling the rest of a on both sides
func fits(a string, s int, x string) bool {
	n := len(a)
	if a[s:min(n, s+len(x))] != x[:min(len(x), n-s)] {
		return false
	}
	pos, cur := s+len(x), x
	for pos < n {
		cur = inc(cur)
		if a[pos:min(n, pos+len(cur))] != cur[:min(len(cur), n-pos)] {
			return false
		}
		pos += len(cur)
	}
	pos, cur = s, x
	for pos > 0 {
		cur = dec(cur)
		if cur == "0" {
			return false
		}
		m := min(pos, len(cur))
		if a[pos-m:pos] != cur[len(cur)-m:] {
			return false
		}
		pos -= len(cur)
	}
	return true
}

func main() {
	var a string
	fmt.Scan(&a)
	n := len(a)
	// a inside one number, right after its first digit
	best := position("1"+a, -1)
	consider := func(s int, x string) {
		if fits(a, s, x) {
			if k := position(x, s); k.Cmp(best) < 0 {
				best = k
			}
		}
	}
	// some number lies in a completely
	for s := 0; s < n; s++ {
		if a[s] != '0' {
			for e := s + 1; e <= n; e++ {
				consider(s, a[s:e])
			}
		}
	}
	// a is the end of y - 1 followed by the beginning of y; the last i digits
	// of y are those of y - 1 plus one, and they may overlap the known
	// beginning by j digits
	for i := 1; i < n; i++ {
		if a[i] == '0' {
			continue
		}
		tail := inc(a[:i])
		tail = tail[len(tail)-i:]
		for j := 0; j <= min(n-i, i); j++ {
			if a[n-j:] == tail[:j] {
				consider(i, a[i:]+tail[j:])
			}
		}
	}
	fmt.Println(best.String())
}
