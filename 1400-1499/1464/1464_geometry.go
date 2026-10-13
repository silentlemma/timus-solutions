package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	digits = 4 // coordinates are given to four decimals
	scale  = 1e4
	bits   = 64
	buffer = 1 << 20
)

// a coordinate times 10^4, read exactly
func exact(text string) int64 {
	sign := int64(1)
	if strings.HasPrefix(text, "-") {
		sign, text = -1, text[1:]
	}
	whole, frac := text, ""
	if dot := strings.IndexByte(text, '.'); dot >= 0 {
		whole, frac = text[:dot], text[dot+1:]
	}
	frac = (frac + strings.Repeat("0", digits))[:digits]
	w, _ := strconv.ParseInt("0"+whole, 10, bits)
	f, _ := strconv.ParseInt(frac, 10, bits)
	return sign * (w*scale + f)
}

var num, ex, ey, midX, midY []float64
var best, first []int
var size int

// how far along the middle ray of gap k the line of edge e lies
func distance(e, k int) float64 { return num[e] / (midX[k]*ey[e] - midY[k]*ex[e]) }

// each node keeps the nearest edge among those covering all its gaps,
// and edges never cross, so one gap decides for the whole node
func offer(x, e int) {
	if best[x] < 0 || distance(e, first[x]) < distance(best[x], first[x]) {
		best[x] = e
	}
}

func cover(lo, hi, e int) {
	for lo, hi = lo+size, hi+size; lo < hi; lo, hi = lo>>1, hi>>1 {
		if lo&1 == 1 {
			offer(lo, e)
			lo++
		}
		if hi&1 == 1 {
			hi--
			offer(hi, e)
		}
	}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, buffer)
	word := func() string {
		var s string
		fmt.Fscan(reader, &s)
		return s
	}
	px, py := exact(word()), exact(word())
	n, _ := strconv.Atoi(word())
	xs, ys := make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		xs[i], ys[i] = exact(word())-px, exact(word())-py
	}
	// the directions of the corners seen from the lamp, equal ones merged
	order := make([]int, n)
	angle := make([]float64, n)
	for i := range order {
		order[i] = i
		angle[i] = math.Atan2(float64(ys[i]), float64(xs[i]))
	}
	sort.Slice(order, func(a, b int) bool { return angle[order[a]] < angle[order[b]] })
	group := make([]int, n)
	var dx, dy []int64
	for _, i := range order {
		k := len(dx) - 1
		same := k >= 0 && xs[i]*dy[k] == ys[i]*dx[k] && xs[i]*dx[k]+ys[i]*dy[k] > 0
		if !same {
			dx, dy = append(dx, xs[i]), append(dy, ys[i])
		}
		group[i] = len(dx) - 1
	}
	m := len(dx)
	// every gap between neighbouring directions is below half a turn; its middle
	midX, midY = make([]float64, m), make([]float64, m)
	for k := 0; k < m; k++ {
		l := (k + 1) % m
		la := math.Hypot(float64(dx[k]), float64(dy[k]))
		lb := math.Hypot(float64(dx[l]), float64(dy[l]))
		midX[k] = float64(dx[k])/la + float64(dx[l])/lb
		midY[k] = float64(dy[k])/la + float64(dy[l])/lb
	}
	for size = 1; size < m; size *= 2 {
	}
	first, best = make([]int, 2*size), make([]int, 2*size)
	for x := 2*size - 1; x > 0; x-- {
		best[x] = -1
		if x >= size {
			first[x] = x - size
		} else {
			first[x] = first[2*x]
		}
	}
	for i := 0; i < n; i++ {
		j := (i + 1) % n
		c := xs[i]*ys[j] - ys[i]*xs[j]
		if c == 0 {
			continue // seen edge-on, it hides nothing
		}
		a, b := i, j
		if c < 0 {
			a, b = j, i
		}
		e := len(num)
		num = append(num, float64(xs[a]*(ys[b]-ys[a])-ys[a]*(xs[b]-xs[a])))
		ex = append(ex, float64(xs[b]-xs[a]))
		ey = append(ey, float64(ys[b]-ys[a]))
		if group[a] < group[b] {
			cover(group[a], group[b], e)
		} else {
			cover(group[a], m, e)
			cover(0, group[b], e)
		}
	}
	area := 0.0
	for k := 0; k < m; k++ {
		near := -1
		for x := k + size; x > 0; x >>= 1 {
			if best[x] >= 0 && (near < 0 || distance(best[x], k) < distance(near, k)) {
				near = best[x]
			}
		}
		l := (k + 1) % m
		ta := num[near] / (float64(dx[k])*ey[near] - float64(dy[k])*ex[near])
		tb := num[near] / (float64(dx[l])*ey[near] - float64(dy[l])*ex[near])
		area += ta * tb * (float64(dx[k])*float64(dy[l]) - float64(dy[k])*float64(dx[l])) / 2
	}
	fmt.Printf("%.4f\n", area/scale/scale)
}
