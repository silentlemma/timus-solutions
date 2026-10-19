package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	full    = int64(1)<<32 - 1
	byteLen = 8
)

type block struct{ lo, hi, gate int64 }

// a dotted address read byte by byte
func address(text string) int64 {
	var value int64
	for _, part := range strings.Split(text, ".") {
		b, _ := strconv.Atoi(part)
		value = value<<byteLen | int64(b)
	}
	return value
}

// each row covers one aligned block of addresses, and two blocks are
// nested or apart; sweeping them by start, larger first, with a stack of
// open blocks cuts the line into pieces routed by the innermost one
func pieces(blocks []block) []block {
	sort.Slice(blocks, func(i, j int) bool {
		if blocks[i].lo != blocks[j].lo {
			return blocks[i].lo < blocks[j].lo
		}
		return blocks[i].hi > blocks[j].hi
	})
	blocks = append(blocks, block{full + 1, full + 1, -1})
	var out, stack []block
	pos := int64(0)
	// adjacent pieces with one gateway merge, so equal routing gives
	// equal lists
	emit := func(lo, hi, gate int64) {
		if lo > hi {
			return
		}
		if k := len(out) - 1; k >= 0 && out[k].hi+1 == lo && out[k].gate == gate {
			out[k].hi = hi
		} else {
			out = append(out, block{lo, hi, gate})
		}
	}
	for _, b := range blocks {
		for len(stack) > 0 && stack[len(stack)-1].hi < b.lo {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			emit(pos, top.hi, top.gate)
			pos = top.hi + 1
		}
		if len(stack) > 0 {
			emit(pos, b.lo-1, stack[len(stack)-1].gate)
		}
		pos = b.lo
		stack = append(stack, b)
	}
	return out
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var tables [2][]block
	for t := range tables {
		var count int
		if _, err := fmt.Fscan(in, &count); err != nil {
			return
		}
		blocks := make([]block, count)
		for i := range blocks {
			var ds, ms, gs string
			fmt.Fscan(in, &ds, &ms, &gs)
			d, m := address(ds), address(ms)
			blocks[i] = block{d & m, (d & m) | (full ^ m), address(gs)}
		}
		tables[t] = pieces(blocks)
	}
	same := len(tables[0]) == len(tables[1])
	for i := 0; same && i < len(tables[0]); i++ {
		same = tables[0][i] == tables[1][i]
	}
	if same {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
