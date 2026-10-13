package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const nine = 9
const classes = 4                             // positions grouped by the signs of the two rules
const bothUp, xUp, yUp, bothDown = 0, 1, 2, 3 // the four classes by sign

var s []int
var size int

type combo struct {
	wx, wy, cls, tail []int // tail[k]: sum of wx from k on
	cnt               [classes][]int
	px, py            []int
}

func newCombo(wx, wy []int) *combo {
	c := &combo{wx: wx, wy: wy, cls: make([]int, size), tail: make([]int, size+1)}
	for k := range c.cnt {
		c.cnt[k] = make([]int, size+1)
	}
	c.px, c.py = make([]int, size+1), make([]int, size+1)
	for k := 0; k < size; k++ {
		c.cls[k] = 0
		if wx[k] < 0 {
			c.cls[k] += 2
		}
		if wy[k] < 0 {
			c.cls[k]++
		}
		for q := 0; q < classes; q++ {
			c.cnt[q][k+1] = c.cnt[q][k]
		}
		c.cnt[c.cls[k]][k+1]++
		c.px[k+1] = c.px[k] + wx[k]*s[k]
		c.py[k+1] = c.py[k] + wy[k]*s[k]
	}
	for k := size - 1; k >= 0; k-- {
		c.tail[k] = c.tail[k+1] + wx[k]
	}
	return c
}

// feasible: digits before j give sums sx, sy; j in [loJ, hiJ], free up to p,
// p at most 8, nines after p; t must balance wx, t + 1 must balance wy.
func (c *combo) feasible(sx, sy, j, p, loJ, hiJ int) bool {
	a, b := -sx-nine*c.tail[p+1], -sy-c.wy[p]
	var lo, hi [classes]int
	for q := 0; q < classes; q++ {
		hi[q] = nine * (c.cnt[q][p+1] - c.cnt[q][j])
	}
	hi[c.cls[j]] += hiJ - nine
	lo[c.cls[j]] += loJ
	if p > j {
		hi[c.cls[p]]--
	}
	if (a+b)%2 != 0 {
		return false
	}
	u, v := (a+b)/2, (a-b)/2
	return lo[bothUp]-hi[bothDown] <= u && u <= hi[bothUp]-lo[bothDown] &&
		lo[xUp]-hi[yUp] <= v && v <= hi[xUp]-lo[yUp]
}

// build: t from s up to j, then d, then the smallest digits that still fit, then nines after p.
func (c *combo) build(p, j, d int) []int {
	t := append([]int(nil), s[:j]...)
	if j > p { // t keeps s up to p and has nines after it
		t = append([]int(nil), s[:p+1]...)
	} else {
		sx, sy := c.px[j]+c.wx[j]*d, c.py[j]+c.wy[j]*d
		t = append(t, d)
		for k := j + 1; k <= p; k++ {
			x := 0
			for !c.feasible(sx, sy, k, p, x, x) {
				x++
			}
			t = append(t, x)
			sx += c.wx[k] * x
			sy += c.wy[k] * x
		}
	}
	for len(t) < size {
		t = append(t, nine)
	}
	return t
}

func less(a, b []int) bool {
	for k := range a {
		if a[k] != b[k] {
			return a[k] < b[k]
		}
	}
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var line string
	fmt.Fscan(in, &line)
	line = strings.TrimSpace(line)
	size = len(line)
	s = make([]int, size)
	for k := range s {
		s[k] = int(line[k] - '0')
	}
	half := size / 2
	ruleA, ruleB := make([]int, size), make([]int, size)
	for k := 0; k < size; k++ {
		ruleA[k], ruleB[k] = 1, 1
		if k >= half {
			ruleA[k] = -1
		}
		if k%2 == 1 {
			ruleB[k] = -1
		}
	}
	rules := [][]int{ruleA, ruleB}
	// best: the first position where t leaves s (later is better), then the digit there
	bestDev, bestDigit := -1, nine+1
	var best []int
	for _, x := range rules {
		for _, y := range rules { // the rule for t, then the rule for t + 1
			c := newCombo(x, y)
			for p := 0; p < size; p++ {
				dev, digit, j, d := -1, 0, -1, 0
				if s[p] < nine && c.px[p+1]+nine*c.tail[p+1] == 0 && c.py[p+1]+c.wy[p] == 0 {
					dev = size
					for k := p + 1; k < size; k++ {
						if s[k] < nine {
							dev = k
							break
						}
					}
					digit, j = nine, p+1
				} else {
					for q := p; q >= 0 && dev < 0; q-- {
						top := nine
						if q == p {
							top = nine - 1
						}
						if s[q]+1 > top || !c.feasible(c.px[q], c.py[q], q, p, s[q]+1, top) {
							continue
						}
						d = s[q] + 1
						for !c.feasible(c.px[q], c.py[q], q, p, d, d) {
							d++
						}
						dev, j, digit = q, q, d
					}
				}
				if dev < 0 || dev < bestDev || (dev == bestDev && digit > bestDigit) {
					continue
				}
				t := c.build(p, j, d)
				if best == nil || dev > bestDev || digit < bestDigit || less(t, best) {
					best, bestDev, bestDigit = t, dev, digit
				}
			}
		}
	}
	if best == nil {
		fmt.Println("No solution")
		return
	}
	next := append([]int(nil), best...)
	k := size - 1
	for next[k] == nine {
		next[k] = 0
		k--
	}
	next[k]++
	var a, b strings.Builder
	for i := range best {
		a.WriteByte(byte('0' + best[i]))
		b.WriteByte(byte('0' + next[i]))
	}
	fmt.Println(a.String(), b.String())
}
