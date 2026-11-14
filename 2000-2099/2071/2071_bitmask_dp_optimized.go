package main

import (
	"bufio"
	"math/bits"
	"os"
	"strconv"
)

const (
	juiceCount = 3
	kinds      = 1<<juiceCount - 1
	states     = 1 << kinds
	unreached  = juiceCount*kinds + 1
	digits     = 10
	byteValues = 1 << 8
)

func bestOrder(present int) (byte, []int) {
	var cost, previous [states][kinds]byte
	for used := range cost {
		for last := range cost[used] {
			cost[used][last] = unreached
		}
	}
	for kind := 0; kind < kinds; kind++ {
		if present&(1<<kind) != 0 {
			cost[1<<kind][kind] = byte(bits.OnesCount(uint(kind + 1)))
		}
	}
	for used := 1; used < present; used++ {
		available := present &^ used
		for last, current := range cost[used] {
			if current == unreached {
				continue
			}
			for remaining := available; remaining != 0; remaining &= remaining - 1 {
				next := bits.TrailingZeros(uint(remaining))
				state := used | 1<<next
				total := current + byte(bits.OnesCount(uint((next+1)&^(last+1))))
				if total < cost[state][next] {
					cost[state][next] = total
					previous[state][next] = byte(last)
				}
			}
		}
	}
	last := 0
	for kind := 1; kind < kinds; kind++ {
		if cost[present][kind] < cost[present][last] {
			last = kind
		}
	}
	minimum := cost[present][last]
	order := make([]int, 0, kinds)
	for used := present; used != 0; {
		order = append(order, last)
		used, last = used^(1<<last), int(previous[used][last])
	}
	return minimum, order
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	input.Scan()
	count, _ := strconv.Atoi(input.Text())
	var first [kinds]uint32
	next := make([]uint32, count+1)
	var juiceBit [byteValues]uint8
	juiceBit['A'], juiceBit['B'], juiceBit['P'] = 1, 2, 1<<(juiceCount-1)
	present := 0
	for glass := 1; glass <= count; glass++ {
		input.Scan()
		var mask uint8
		for _, juice := range input.Bytes() {
			mask |= juiceBit[juice]
		}
		kind := mask - 1
		present |= 1 << kind
		// Link the indices of each cocktail type through a single array.
		next[glass], first[kind] = first[kind], uint32(glass)
	}
	minimum, order := bestOrder(present)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var buffer [digits]byte
	output.Write(strconv.AppendUint(buffer[:0], uint64(minimum), 10))
	separator := byte('\n')
	for i := len(order) - 1; i >= 0; i-- {
		for glass := first[order[i]]; glass != 0; glass = next[glass] {
			output.WriteByte(separator)
			output.Write(strconv.AppendUint(buffer[:0], uint64(glass), 10))
			separator = ' '
		}
	}
	output.WriteByte('\n')
}
