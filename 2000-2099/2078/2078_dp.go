package main

import (
	"fmt"
	"math"
)

const (
	frames = 10
	pins   = 10
	roll   = pins + 1 // a roll knocks down 0 to 10 pins
)

// table[x][y]: the least and the most points of the frames from the current
// one on, when the rolls from the current frame on start with x and y
type table [roll][roll][2]int

func empty() *table {
	t := new(table)
	for x := range t {
		for y := range t[x] {
			t[x][y] = [2]int{math.MaxInt32, math.MinInt32}
		}
	}
	return t
}

func (t *table) put(x, y, a, b int) {
	if a < t[x][y][0] {
		t[x][y][0] = a
	}
	if b > t[x][y][1] {
		t[x][y][1] = b
	}
}

func main() {
	var total [frames]int
	for i := range total {
		fmt.Scan(&total[i])
	}
	cur := empty()
	// rolls of the last frame: two, and a third one after a strike or a spare
	last := total[frames-1]
	for r1 := 0; r1 <= pins; r1++ {
		top := pins - r1
		if r1 == pins {
			top = pins
		}
		for r2 := 0; r2 <= top; r2++ {
			if r1 < pins && r1+r2 < pins {
				if r1+r2 == last {
					cur.put(r1, r2, last, last)
				}
				continue
			}
			cap3 := pins - r2
			if r1 < pins || r2 == pins {
				cap3 = pins
			}
			if r3 := last - r1 - r2; r3 >= 0 && r3 <= cap3 {
				cur.put(r1, r2, last, last)
			}
		}
	}
	for f := frames - 2; f >= 0; f-- {
		t := total[f]
		nxt := empty()
		for x := 0; x < roll; x++ {
			for y := 0; y < roll; y++ {
				if cur[x][y][0] == math.MaxInt32 {
					continue
				}
				a, b := cur[x][y][0]+t, cur[x][y][1]+t
				if t < pins {
					for r1 := 0; r1 <= t; r1++ {
						nxt.put(r1, t-r1, a, b)
					}
					continue
				}
				// a strike takes the next two rolls, a spare the next one
				nxt.put(pins, x, a+x+y, b+x+y)
				for r1 := 0; r1 < pins; r1++ {
					nxt.put(r1, pins-r1, a+x, b+x)
				}
			}
		}
		cur = nxt
	}
	lo, hi := math.MaxInt32, math.MinInt32
	for x := 0; x < roll; x++ {
		for y := 0; y < roll; y++ {
			if cur[x][y][0] < lo {
				lo = cur[x][y][0]
			}
			if cur[x][y][1] > hi {
				hi = cur[x][y][1]
			}
		}
	}
	fmt.Println(lo, hi)
}
