package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

var colors = []string{"VIOLET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"}

const red = 6
const perDecade = 5 // a level per 2 dB: five levels per tenfold distance
const ten = 10
const eps = 1e-9 // events closer than this in segment time happen together
const tie = 1e-9 // powers closer than this relative gap are equal

var n int
var xs, ys, rs []float64
var names []string
var bounds [][]float64 // squared radii where the level steps up
var sx, sy, dx, dy, len2 float64

type point struct{ x, y float64 }

type event struct {
	t       float64
	station int
}

func level(i int, px, py float64) int {
	d2 := (px-xs[i])*(px-xs[i]) + (py-ys[i])*(py-ys[i])
	l := 0
	for _, b := range bounds[i] {
		if d2 > b {
			l++
		}
	}
	return l
}

// best: the strongest station at (px, py); equal powers go to the smaller name.
func best(cands []int, px, py float64) int {
	top := cands[0]
	for _, i := range cands[1:] {
		// power is r / d: compare r_i * d_top with r_top * d_i
		a := rs[i] * math.Hypot(px-xs[top], py-ys[top])
		b := rs[top] * math.Hypot(px-xs[i], py-ys[i])
		if a > b*(1+tie) || (math.Abs(a-b) <= tie*math.Max(a, b) && names[i] < names[top]) {
			top = i
		}
	}
	return top
}

// roots: the times in (0, 1) where the distance to station i squared is rad2.
func roots(i int, rad2 float64, out []float64) []float64 {
	px, py := sx-xs[i], sy-ys[i]
	b, c := dx*px+dy*py, px*px+py*py-rad2
	disc := b*b - len2*c
	if disc <= 0 {
		return out
	}
	q := -(b + math.Copysign(math.Sqrt(disc), b))
	for _, t := range []float64{q / len2, c / q} {
		if t > 0 && t < 1 {
			out = append(out, t)
		}
	}
	return out
}

// levelAfter: the level of station i just after time t, before its own next change.
func levelAfter(i int, t float64) int {
	var ts []float64
	for _, b := range bounds[i] {
		ts = roots(i, b, ts)
	}
	next := 1.0
	for _, u := range ts {
		if u > t+eps && u < next {
			next = u
		}
	}
	u := (t + next) / 2
	return level(i, sx+dx*u, sy+dy*u)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fscan(in, &n)
	xs, ys, rs = make([]float64, n), make([]float64, n), make([]float64, n)
	names, bounds = make([]string, n), make([][]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &xs[i], &ys[i], &rs[i], &names[i])
		for k := 0; k < red; k++ {
			r := rs[i] * math.Pow(ten, float64(k)/perDecade)
			bounds[i] = append(bounds[i], r*r)
		}
	}
	var m int
	fmt.Fscan(in, &m)
	from, to := make([]point, m), make([]point, m) // the ends of each segment
	for j := 0; j < m; j++ {
		fmt.Fscan(in, &from[j].x, &from[j].y, &to[j].x, &to[j].y)
	}
	all := make([]int, n)
	for i := range all {
		all[i] = i
	}
	cur := best(all, from[0].x, from[0].y)
	lev := level(cur, from[0].x, from[0].y)
	fmt.Fprintf(out, "Power on. CELL_ID:%s, SIGNAL_LEVEL:%s\n", names[cur], colors[lev])

	for j := 0; j < m; j++ {
		sx, sy, dx, dy = from[j].x, from[j].y, to[j].x-from[j].x, to[j].y-from[j].y
		len2 = dx*dx + dy*dy
		if len2 == 0 {
			continue
		}
		// red and not red switch only on the outer circles
		var reds []event
		for i := 0; i < n; i++ {
			for _, t := range roots(i, bounds[i][red-1], nil) {
				reds = append(reds, event{t, i})
			}
		}
		timeline := func(after float64) []event {
			var events []event
			var ts []float64
			for _, b := range bounds[cur] {
				ts = roots(cur, b, ts)
			}
			for _, t := range ts {
				if t > after {
					events = append(events, event{t, -1})
				}
			}
			for _, e := range reds {
				if e.t > after {
					events = append(events, e)
				}
			}
			sort.Slice(events, func(a, b int) bool {
				if events[a].t != events[b].t {
					return events[a].t < events[b].t
				}
				return events[a].station < events[b].station
			})
			return events
		}
		events := timeline(-1)
		k := 0
		for k < len(events) {
			t0 := events[k].t
			var group []int
			for k < len(events) && events[k].t-t0 <= eps {
				group = append(group, events[k].station)
				k++
			}
			// the state right after the group holds until the next event
			tend := events[k-1].t
			t1 := 1.0
			if k < len(events) {
				t1 = events[k].t
			}
			mx, my := sx+dx*(t0+t1)/2, sy+dy*(t0+t1)/2
			px, py := sx+dx*t0, sy+dy*t0
			searching := false
			var cands []int
			if lev != red {
				now := level(cur, mx, my)
				if now != lev {
					lev = now
					fmt.Fprintf(out, "Signal changed. SIGNAL_LEVEL:%s\n", colors[lev])
					if lev == red {
						searching = true
						for i := 0; i < n; i++ {
							if level(i, mx, my) < red {
								cands = append(cands, i)
							}
						}
					}
				}
			} else {
				searching = true
				for _, i := range group {
					if i >= 0 && level(i, mx, my) < red {
						cands = append(cands, i)
					}
				}
			}
			if !searching || len(cands) == 0 {
				continue
			}
			pick := best(cands, px, py)
			lev = levelAfter(pick, tend)
			if pick == cur {
				fmt.Fprintf(out, "Signal changed. SIGNAL_LEVEL:%s\n", colors[lev])
			} else {
				cur = pick
				fmt.Fprintf(out, "Cell changed. CELL_ID:%s, SIGNAL_LEVEL:%s\n", names[cur], colors[lev])
				events = timeline(tend + eps)
				k = 0
			}
		}
	}
}
