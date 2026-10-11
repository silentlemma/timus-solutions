package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var w, h, x, y, d int
	fmt.Fscan(in, &w, &h, &x, &y, &d)
	open := make([]bool, w*h)
	wet := make([]bool, w*h)
	for r := 0; r < h; r++ {
		var row string
		fmt.Fscan(in, &row)
		for c := 0; c < w; c++ {
			open[r*w+c] = row[c] != '#'
		}
	}
	// water reaches a cell that has a way to the surface without going down,
	// so search back from the top row: down, left and right
	var stack []int
	for c := 0; c < w; c++ {
		if open[c] {
			wet[c] = true
			stack = append(stack, c)
		}
	}
	for len(stack) > 0 {
		cell := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		r, c := cell/w, cell%w
		for _, n := range []int{iff(r+1 < h, cell+w), iff(c > 0, cell-1), iff(c+1 < w, cell+1)} {
			if n >= 0 && open[n] && !wet[n] {
				wet[n] = true
				stack = append(stack, n)
			}
		}
	}
	// label: moves made under water since the last breath; an air pocket
	// resets it to 0, and no stretch under water may take more than D moves
	start := (h-y)*w + (x - 1)
	label := make([]int, w*h)
	for i := range label {
		label[i] = d + 1
	}
	buckets := make([][]int, d+1)
	label[start] = 0
	buckets[0] = append(buckets[0], start)
	for level := 0; level <= d; {
		if len(buckets[level]) == 0 {
			level++
			continue
		}
		cell := buckets[level][len(buckets[level])-1]
		buckets[level] = buckets[level][:len(buckets[level])-1]
		here := label[cell]
		if here != level {
			continue
		}
		r, c := cell/w, cell%w
		if r == 0 && here+1 <= d {
			fmt.Println("Can be rescued by himself")
			return
		}
		next := []int{
			iff(r > 0, cell-w), iff(r+1 < h, cell+w), iff(c > 0, cell-1), iff(c+1 < w, cell+1),
		}
		for _, n := range next {
			if n < 0 || !open[n] {
				continue
			}
			nl := 0
			if wet[n] {
				nl = here + 1
			} else if wet[cell] && here+1 > d {
				continue
			}
			if nl <= d && nl < label[n] {
				label[n] = nl
				buckets[nl] = append(buckets[nl], n)
				if nl < level {
					level = nl
				}
			}
		}
	}
	fmt.Println("Rescue operation required")
}

// iff gives the cell when it lies inside the cave and -1 otherwise
func iff(inside bool, cell int) int {
	if inside {
		return cell
	}
	return -1
}
