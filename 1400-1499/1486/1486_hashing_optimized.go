package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	mixFirst  = 0x9e3779b185ebca87
	mixSecond = 0xc2b2ae3d27d4eb4f
	mixThird  = 0x165667b19e3779f9
	mixFinal  = 0xbf58476d1ce4e5b9
	mixShift  = 32
)

// Each occupied slot points to a representative square. All four labels
// are compared on a hit, so collisions cannot change the answer.
type classes struct {
	width, height int
	table         []uint32
	repeated      []bool
}

func (c *classes) match(previous, next []uint32, size, offset int) (int, int, bool) {
	for i := range c.table {
		c.table[i] = 0
	}
	if next != nil {
		for i := range c.repeated {
			c.repeated[i] = false
		}
	}
	mask := uint64(len(c.table) - 1)
	below := offset * c.width
	width := c.width - size + 1
	first, second := 0, 0
	matched := false
	for r := 0; r <= c.height-size; r++ {
		for i, end := r*c.width, r*c.width+width; i < end; i++ {
			a, b := previous[i], previous[i+offset]
			d, e := previous[i+below], previous[i+below+offset]
			if a == 0 || b == 0 || d == 0 || e == 0 {
				if next != nil {
					next[i] = 0
				}
				continue
			}
			hash := uint64(a)*mixFirst ^ uint64(b)*mixSecond ^ uint64(d)*mixThird ^ uint64(e)
			hash = (hash ^ (hash >> mixShift)) * mixFinal
			slot := (hash ^ (hash >> mixShift)) & mask
			for {
				label := c.table[slot]
				if label == 0 {
					label = uint32(i + 1)
					c.table[slot] = label
					if next != nil {
						next[i] = label
					}
					break
				}
				j := int(label - 1)
				if previous[j] == a && previous[j+offset] == b &&
					previous[j+below] == d && previous[j+below+offset] == e {
					if next == nil {
						return j, i, true
					}
					next[i] = label
					c.repeated[label] = true
					first, second, matched = j, i, true
					break
				}
				slot = (slot + 1) & mask
			}
		}
	}
	if next != nil {
		// A unique corner cannot be part of two equal larger squares.
		for r := 0; r <= c.height-size; r++ {
			for i, end := r*c.width, r*c.width+width; i < end; i++ {
				if !c.repeated[next[i]] {
					next[i] = 0
				}
			}
		}
	}
	return first, second, matched
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var height, width int
	fmt.Fscan(input, &height, &width)
	labels := make([]uint32, height*width)
	var seen ['z' - 'a' + 1]int
	best, first, second := 0, 0, 0
	for r := 0; r < height; r++ {
		var row string
		fmt.Fscan(input, &row)
		for col := 0; col < width; col++ {
			i := r*width + col
			letter := row[col] - 'a'
			labels[i] = uint32(letter) + 1
			if seen[letter] != 0 {
				best, first, second = 1, seen[letter]-1, i
			}
			seen[letter] = i + 1
		}
	}
	if best == 0 {
		fmt.Println(0)
		return
	}
	limit := height
	if width < limit {
		limit = width
	}
	if limit > 1 {
		capacity := 1
		for capacity < 2*(height-1)*(width-1) {
			capacity *= 2
		}
		index := classes{width, height, make([]uint32, capacity), make([]bool, len(labels)+1)}
		next := make([]uint32, len(labels))
		power := 1
		for power*2 <= limit {
			a, b, found := index.match(labels, next, power*2, power)
			if !found {
				break
			}
			power *= 2
			best, first, second = power, a, b
			labels, next = next, labels
		}
		// Between consecutive powers of two, the four corner blocks cover
		// the whole square. Their labels therefore determine exact equality.
		high := 2*power - 1
		if limit < high {
			high = limit
		}
		for low := power + 1; low <= high; {
			size := (low + high) / 2
			a, b, found := index.match(labels, nil, size, size-power)
			if found {
				best, first, second = size, a, b
				low = size + 1
			} else {
				high = size - 1
			}
		}
	}
	fmt.Println(best)
	fmt.Println(first/width+1, first%width+1)
	fmt.Println(second/width+1, second%width+1)
}
