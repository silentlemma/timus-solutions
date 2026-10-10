package main

import (
	"bufio"
	"container/heap"
	"os"
	"sort"
	"strconv"
)

const (
	// rounds is the number of improvements after which the local search stops
	rounds = 20000
	// splitBits caps the bits of tables one exact split of two generals uses
	splitBits = 4000000
	word      = 64
	// a box is its value shifted by indexBits, plus its number
	indexBits = 14
	indexMask = 1<<indexBits - 1
)

type poorHeap [][2]int64

func (h poorHeap) Len() int { return len(h) }
func (h poorHeap) Less(i, j int) bool {
	return h[i][0] < h[j][0] || h[i][0] == h[j][0] && h[i][1] < h[j][1]
}
func (h poorHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *poorHeap) Push(x interface{}) { *h = append(*h, x.([2]int64)) }
func (h *poorHeap) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

var sums []int64
var boxes [][]int // sorted, per general

func put(list []int, b int) []int {
	k := sort.SearchInts(list, b)
	list = append(list, 0)
	copy(list[k+1:], list[k:])
	list[k] = b
	return list
}

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

// exchange makes the move or swap of boxes from hi to lo that leaves the
// smallest gap between the two, if it is smaller than now
func exchange(hi, lo int) bool {
	d := sums[hi] - sums[lo]
	if d <= 1 {
		return false
	}
	best, bestA, bestB := d, -1, -1
	a, b := boxes[hi], boxes[lo]
	consider := func(t int64, ia, ib int) {
		if t > 0 && t < d && abs(d-2*t) < best {
			best, bestA, bestB = abs(d-2*t), ia, ib
		}
	}
	half := int(d / 2)
	if len(a) > 1 {
		k := sort.SearchInts(a, half<<indexBits)
		for ia := k - 1; ia <= k; ia++ {
			if ia >= 0 && ia < len(a) {
				consider(int64(a[ia]>>indexBits), ia, -1)
			}
		}
	}
	for ia := range a {
		va := a[ia] >> indexBits
		if ia > 0 && va == a[ia-1]>>indexBits {
			continue
		}
		k := sort.SearchInts(b, (va-half)<<indexBits)
		for ib := k - 1; ib <= k; ib++ {
			if ib >= 0 && ib < len(b) {
				consider(int64(va-b[ib]>>indexBits), ia, ib)
			}
		}
	}
	if bestA < 0 {
		return false
	}
	x := a[bestA]
	a = append(a[:bestA], a[bestA+1:]...)
	sums[hi] -= int64(x >> indexBits)
	sums[lo] += int64(x >> indexBits)
	if bestB >= 0 {
		y := b[bestB]
		b = append(b[:bestB], b[bestB+1:]...)
		a = put(a, y)
		sums[hi] += int64(y >> indexBits)
		sums[lo] -= int64(y >> indexBits)
	}
	boxes[hi], boxes[lo] = a, put(b, x)
	return true
}

// split takes the most even split of the boxes of hi and lo found by subset
// sums, if it narrows their gap and leaves each general a box
func split(hi, lo int) bool {
	items := append(append([]int{}, boxes[hi]...), boxes[lo]...)
	total := sums[hi] + sums[lo]
	count, words := len(items), int(total/word)+1
	if int64(count+1)*int64(words)*word > splitBits {
		return false
	}
	reach := make([][]uint64, count+1)
	reach[0] = make([]uint64, words)
	reach[0][0] = 1
	for k := 0; k < count; k++ {
		v := items[k] >> indexBits
		shift, bits := v/word, uint(v%word)
		from, to := reach[k], make([]uint64, words)
		for w := 0; w < words; w++ {
			var moved uint64
			if w-shift >= 0 {
				moved = from[w-shift] << bits
				if bits > 0 && w-shift-1 >= 0 {
					moved |= from[w-shift-1] >> (word - bits)
				}
			}
			to[w] = from[w] | moved
		}
		reach[k+1] = to
	}
	has := func(k int, t int64) bool { return reach[k][t/word]>>uint(t%word)&1 == 1 }
	t := total / 2
	for t > 0 && !has(count, t) {
		t--
	}
	if t == 0 || total-2*t >= sums[hi]-sums[lo] {
		return false
	}
	var small, big []int
	rest := t
	for k := count - 1; k >= 0; k-- {
		if !has(k, rest) {
			small = append(small, items[k])
			rest -= int64(items[k] >> indexBits)
		} else {
			big = append(big, items[k])
		}
	}
	if len(small) == 0 || len(big) == 0 {
		return false
	}
	sort.Ints(small)
	sort.Ints(big)
	boxes[hi], boxes[lo] = big, small
	sums[hi], sums[lo] = total-t, t
	return true
}

func readInt(in *bufio.Reader) int {
	n, c := 0, byte(' ')
	for c == ' ' || c == '\n' || c == '\r' {
		c, _ = in.ReadByte()
	}
	for ; c >= '0' && c <= '9'; c, _ = in.ReadByte() {
		n = n*10 + int(c-'0')
	}
	return n
}

func main() {
	in := bufio.NewReader(os.Stdin)
	n, m, limit := readInt(in), readInt(in), int64(readInt(in))
	value := make([]int, n)
	for i := range value {
		value[i] = readInt(in)
	}
	// largest boxes first, each to the general with the least gold so far
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.SliceStable(order, func(x, y int) bool { return value[order[x]] > value[order[y]] })
	sums = make([]int64, m)
	boxes = make([][]int, m)
	poorest := make(poorHeap, m)
	for g := range poorest {
		poorest[g] = [2]int64{0, int64(g)}
	}
	heap.Init(&poorest)
	for _, i := range order {
		top := heap.Pop(&poorest).([2]int64)
		g := int(top[1])
		boxes[g] = append(boxes[g], value[i]<<indexBits|i)
		sums[g] = top[0] + int64(value[i])
		heap.Push(&poorest, [2]int64{sums[g], int64(g)})
	}
	for _, list := range boxes {
		sort.Ints(list)
	}
	// then even out the richest and the poorest general against the others
	up, down := make([]int, m), make([]int, m)
	for round := 0; round < rounds; round++ {
		hi, lo := 0, 0
		for g := range sums {
			if sums[g] > sums[hi] {
				hi = g
			}
			if sums[g] < sums[lo] {
				lo = g
			}
		}
		if sums[hi]-sums[lo] <= limit {
			break
		}
		if exchange(hi, lo) {
			continue
		}
		for g := range up {
			up[g], down[g] = g, g
		}
		sort.SliceStable(up, func(x, y int) bool { return sums[up[x]] < sums[up[y]] })
		sort.SliceStable(down, func(x, y int) bool { return sums[down[x]] > sums[down[y]] })
		moved := false
		for _, g := range up {
			if !moved && g != hi {
				moved = exchange(hi, g)
			}
		}
		for _, g := range down {
			if !moved && g != lo {
				moved = exchange(g, lo)
			}
		}
		moved = moved || split(hi, lo)
		for _, g := range up {
			if !moved && g != hi {
				moved = split(hi, g)
			}
		}
		for _, g := range down {
			if !moved && g != lo {
				moved = split(g, lo)
			}
		}
		if !moved {
			break
		}
	}
	most, least := sums[0], sums[0]
	for _, s := range sums {
		if s > most {
			most = s
		}
		if s < least {
			least = s
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.FormatInt(most-least, 10) + "\n")
	for _, list := range boxes {
		ids := make([]int, len(list))
		for k, b := range list {
			ids[k] = b&indexMask + 1
		}
		sort.Ints(ids)
		for k, id := range ids {
			if k > 0 {
				out.WriteString(" ")
			}
			out.WriteString(strconv.Itoa(id))
		}
		out.WriteString("\n")
	}
}
