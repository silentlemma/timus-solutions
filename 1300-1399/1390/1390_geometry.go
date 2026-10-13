package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const digits = 1000000000 // the time is printed with nine digits after the point
const wall = 4            // numbers that describe a wall
const treeFactor = 4      // a segment tree over n leaves has under 4 n nodes

type dir struct{ x, y int64 }

func gcd(a, b int64) int64 {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func reduced(x, y int64) dir {
	g := gcd(x, y)
	return dir{x / g, y / g}
}

// before: counterclockwise order of directions, starting from the positive x axis.
func before(a, b dir) bool {
	ha, hb := a.y < 0 || (a.y == 0 && a.x < 0), b.y < 0 || (b.y == 0 && b.x < 0)
	if ha != hb {
		return hb
	}
	return a.x*b.y-a.y*b.x > 0
}

var leaves []dir

// a wall is the line nx x + ny y = c with c > 0: a shot v hits it at time c / (n . v)
var nx, ny, cs []int64
var tree []int

func better(w, u, leaf int) bool {
	vx, vy := leaves[leaf].x, leaves[leaf].y
	return (nx[w]*vx+ny[w]*vy)*cs[u] > (nx[u]*vx+ny[u]*vy)*cs[w]
}

// push: Li Chao insertion; two walls swap places at most once on an arc below pi.
func push(node, lo, hi, w int) {
	for {
		if tree[node] < 0 {
			tree[node] = w
			return
		}
		mid := (lo + hi) / 2
		if better(w, tree[node], mid) {
			w, tree[node] = tree[node], w
		}
		if lo == hi {
			return
		}
		if better(w, tree[node], lo) {
			node, hi = 2*node, mid
		} else if better(w, tree[node], hi) {
			node, lo = 2*node+1, mid+1
		} else {
			return
		}
	}
}

func insert(node, lo, hi, left, right, w int) {
	if right < lo || hi < left {
		return
	}
	if left <= lo && hi <= right {
		push(node, lo, hi, w)
		return
	}
	mid := (lo + hi) / 2
	insert(2*node, lo, mid, left, right, w)
	insert(2*node+1, mid+1, hi, left, right, w)
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	num := func() int64 {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return int64(v)
	}
	var events [][]int64
	for sc.Scan() && sc.Text() != "end" {
		count := wall
		if sc.Text() == "shot" {
			count = 2
		}
		e := make([]int64, count)
		for i := range e {
			e[i] = num()
		}
		events = append(events, e)
	}
	// the leaves: distinct shot directions by angle
	for _, e := range events {
		if len(e) == 2 {
			leaves = append(leaves, reduced(e[0], e[1]))
		}
	}
	sort.Slice(leaves, func(i, j int) bool { return before(leaves[i], leaves[j]) })
	unique := leaves[:0]
	for _, d := range leaves {
		if len(unique) == 0 || unique[len(unique)-1] != d {
			unique = append(unique, d)
		}
	}
	leaves = unique
	size := len(leaves)
	if size == 0 {
		size = 1
	}
	tree = make([]int, treeFactor*size)
	for i := range tree {
		tree[i] = -1
	}
	lowerBound := func(d dir) int {
		return sort.Search(len(leaves), func(i int) bool { return !before(leaves[i], d) })
	}
	upperBound := func(d dir) int {
		return sort.Search(len(leaves), func(i int) bool { return before(d, leaves[i]) })
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, e := range events {
		if len(e) == wall {
			if len(leaves) == 0 {
				continue // no shots at all
			}
			x1, y1, x2, y2 := e[0], e[1], e[2], e[wall-1]
			if x1*y2-y1*x2 < 0 {
				x1, y1, x2, y2 = x2, y2, x1, y1
			}
			a, b := y2-y1, x1-x2
			nx, ny, cs = append(nx, a), append(ny, b), append(cs, a*x1+b*y1)
			w := len(cs) - 1
			// the wall covers the directions from its first end counterclockwise to the second
			first, last := reduced(x1, y1), reduced(x2, y2)
			lo, hi := lowerBound(first), upperBound(last)-1
			if before(first, last) {
				insert(1, 0, size-1, lo, hi, w)
			} else {
				insert(1, 0, size-1, lo, size-1, w)
				insert(1, 0, size-1, 0, hi, w)
			}
			continue
		}
		vx, vy := e[0], e[1]
		leaf := lowerBound(reduced(vx, vy))
		node, lo, hi, best := 1, 0, size-1, -1
		for {
			cur := tree[node]
			if cur >= 0 && (best < 0 || better(cur, best, leaf)) {
				best = cur
			}
			if lo == hi {
				break
			}
			mid := (lo + hi) / 2
			if leaf <= mid {
				node, hi = 2*node, mid
			} else {
				node, lo = 2*node+1, mid+1
			}
		}
		if best < 0 {
			fmt.Fprintln(out, "Infinite")
		} else {
			den := nx[best]*vx + ny[best]*vy
			q := (2*cs[best]*digits + den) / (2 * den)
			fmt.Fprintf(out, "%d.%09d\n", q/digits, q%digits)
		}
	}
}
