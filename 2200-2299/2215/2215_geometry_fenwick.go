package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const fullTurn = 4
const threeQuarters = fullTurn - 1

type point struct {
	x, y int64
}

type event struct {
	x, low, high int64
	index, sign  int
}

func prefix(tree []int, index int) int {
	sum := 0
	for index > 0 {
		sum += tree[index]
		index -= index & -index
	}
	return sum
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	points := make([]point, n)
	ys := make([]int64, n)
	for i := range points {
		fmt.Fscan(in, &points[i].x, &points[i].y)
		ys[i] = points[i].y
	}
	sort.Slice(points, func(i, j int) bool { return points[i].x < points[j].x })
	sort.Slice(ys, func(i, j int) bool { return ys[i] < ys[j] })
	size := 0
	for _, y := range ys {
		if size == 0 || ys[size-1] != y {
			ys[size] = y
			size++
		}
	}
	ys = ys[:size]
	var q, orientation int
	var tx, ty int64
	fmt.Fscan(in, &q)
	events := make([]event, 0, 2*q)
	answers := make([]int, 0, q)
	for ; q > 0; q-- {
		var command string
		var x, y int64
		fmt.Fscan(in, &command, &x, &y)
		if command != "ask" {
			turns := threeQuarters
			if command == "r90" {
				turns = 1
			} else if command == "r180" {
				turns = 2
			}
			dx, dy := tx-x, ty-y
			for step := 0; step < turns; step++ {
				dx, dy = -dy, dx
			}
			tx, ty = x+dx, y+dy
			orientation = (orientation + turns) % fullTurn
		} else {
			var xx, yy int64
			fmt.Fscan(in, &xx, &yy)
			x, y, xx, yy = x-tx, y-ty, xx-tx, yy-ty
			// Undo the global transform on two opposite corners.
			for step := 0; step < orientation; step++ {
				x, y, xx, yy = y, -x, yy, -xx
			}
			if x > xx {
				x, xx = xx, x
			}
			if y > yy {
				y, yy = yy, y
			}
			index := len(answers)
			answers = append(answers, 0)
			events = append(events, event{xx, y, yy, index, 1})
			events = append(events, event{x - 1, y, yy, index, -1})
		}
	}
	sort.Slice(events, func(i, j int) bool { return events[i].x < events[j].x })
	tree := make([]int, size+1)
	inserted := 0
	for _, e := range events {
		for inserted < n && points[inserted].x <= e.x {
			y := points[inserted].y
			index := sort.Search(size, func(i int) bool { return ys[i] >= y }) + 1
			for index <= size {
				tree[index]++
				index += index & -index
			}
			inserted++
		}
		low := sort.Search(size, func(i int) bool { return ys[i] >= e.low })
		high := sort.Search(size, func(i int) bool { return ys[i] > e.high })
		answers[e.index] += e.sign * (prefix(tree, high) - prefix(tree, low))
	}
	for _, answer := range answers {
		fmt.Fprintln(out, answer)
	}
}
