package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var ends = []int{1, 2} // the first and last rows of a best shape are this narrow

// no k cells have fewer than sqrt(scale k - shift) + 2 neighbours
const (
	scale = 8
	shift = 4
)

func isqrt(n int64) int64 {
	r := int64(math.Sqrt(float64(n)))
	for r*r > n {
		r--
	}
	for (r+1)*(r+1) <= n {
		r++
	}
	return r
}

func capped(full []int, c int) int64 {
	total := int64(0)
	for _, w := range full {
		if w < c {
			total += int64(w)
		} else {
			total += int64(c)
		}
	}
	return total
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// widthsFor: row widths of a region of k cells with the smallest fence. With
// row ends moving by at most one cell per row the fence is two cells per row
// plus the first and the last row, and none is smaller than sqrt(8 k - 4) + 2.
func widthsFor(k int64) []int {
	for fence := int(isqrt(scale*k-shift-1)) + 1 + 2; ; fence++ {
		for _, first := range ends {
			for _, last := range ends {
				twice := fence - first - last
				rows := twice / 2
				if twice%2 != 0 || rows < 1 {
					continue
				}
				var full []int
				if rows == 1 {
					if first == last {
						full = []int{first}
					}
				} else {
					for i := 0; i < rows; i++ {
						full = append(full, min(first+2*i, last+2*(rows-1-i)))
					}
				}
				widest := 0
				for _, w := range full {
					if w > widest {
						widest = w
					}
				}
				if len(full) == 0 || capped(full, widest) < k {
					continue
				}
				// cap the widest rows at the smallest level that holds k cells
				low := full[0]
				if full[len(full)-1] > low {
					low = full[len(full)-1]
				}
				lo, hi := low, widest
				for lo < hi {
					mid := (lo + hi) / 2
					if capped(full, mid) < k {
						lo = mid + 1
					} else {
						hi = mid
					}
				}
				c := lo
				widths := make([]int, rows)
				for i, w := range full {
					widths[i] = min(w, c)
				}
				extra := int(capped(full, c) - k)
				var inner []int
				for i := 1; i+1 < rows; i++ {
					if widths[i] == c {
						inner = append(inner, i)
					}
				}
				if c > low && extra <= len(inner) {
					for _, i := range inner[:extra] {
						widths[i]--
					}
					return widths
				}
				if extra == 0 {
					return widths
				}
			}
		}
	}
}

func main() {
	var k int64
	fmt.Scan(&k)
	widths := widthsFor(k)
	// place the rows from y = 0 up, the first one starting at x = 0; the ends
	// move by at most one cell, the left one first when the row narrows
	left, right := []int{0}, []int{widths[0] - 1}
	for _, w := range widths[1:] {
		grow := w - (right[len(right)-1] - left[len(left)-1] + 1)
		dl := 0
		if grow == 2 {
			dl = -1
		} else if grow < 0 {
			dl = 1
		}
		left = append(left, left[len(left)-1]+dl)
		right = append(right, left[len(left)-1]+w-1)
	}
	top := len(widths) - 1
	var fence [][2]int
	for x := left[0]; x <= right[0]; x++ {
		fence = append(fence, [2]int{x, -1})
	}
	for y := 0; y <= top; y++ {
		fence = append(fence, [2]int{right[y] + 1, y})
	}
	for x := right[top]; x >= left[top]; x-- {
		fence = append(fence, [2]int{x, top + 1})
	}
	for y := top; y >= 0; y-- {
		fence = append(fence, [2]int{left[y] - 1, y})
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(fence))
	for _, c := range fence {
		fmt.Fprintln(out, c[0], c[1])
	}
}
