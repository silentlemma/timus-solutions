package main

import "fmt"

const (
	longest = 30
	base    = 10
)

var digits = []int{1, 2}

func main() {
	var n int
	fmt.Scan(&n)
	// breadth-first search over remainders: shorter numbers come first, and
	// within one length the queue keeps numeric order, so the first number
	// to reach a remainder is the smallest one with it
	parent := make([]int, n)
	digit := make([]int, n)
	length := make([]int, n)
	for i := range parent {
		parent[i] = -2
	}
	queue := make([]int, 0, n)
	for _, d := range digits {
		if r := d % n; parent[r] == -2 {
			parent[r], digit[r], length[r] = -1, d, 1
			queue = append(queue, r)
		}
	}
	for head := 0; head < len(queue) && parent[0] == -2; head++ {
		r := queue[head]
		if length[r] == longest {
			continue
		}
		for _, d := range digits {
			if s := (r*base + d) % n; parent[s] == -2 {
				parent[s], digit[s], length[s] = r, d, length[r]+1
				queue = append(queue, s)
			}
		}
	}
	if parent[0] == -2 {
		fmt.Println("Impossible")
		return
	}
	var out []byte
	for r := 0; r != -1; r = parent[r] {
		out = append(out, byte('0'+digit[r]))
	}
	for i, j := 0, len(out)-1; i < j; i, j = i+1, j-1 {
		out[i], out[j] = out[j], out[i]
	}
	fmt.Println(string(out))
}
