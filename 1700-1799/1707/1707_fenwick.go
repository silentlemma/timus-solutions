package main

import (
	"bufio"
	"os"
	"strconv"
)

const mod = 200904040963 // the modulus of the hash printed for long experiments
const base = 7
const short = 20 // experiments up to this length are printed digit by digit
const corners = 4
const opposite = 3 // the corner (a - 1, c - 1) among the four of a step
const bufferSize = 1 << 20
const wordBits = 64

func wrap(v int64, n int) int {
	r := int(v % int64(n))
	if r < 0 {
		r += n
	}
	return r
}

type ask struct{ x, id int }

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, bufferSize), bufferSize)
	scanner.Split(bufio.ScanWords)
	next := func() int64 {
		scanner.Scan()
		v, _ := strconv.ParseInt(scanner.Text(), 10, wordBits)
		return v
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	n, m := int(next()), int(next())
	// the eyes' states are points (s, t); an experiment step asks whether a
	// rectangle holds one, answered by four prefix counts of a sweep over t
	xsByY := make([][]int, n)
	for l := 0; l < m; l++ {
		s0, t0, ds, dt, k := next(), next(), next(), next(), next()
		for i := int64(0); i < k; i++ {
			y := wrap(t0+i*dt, n)
			xsByY[y] = append(xsByY[y], wrap(s0+i*ds, n))
		}
	}
	p := int(next())
	asksByY := make([][]ask, n)
	// count 0 is a fixed zero for the corners outside the grid
	count := 1
	lengths := make([]int, p)
	cornerIds := make([][]int, p)
	for e := 0; e < p; e++ {
		a0, b0, c0, d0 := next(), next(), next(), next()
		da, db, dc, dd := next(), next(), next(), next()
		q := int(next())
		lengths[e] = q
		for j := int64(0); j < int64(q); j++ {
			a, b := wrap(a0+j*da, n), wrap(b0+j*db, n)
			c, d := wrap(c0+j*dc, n), wrap(d0+j*dd, n)
			if a > b {
				a, b = b, a
			}
			if c > d {
				c, d = d, c
			}
			xs := [corners]int{b, a - 1, b, a - 1}
			ys := [corners]int{d, d, c - 1, c - 1}
			for r := 0; r < corners; r++ {
				if xs[r] < 0 || ys[r] < 0 {
					cornerIds[e] = append(cornerIds[e], 0)
				} else {
					asksByY[ys[r]] = append(asksByY[ys[r]], ask{xs[r], count})
					cornerIds[e] = append(cornerIds[e], count)
					count++
				}
			}
		}
	}
	below := make([]int, count) // points with s <= x and t <= y for each asked corner
	tree := make([]int, n+1)
	for y := 0; y < n; y++ {
		for _, x := range xsByY[y] {
			for i := x + 1; i <= n; i += i & -i {
				tree[i]++
			}
		}
		for _, a := range asksByY[y] {
			total := 0
			for i := a.x + 1; i > 0; i -= i & -i {
				total += tree[i]
			}
			below[a.id] = total
		}
	}
	for e := 0; e < p; e++ {
		c := cornerIds[e]
		bits := make([]byte, lengths[e])
		for j := range bits {
			r := j * corners
			if below[c[r]]-below[c[r+1]]-below[c[r+2]]+below[c[r+opposite]] > 0 {
				bits[j] = '1'
			} else {
				bits[j] = '0'
			}
		}
		if lengths[e] <= short {
			writer.Write(bits)
		} else {
			var value int64
			for j := len(bits) - 1; j >= 0; j-- {
				value = (value*base + int64(bits[j]-'0')) % mod
			}
			writer.WriteString(strconv.FormatInt(value, 10))
		}
		writer.WriteString("\n")
	}
}
