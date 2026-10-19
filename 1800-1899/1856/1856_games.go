package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	spell := [2][]int{make([]int, n), make([]int, n)}
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &spell[0][i], &spell[1][i])
		spell[0][i]--
		spell[1][i]--
	}
	// the army gathers exactly when every pair of garrisons can be forced
	// together, one pair after another; a pair (u, v), u < v, is the number
	// u * n + v, and a day is her spell m, then his spell k
	size := n * n
	openMoves := make([]uint8, 2*size) // his replies that keep the pair apart
	var target, source []int32         // pair after both spells, pair * 2 + her spell
	for u := 0; u < n; u++ {
		for v := u + 1; v < n; v++ {
			p := u*n + v
			for mine := 0; mine < 2; mine++ {
				x, y := spell[mine][u], spell[mine][v]
				if x == y {
					continue
				}
				for k := 0; k < 2; k++ {
					s, t := spell[k][x], spell[k][y]
					if s == t {
						continue
					}
					if s > t {
						s, t = t, s
					}
					target = append(target, int32(s*n+t))
					source = append(source, int32(2*p+mine))
					openMoves[2*p+mine]++
				}
			}
		}
	}
	// the replies that lead into every pair, grouped by that pair
	start := make([]int32, size+1)
	for _, q := range target {
		start[q+1]++
	}
	for q := 0; q < size; q++ {
		start[q+1] += start[q]
	}
	place := append([]int32(nil), start[:size]...)
	from := make([]int32, len(target))
	for i, q := range target {
		from[place[q]] = source[i]
		place[q]++
	}
	// a pair is won when some spell of hers leaves him no reply that keeps
	// the pair apart outside the won pairs
	won := make([]bool, size)
	var queue []int32
	for u := 0; u < n; u++ {
		for v := u + 1; v < n; v++ {
			p := u*n + v
			if openMoves[2*p] == 0 || openMoves[2*p+1] == 0 {
				won[p] = true
				queue = append(queue, int32(p))
			}
		}
	}
	for h := 0; h < len(queue); h++ {
		q := queue[h]
		for e := start[q]; e < start[q+1]; e++ {
			move := from[e]
			p := move >> 1
			if won[p] {
				continue
			}
			openMoves[move]--
			if openMoves[move] == 0 {
				won[p] = true
				queue = append(queue, p)
			}
		}
	}
	if len(queue) == n*(n-1)/2 {
		fmt.Println("War")
	} else {
		fmt.Println("Peace")
	}
}
