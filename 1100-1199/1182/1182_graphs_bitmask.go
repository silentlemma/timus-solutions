package main

import (
	"math/bits"
	"os"
	"strconv"
)

const (
	maxPeople  = 100
	wordBits   = 64
	wordCount  = 2
	inputSize  = 512
	outputSize = 1024
)

type bitmap [wordCount]uint64

func has(value bitmap, index int) bool {
	return value[index/wordBits]>>uint(index%wordBits)&1 != 0
}
func insert(value *bitmap, index int) { value[index/wordBits] |= uint64(1) << uint(index%wordBits) }
func shifted(value bitmap, count int) bitmap {
	if count == 0 {
		return value
	}
	if count >= wordBits {
		return bitmap{0, value[0] << uint(count-wordBits)}
	}
	return bitmap{value[0] << uint(count), value[1]<<uint(count) | value[0]>>uint(wordBits-count)}
}

type input struct {
	bytes            [inputSize]byte
	position, length int
}

func (in *input) next() byte {
	if in.position == in.length {
		in.length, _ = os.Stdin.Read(in.bytes[:])
		in.position = 0
		if in.length == 0 {
			return 0
		}
	}
	c := in.bytes[in.position]
	in.position++
	return c
}
func (in *input) number() int {
	c, value := in.next(), 0
	for c != 0 && c <= ' ' {
		c = in.next()
	}
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = in.next()
	}
	return value
}

func main() {
	var in input
	n := in.number()
	var knows, edges [maxPeople]bitmap
	for person := 0; person < n; person++ {
		for friend := in.number(); friend != 0; friend = in.number() {
			insert(&knows[person], friend-1)
		}
	}
	for a := 0; a < n; a++ {
		for b := a + 1; b < n; b++ {
			if !has(knows[a], b) || !has(knows[b], a) {
				insert(&edges[a], b)
				insert(&edges[b], a)
			}
		}
	}
	var remaining bitmap
	for person := 0; person < n; person++ {
		insert(&remaining, person)
	}
	var colors [2]bitmap
	var side [maxPeople]uint8
	var parts [maxPeople][2]bitmap
	var sizes [maxPeople][2]uint8
	components := 0
	for seed := 0; seed < n; seed++ {
		if !has(remaining, seed) {
			continue
		}
		remaining[seed/wordBits] &^= uint64(1) << uint(seed%wordBits)
		side[seed] = 0
		insert(&colors[0], seed)
		var queue [maxPeople]uint8
		queue[0] = uint8(seed)
		tail := 1
		for head := 0; head < tail; head++ {
			person := int(queue[head])
			group := side[person]
			insert(&parts[components][group], person)
			sizes[components][group]++
			for word := 0; word < wordCount; word++ {
				if edges[person][word]&colors[group][word] != 0 {
					os.Stdout.Write([]byte("No solution\n"))
					return
				}
				pending := edges[person][word] & remaining[word]
				for pending != 0 {
					bit := uint(bits.TrailingZeros64(pending))
					mask := uint64(1) << bit
					pending &^= mask
					remaining[word] &^= mask
					neighbor := word*wordBits + int(bit)
					side[neighbor] = 1 - group
					colors[1-group][word] |= mask
					queue[tail] = uint8(neighbor)
					tail++
				}
			}
		}
		components++
	}
	// Retain one small reachability bitset per component for exact reconstruction.
	var history [maxPeople + 1]bitmap
	history[0][0] = 1
	for component := 0; component < components; component++ {
		a := shifted(history[component], int(sizes[component][0]))
		b := shifted(history[component], int(sizes[component][1]))
		history[component+1] = bitmap{a[0] | b[0], a[1] | b[1]}
	}
	size := n / 2
	for size > 0 && !has(history[components], size) {
		size--
	}
	if size == 0 {
		os.Stdout.Write([]byte("No solution\n"))
		return
	}
	var teams [2]bitmap
	for component := components - 1; component >= 0; component-- {
		pick := 0
		a := int(sizes[component][0])
		if size < a || !has(history[component], size-a) {
			pick = 1
		}
		for word := 0; word < wordCount; word++ {
			teams[0][word] |= parts[component][pick][word]
			teams[1][word] |= parts[component][1-pick][word]
		}
		size -= int(sizes[component][pick])
	}
	var buffer [outputSize]byte
	output := buffer[:0]
	for _, team := range teams {
		count := bits.OnesCount64(team[0]) + bits.OnesCount64(team[1])
		output = strconv.AppendInt(output, int64(count), 10)
		for person := 0; person < n; person++ {
			if has(team, person) {
				output = append(output, ' ')
				output = strconv.AppendInt(output, int64(person+1), 10)
			}
		}
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
