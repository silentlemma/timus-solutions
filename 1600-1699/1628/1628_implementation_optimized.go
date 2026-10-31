package main

import (
	"fmt"
	"os"
	"sort"
)

const inputBuffer = 4096

// refills bound storage even when whitespace or tokens cross a buffer boundary.
type reader struct {
	buffer   [inputBuffer]byte
	at, size int
}

func (r *reader) read() byte {
	if r.at == r.size {
		r.size, _ = os.Stdin.Read(r.buffer[:])
		r.at = 0
		if r.size == 0 {
			return 0
		}
	}
	c := r.buffer[r.at]
	r.at++
	return c
}
func (r *reader) next() int {
	c := r.read()
	for c != 0 && c != '-' && (c < '0' || c > '9') {
		c = r.read()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = r.read()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = r.read()
	}
	return sign * value
}

func main() {
	in := reader{}
	m, n, k := in.next(), in.next(), in.next()
	stride, columnStride := n+2, m+2
	// row-major keys replace coordinate maps and thousands of small allocations.
	rows, columns := make([]int, k), make([]int, k)
	for i := range rows {
		x, y := in.next(), in.next()
		rows[i] = x*stride + y
		columns[i] = y*columnStride + x
	}
	sort.Ints(rows)
	sort.Ints(columns)
	contains := func(key int) bool {
		at := sort.SearchInts(rows, key)
		return at < k && rows[at] == key
	}
	answer, at := 0, 0
	for x := 1; x <= m; x++ {
		previous := 0
		for {
			next := n + 1
			if at < k && rows[at]/stride == x {
				next = rows[at] % stride
				at++
			}
			length, cell := next-previous-1, x*stride+previous+1
			if length >= 2 || (length == 1 &&
				(x == 1 || contains(cell-stride)) && (x == m || contains(cell+stride))) {
				answer++
			}
			if next == n+1 {
				break
			}
			previous = next
		}
	}
	at = 0
	for y := 1; y <= n; y++ {
		previous := 0
		for {
			next := m + 1
			if at < k && columns[at]/columnStride == y {
				next = columns[at] % columnStride
				at++
			}
			if next-previous-1 >= 2 {
				answer++
			}
			if next == m+1 {
				break
			}
			previous = next
		}
	}
	fmt.Println(answer)
}
