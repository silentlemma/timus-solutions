package main

import (
	"bufio"
	"math/bits"
	"os"
	"sort"
	"strconv"
)

const (
	outputSize = 16
	decimal    = 10
)

type offer struct {
	mask  uint
	price uint16
}

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	caps := nextInt(input)
	offers := make([]offer, caps)
	for i := range offers {
		offers[i] = offer{1 << uint(i), uint16(nextInt(input))}
	}
	for sets := nextInt(input); sets > 0; sets-- {
		price, size := nextInt(input), nextInt(input)
		var mask uint
		for i := 0; i < size; i++ {
			mask |= 1 << uint(nextInt(input)-1)
		}
		offers = append(offers, offer{mask, uint16(price)})
	}
	var wanted uint
	for count := nextInt(input); count > 0; count-- {
		wanted |= 1 << uint(nextInt(input)-1)
	}
	for i := range offers {
		offers[i].mask &= wanted
	}

	useful := make([]offer, 0, len(offers))
	for i, current := range offers {
		if current.mask == 0 {
			continue
		}
		dominated := false
		for j, other := range offers {
			if other.mask&current.mask == current.mask &&
				(other.price < current.price ||
					other.price == current.price && (other.mask != current.mask || j < i)) {
				dominated = true
				break
			}
		}
		if !dominated {
			useful = append(useful, current)
		}
	}

	type capInfo struct {
		bit    uint
		offers int
	}
	order := make([]capInfo, 0, caps)
	for bit := uint(1); bit <= wanted; bit <<= 1 {
		if wanted&bit == 0 {
			continue
		}
		info := capInfo{bit: bit}
		for _, current := range useful {
			if current.mask&bit != 0 {
				info.offers++
			}
		}
		order = append(order, info)
	}
	sort.Slice(order, func(i, j int) bool { return order[i].offers < order[j].offers })
	full := uint(1)<<uint(len(order)) - 1
	choices := make([][]offer, len(order))
	for _, current := range useful {
		var mask uint
		for i, cap := range order {
			if current.mask&cap.bit != 0 {
				mask |= 1 << uint(i)
			}
		}
		for pending := mask; pending != 0; pending &= pending - 1 {
			bit := bits.TrailingZeros(pending)
			choices[bit] = append(choices[bit], offer{full ^ mask, current.price})
		}
	}
	// Buying each cap separately costs at most 20,000.
	cheapest := make([]uint16, full+1)
	for missing := uint(1); missing <= full; missing++ {
		least := ^uint16(0)
		for _, current := range choices[bits.TrailingZeros(missing)] {
			value := current.price + cheapest[missing&current.mask]
			if value < least {
				least = value
			}
		}
		cheapest[missing] = least
	}
	var output [outputSize]byte
	line := strconv.AppendUint(output[:0], uint64(cheapest[full]), decimal)
	os.Stdout.Write(append(line, '\n'))
}
