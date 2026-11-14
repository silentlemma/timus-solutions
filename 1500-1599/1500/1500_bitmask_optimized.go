package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

const (
	maxCrossings = 30
	groupBits    = 5
	groups       = 4
	groupSize    = 1 << groupBits
	groupMask    = groupSize - 1
	home         = 1
	work         = 2
)

type roads [maxCrossings][groups][groupSize]uint32

func (graph *roads) connects(permits uint32) bool {
	a := permits & groupMask
	b := permits >> groupBits & groupMask
	c := permits >> (2 * groupBits) & groupMask
	d := permits >> ((groups - 1) * groupBits)
	seen, pending := uint32(home), uint32(home)
	for pending != 0 {
		row := &graph[bits.TrailingZeros32(pending)]
		pending &= pending - 1
		fresh := (row[0][a] | row[1][b] | row[2][c] | row[groups-1][d]) &^ seen
		if fresh&work != 0 {
			return true
		}
		seen |= fresh
		pending |= fresh
	}
	return false
}

func (graph *roads) choose(required, available uint32, count int) (uint32, bool) {
	if count == 0 {
		return required, graph.connects(required)
	}
	for bits.OnesCount32(available) >= count {
		bit := available & -available
		available ^= bit
		if result, ok := graph.choose(required|bit, available, count-1); ok {
			return result, true
		}
	}
	return 0, false
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var categories, crossings, count int
	fmt.Fscan(input, &categories, &crossings, &count)
	var graph roads
	for i := 0; i < count; i++ {
		var a, b, category int
		fmt.Fscan(input, &a, &b, &category)
		group := category / groupBits
		bit := 1 << (category % groupBits)
		graph[a][group][bit] |= 1 << b
		graph[b][group][bit] |= 1 << a
	}
	for crossing := 0; crossing < crossings; crossing++ {
		for group := range graph[crossing] {
			table := &graph[crossing][group]
			for mask := 1; mask < groupSize; mask++ {
				previous := mask & (mask - 1)
				table[mask] |= table[previous] | table[mask^previous]
			}
		}
	}

	all := uint32(1)<<categories - 1
	var required uint32
	// If omitting a category disconnects the endpoints, every answer needs it.
	for bit := uint32(1); bit <= all; bit <<= 1 {
		if !graph.connects(all ^ bit) {
			required |= bit
		}
	}
	available := all &^ required
	for extra := 0; extra <= bits.OnesCount32(available); extra++ {
		if result, ok := graph.choose(required, available, extra); ok {
			output := bufio.NewWriter(os.Stdout)
			fmt.Fprintln(output, bits.OnesCount32(result))
			separator := ""
			for result != 0 {
				fmt.Fprint(output, separator, bits.TrailingZeros32(result))
				separator = " "
				result &= result - 1
			}
			fmt.Fprintln(output)
			output.Flush()
			return
		}
	}
}
