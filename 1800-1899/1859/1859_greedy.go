package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	seats = 4 // compartment seats in a block
	sides = 2 // side seats in a block
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type block struct {
	members []int
	free    int // free compartment seats
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	word := func() string {
		in.Scan()
		return in.Text()
	}
	number := func() int {
		v, _ := strconv.Atoi(word())
		return v
	}
	n := number()
	wish := word()
	m := number()
	people := (seats + sides) * n
	parent := make([]int, people)
	for i := range parent {
		parent[i] = i
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	for k := 0; k < m; k++ {
		a, b := number()-1, number()-1
		parent[find(a)] = find(b)
	}
	members := make([][]int, people)
	for p := 0; p < people; p++ {
		r := find(p)
		members[r] = append(members[r], p+1)
	}
	// a group of friends wants a compartment seats and b side seats; a block
	// holds one group with b = 2, or two groups with b = 1, and groups with
	// b = 0 fill the compartment seats left: kind[b][a]
	var kind [sides + 1][seats + 1][][]int
	for _, g := range members {
		if len(g) == 0 {
			continue
		}
		a := 0
		for _, p := range g {
			if wish[p-1] == '1' {
				a++
			}
		}
		kind[len(g)-a][a] = append(kind[len(g)-a][a], g)
	}
	fillers, halves, wholes := &kind[0], &kind[1], &kind[sides]
	s0, s1, s2 := len(halves[0]), len(halves[1]), len(halves[2])
	s3, s4 := len(halves[seats-1]), len(halves[seats])
	t0, t1, t2 := len(wholes[0]), len(wholes[1]), len(wholes[2])
	f2, f3, f4 := len(fillers[2]), len(fillers[seats-1]), len(fillers[seats])
	// fits tells whether the fillers can fill blocks with c4, c3, c2 free
	// compartment seats (and some with 1): fours need a 4, threes take a 3
	// first and then a 4, twos take what is left of the 2s, 3s and 4s
	fits := func(c4, c3, c2 int) bool {
		if f4 > c4 || f3 > c3+c4-f4 {
			return false
		}
		late := max(0, f3-c3) // threes in blocks with 4 free seats
		return f2 <= c2+(c3-f3+late)+2*(c4-f4-late)
	}
	// two halves with a1 and a2 leave 4 - a1 - a2 free seats; merging the
	// free seats of two blocks never hurts, so threes pair with ones when
	// they can, and two (0, 2) pairs would rather be (2, 2) and (0, 0)
	x31 := min(s3, s1)
	x30 := s3 - x31
	ones := s1 - x31
	zeros := s0 - s4 - x30
	type pair struct{ a, b, count int }
	var plan []pair
	for x20 := 0; x20 <= 1 && plan == nil; x20++ {
		for x21 := 0; x21 <= min(s2-x20, ones) && plan == nil; x21++ {
			// with x11 pairs (1, 1) the zeros left pair up as base + 2 x11
			base := zeros - x20 - ones + x21
			if (s2-x21-x20)%2 != 0 || base%2 != 0 {
				continue
			}
			// x11 must leave both kinds of pairs possible and give the fours
			// and the threes their blocks; the room for twos rises until the
			// free threes run short of threes and falls after that
			low := max(max(0, -base/2), f4-t0-base/2)
			high := min((ones-x21)/2, t0+t1+ones-x21+base/2-f3-f4)
			peak := min(max((t1+ones-x21-f3)/2, low), high)
			for x11 := peak - 1; x11 <= peak+1; x11++ {
				x10, x00 := ones-x21-2*x11, base/2+x11
				if low <= x11 && x11 <= high && fits(t0+x00, t1+x10, t2+x20+x11) {
					plan = []pair{{seats, 0, s4}, {seats - 1, 1, x31}, {seats - 1, 0, x30},
						{2, 2, (s2 - x21 - x20) / 2}, {2, 1, x21}, {2, 0, x20},
						{1, 1, x11}, {1, 0, x10}, {0, 0, x00}}
					break
				}
			}
		}
	}
	var blocks []block
	for a := 0; a <= seats; a++ {
		for _, g := range wholes[a] {
			blocks = append(blocks, block{g, seats - a})
		}
	}
	pop := func(list *[][]int) []int {
		g := (*list)[len(*list)-1]
		*list = (*list)[:len(*list)-1]
		return g
	}
	for _, p := range plan {
		for k := 0; k < p.count; k++ {
			g := append(pop(&halves[p.a]), pop(&halves[p.b])...)
			blocks = append(blocks, block{g, seats - p.a - p.b})
		}
	}
	// the fillers, largest first, as the check above assumes
	var free [seats + 1][]int
	for i, b := range blocks {
		free[b.free] = append(free[b.free], i)
	}
	for size := seats; size >= 1; size-- {
		for _, g := range fillers[size] {
			at := size
			for len(free[at]) == 0 {
				at++
			}
			i := free[at][len(free[at])-1]
			free[at] = free[at][:len(free[at])-1]
			blocks[i].members = append(blocks[i].members, g...)
			free[at-size] = append(free[at-size], i)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, b := range blocks {
		for k, p := range b.members {
			if k > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(p))
		}
		out.WriteByte('\n')
	}
}
