package main

import (
	"bufio"
	"os"
	"strconv"
)

const digits = 10
const wordBits = 64
const hashMultiplier uint64 = 11400714819323198485

var number []int64
var table, best, before, heap, position []int32
var bits uint
var size int32

// slots hold index + 1; zero marks an empty slot in the flat multiplicative hash table.
func slot(value int64) int {
	s := int(uint64(value) * hashMultiplier >> (wordBits - bits))
	for table[s] != 0 && number[table[s]-1] != value {
		s = (s + 1) & (len(table) - 1)
	}
	return s
}

// indexed decrease-key keeps one heap slot per vertex and avoids interface allocations.
func rise(v int32) {
	at := position[v]
	if at < 0 {
		at = size
		size++
	}
	for at > 0 {
		parent := (at - 1) / 2
		if best[heap[parent]] <= best[v] {
			break
		}
		heap[at] = heap[parent]
		position[heap[at]] = at
		at = parent
	}
	heap[at] = v
	position[v] = at
}
func relax(value int64, time, from int32) {
	v := table[slot(value)] - 1
	if v >= 0 && (best[v] < 0 || time < best[v]) {
		best[v] = time
		before[v] = from
		rise(v)
	}
}
func main() {
	in := bufio.NewReader(os.Stdin)
	// buffered byte parsing avoids fmt reflection and temporary phone-number strings.
	next := func() int64 {
		c, err := in.ReadByte()
		for err == nil && c <= ' ' {
			c, err = in.ReadByte()
		}
		value := int64(0)
		for err == nil && c >= '0' && c <= '9' {
			value = value*10 + int64(c-'0')
			c, err = in.ReadByte()
		}
		return value
	}
	n := int(next())
	var cost [digits]int32
	var place [digits]int64
	for p := range cost {
		cost[p] = int32(next())
	}
	place[digits-1] = 1
	for p := digits - 2; p >= 0; p-- {
		place[p] = place[p+1] * 10
	}
	capacity := 1
	for capacity < 2*n {
		capacity *= 2
		bits++
	}
	table = make([]int32, capacity)
	number = make([]int64, n)
	for i := range number {
		number[i] = next()
		table[slot(number[i])] = int32(i + 1)
	}
	// n <= 50000 and costs <= 10000 bound all distances by 499990000, within int32.
	best = make([]int32, n)
	before = make([]int32, n)
	heap = make([]int32, n)
	position = make([]int32, n)
	for i := range best {
		best[i] = -1
		before[i] = -1
		position[i] = -1
	}
	best[0] = 0
	rise(0)
	var digit [digits]int64
	for size > 0 {
		u := heap[0]
		size--
		last := heap[size]
		position[u] = -1
		if size > 0 {
			at := int32(0)
			for at*2+1 < size {
				child := at*2 + 1
				if child+1 < size && best[heap[child+1]] < best[heap[child]] {
					child++
				}
				if best[last] <= best[heap[child]] {
					break
				}
				heap[at] = heap[child]
				position[heap[at]] = at
				at = child
			}
			heap[at] = last
			position[last] = at
		}
		if int(u) == n-1 {
			break
		}
		value := number[u]
		for p := 0; p < digits; p++ {
			digit[p] = value / place[p] % 10
		}
		// neighbours with the first change at digit p share a prefix of p
		for p := 0; p < digits; p++ {
			low := value - digit[p]*place[p]
			for other := int64(0); other < digits; other++ {
				if other != digit[p] {
					relax(low+other*place[p], best[u]+cost[p], u)
				}
			}
			for q := p + 1; q < digits; q++ {
				if digit[q] != digit[p] {
					relax(value+(digit[q]-digit[p])*(place[p]-place[q]), best[u]+cost[p], u)
				}
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if best[n-1] < 0 {
		out.WriteString("-1\n")
		return
	}
	size = 0
	for v := int32(n - 1); v >= 0; v = before[v] {
		heap[size] = v
		size++
	}
	out.WriteString(strconv.Itoa(int(best[n-1])) + "\n" + strconv.Itoa(int(size)) + "\n")
	for size > 0 {
		size--
		out.WriteString(strconv.Itoa(int(heap[size] + 1)))
		if size > 0 {
			out.WriteByte(' ')
		} else {
			out.WriteByte('\n')
		}
	}
}
