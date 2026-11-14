package main

import (
	"io"
	"os"
	"sort"
	"strconv"
)

const (
	maxCount       = 2000
	maxValue       = 1000000000
	maxInput       = (maxCount + 1) * 12
	maxOutput      = (maxCount + 1) * 6
	capacity       = 4096
	hashMultiplier = 2654435761
	hashFold       = 16
	slotShift      = 20
	maxCluster     = 32
	decimal        = 10
)

type positions struct {
	values   [capacity]uint32
	indices  [capacity]uint16
	overflow map[uint32]uint16
}

func (p *positions) slot(value uint32) uint32 {
	hash := value ^ (value >> hashFold)
	slot := (hash * hashMultiplier) >> slotShift
	for p.indices[slot] != 0 && p.values[slot] != value {
		slot = (slot + 1) & (capacity - 1)
	}
	return slot
}

func (p *positions) insert(value uint32, index uint16) bool {
	slot := p.slot(value)
	if p.indices[slot] != 0 {
		return false
	}
	p.indices[slot], p.values[slot] = index, value
	return true
}

func (p *positions) find(value int64) uint16 {
	if value < 0 || value > maxValue {
		return 0
	}
	if p.overflow != nil {
		return p.overflow[uint32(value)]
	}
	return p.indices[p.slot(uint32(value))]
}

// Long occupied runs make unsuccessful lookups expensive. Check both ends
// as a single run because linear probing can wrap around the table.
func (p *positions) boundProbes(values []int) {
	start := 0
	for p.indices[start] != 0 {
		start++
	}
	run := 0
	for offset := 1; offset < capacity; offset++ {
		slot := (start + offset) & (capacity - 1)
		if p.indices[slot] == 0 {
			run = 0
			continue
		}
		run++
		if run > maxCluster {
			p.overflow = make(map[uint32]uint16, len(values))
			for _, value := range values {
				key := uint32(value)
				p.overflow[key] = p.indices[p.slot(key)]
			}
			return
		}
	}
}

func nextNumber(data []byte, cursor *int) int {
	i := *cursor
	for i < len(data) && data[i] <= ' ' {
		i++
	}
	value := 0
	for i < len(data) && data[i] >= '0' && data[i] <= '9' {
		value = value*decimal + int(data[i]-'0')
		i++
	}
	*cursor = i
	return value
}

func longest(values []int, p *positions) (int64, int64, int64) {
	best, first, step := int64(1), int64(values[0]), int64(0)
	maximum := int64(values[len(values)-1])
	for i, value := range values {
		if len(values)-i <= int(best) {
			break
		}
		start := int64(value)
		for _, secondValue := range values[i+1:] {
			second := int64(secondValue)
			delta := second - start
			// A longer progression must include the next record-setting term.
			required := start + best*delta
			if required > maximum {
				break
			}
			if (best > 1 && p.find(required) == 0) || p.find(start-delta) != 0 {
				continue
			}
			length := int64(2)
			for next := second + delta; p.find(next) != 0; next += delta {
				length++
			}
			if length > best {
				best, first, step = length, start, delta
			}
		}
	}
	return best, first, step
}

func main() {
	var input [maxInput]byte
	size, _ := io.ReadFull(os.Stdin, input[:])
	data := input[:size]
	cursor := 0
	count := nextNumber(data, &cursor)
	var p positions
	values := make([]int, 0, count)
	for index := 1; index <= count; index++ {
		value := nextNumber(data, &cursor)
		if p.insert(uint32(value), uint16(index)) {
			values = append(values, value)
		}
	}
	p.boundProbes(values)
	sort.Ints(values)
	length, first, step := longest(values, &p)
	var output [maxOutput]byte
	result := strconv.AppendInt(output[:0], length, decimal)
	result = append(result, '\n')
	for i := int64(0); i < length; i++ {
		if i != 0 {
			result = append(result, ' ')
		}
		result = strconv.AppendUint(result, uint64(p.find(first+i*step)), decimal)
	}
	os.Stdout.Write(append(result, '\n'))
}
