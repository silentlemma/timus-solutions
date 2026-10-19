package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"sort"
)

const smallRemovals = 7
const bufferSize = 1 << 16

type fastInput struct {
	reader *bufio.Reader
}

func (in *fastInput) nextInt() int {
	value := 0
	ch, err := in.reader.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = in.reader.ReadByte()
	}
	for err == nil && ch >= '0' && ch <= '9' {
		value = value*10 + int(ch-'0')
		ch, err = in.reader.ReadByte()
	}
	return value
}

func search(values []int, kept int) int {
	n := len(values)
	suffix := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		suffix[i] = suffix[i+1] | values[i]
	}
	best := 0
	for _, value := range values[:kept] {
		best |= value
	}
	var visit func(int, int, int)
	visit = func(index, needed, current int) {
		if needed == 0 {
			if current > best {
				best = current
			}
			return
		}
		upper := current | suffix[index]
		if upper <= best {
			return
		}
		// Each uncovered bit needs at most one witness; extra places can be filled.
		if needed == n-index || needed >= bits.OnesCount(uint(suffix[index] & ^current)) {
			best = upper
			return
		}
		visit(index+1, needed-1, current|values[index])
		visit(index+1, needed, current)
	}
	visit(0, kept, 0)
	return best
}

func solveDP(values []int, kept, full int) int {
	count := make([]int, full+1)
	for i := range count {
		count[i] = kept + 1
	}
	count[0] = 0
	upper, best, previous := 0, 0, -1
	for _, value := range values {
		if value == previous {
			continue
		}
		previous = value
		// OR never decreases a mask, so descending updates use each element once.
		for mask := upper; mask >= 0; mask-- {
			if count[mask] < kept {
				merged := mask | value
				if count[mask]+1 < count[merged] {
					count[merged] = count[mask] + 1
				}
				if merged > best {
					best = merged
				}
			}
		}
		upper |= value
		if best == full {
			break
		}
	}
	return best
}

func main() {
	in := fastInput{bufio.NewReaderSize(os.Stdin, bufferSize)}
	n, removed := in.nextInt(), in.nextInt()
	values := make([]int, n)
	full := 0
	for i := range values {
		values[i] = in.nextInt()
		full |= values[i]
	}
	kept := n - removed
	answer := full
	if kept < bits.OnesCount(uint(full)) {
		sort.Sort(sort.Reverse(sort.IntSlice(values)))
		if removed <= smallRemovals {
			answer = search(values, kept)
		} else {
			answer = solveDP(values, kept, full)
		}
	}
	fmt.Println(answer)
}
