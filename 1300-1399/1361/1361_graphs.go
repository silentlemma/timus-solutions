package main

import (
	"bufio"
	"fmt"
	"os"
)

// visits: when the walk from start is at each node it reaches, the first
// moment (or -1 if never) and the period, 0 for a node passed only once.
func visits(step []int, start int) ([]int64, []int64) {
	n := len(step) - 1
	first, period := make([]int64, n+1), make([]int64, n+1)
	for i := range first {
		first[i] = -1
	}
	var order []int
	v := start
	for first[v] < 0 {
		first[v] = int64(len(order))
		order = append(order, v)
		v = step[v]
	}
	loopStart, length := first[v], int64(len(order))-first[v]
	for _, u := range order {
		if first[u] >= loopStart {
			period[u] = length
		}
	}
	return first, period
}

const bufferSize = 1 << 20 // the input can take a few megabytes

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// inverse: x with a x = 1 (mod m), for a and m coprime.
func inverse(a, m int64) int64 {
	g, x, x1, a1 := m, int64(0), int64(1), a%m
	for a1 != 0 {
		q := g / a1
		g, a1 = a1, g-q*a1
		x, x1 = x1, x-q*x1
	}
	return (x%m + m) % m
}

// firstCommon: the least moment in both sets r + k L (k >= 0), or -1.
func firstCommon(ra, la, rb, lb int64) int64 {
	if la == 0 && lb == 0 {
		if ra == rb {
			return ra
		}
		return -1
	}
	if la == 0 {
		ra, la, rb, lb = rb, lb, ra, la
	}
	if lb == 0 { // one moment rb against the moments ra, ra + la, ...
		if rb >= ra && (rb-ra)%la == 0 {
			return rb
		}
		return -1
	}
	g := gcd(la, lb)
	if (rb-ra)%g != 0 {
		return -1
	}
	m := lb / g
	k := int64(0)
	if m > 1 {
		diff := ((rb-ra)/g%m + m) % m
		k = diff * inverse(la/g%m, m) % m
	}
	t, whole := ra+la*k, la/g*lb
	if t < rb {
		t += (rb - t + whole - 1) / whole * whole
	}
	return t
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	readInt := func() int {
		n, c := 0, byte(0)
		for c, _ = in.ReadByte(); c == ' ' || c == '\n' || c == '\r'; c, _ = in.ReadByte() {
		}
		for ; c >= '0' && c <= '9'; c, _ = in.ReadByte() {
			n = n*10 + int(c-'0')
		}
		return n
	}
	n := readInt()
	left, right := make([]int, n+1), make([]int, n+1)
	for v := 1; v <= n; v++ {
		x := readInt()
		left[v] = x
		last := 0
		for x != 0 {
			last = x
			x = readInt()
		}
		right[v] = last
	}
	a, b := readInt(), readInt()
	// A always takes the leftmost road and B the rightmost
	firstA, periodA := visits(left, a)
	firstB, periodB := visits(right, b)
	best := int64(-1)
	for v := 1; v <= n; v++ {
		if firstA[v] < 0 || firstB[v] < 0 {
			continue
		}
		t := firstCommon(firstA[v], periodA[v], firstB[v], periodB[v])
		if t >= 0 && (best < 0 || t < best) {
			best = t
		}
	}
	fmt.Println(best)
}
