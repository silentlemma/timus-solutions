package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const far = 2 // eyes lie closer to PR than twice its length

// tan at P = height/near, at R = height/far
type eye struct{ height, near, far int64 }

func abs(v int64) int64 {
	if v < 0 {
		return -v
	}
	return v
}

type arc struct{ px, py, qx, qy, rx, ry int64 }

func faces(a arc, xs, ys []int64) int64 {
	px, py, qx, qy, rx, ry := a.px, a.py, a.qx, a.qy, a.rx, a.ry
	ux, uy := rx-px, ry-py
	side, span := ux*(qy-py)-uy*(qx-px), ux*ux+uy*uy
	var eyes []eye
	for i := range xs {
		cross := ux*(ys[i]-py) - uy*(xs[i]-px)
		near := ux*(xs[i]-px) + uy*(ys[i]-py)
		farR := -ux*(xs[i]-rx) - uy*(ys[i]-ry)
		// across PR from Q, both base angles acute, close enough to PR
		if cross == 0 || (cross > 0) == (side > 0) || near <= 0 || farR <= 0 ||
			abs(cross) >= far*span {
			continue
		}
		eyes = append(eyes, eye{abs(cross), near, farR})
	}
	k := len(eyes)
	atR := func(a, b int) bool {
		return eyes[a].height*eyes[b].far < eyes[b].height*eyes[a].far
	}
	atP := func(a, b int) bool {
		return eyes[a].height*eyes[b].near < eyes[b].height*eyes[a].near
	}
	// ranks of the angles at R, equal angles sharing a rank
	byR := make([]int, k)
	for i := range byR {
		byR[i] = i
	}
	sort.Slice(byR, func(i, j int) bool { return atR(byR[i], byR[j]) })
	rank := make([]int, k)
	r := 0
	for i := 0; i < k; i++ {
		if i > 0 && atR(byR[i-1], byR[i]) {
			r++
		}
		rank[byR[i]] = r + 1
	}
	// the line through two eyes misses PR exactly when one eye is seen
	// higher from P and lower from R: count pairs in opposite orders
	byP := make([]int, k)
	for i := range byP {
		byP[i] = i
	}
	sort.Slice(byP, func(i, j int) bool {
		a, b := byP[i], byP[j]
		if atP(a, b) {
			return true
		}
		if atP(b, a) {
			return false
		}
		return rank[a] < rank[b]
	})
	tree := make([]int, k+1)
	var pairs int64
	for seen := 0; seen < k; seen++ {
		r := rank[byP[seen]]
		below := 0
		for i := r; i > 0; i &= i - 1 {
			below += tree[i]
		}
		pairs += int64(seen - below)
		for i := r; i <= k; i += i & -i {
			tree[i]++
		}
	}
	return pairs
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	if _, err := fmt.Fscan(in, &n, &m); err != nil {
		return
	}
	arcs := make([]arc, n)
	for i := range arcs {
		a := &arcs[i]
		fmt.Fscan(in, &a.px, &a.py, &a.qx, &a.qy, &a.rx, &a.ry)
	}
	xs, ys := make([]int64, m), make([]int64, m)
	for i := 0; i < m; i++ {
		fmt.Fscan(in, &xs[i], &ys[i])
	}
	var total int64
	for _, a := range arcs {
		total += faces(a, xs, ys)
	}
	fmt.Println(total)
}
