package main

import "syscall"

func readInput(buffer []byte) int {
	for {
		count, err := syscall.Read(syscall.Stdin, buffer)
		if count > 0 {
			return count
		}
		if err != syscall.EINTR {
			return 0
		}
	}
}

func writeAll(buffer []byte) {
	for len(buffer) > 0 {
		count, err := syscall.Write(syscall.Stdout, buffer)
		if count > 0 {
			buffer = buffer[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 {
			return
		}
	}
}

const inputSize = 8192

var input [inputSize]byte
var position, length int

func nextByte() byte {
	if position == length {
		length = readInput(input[:])
		position = 0
		if length == 0 {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return sign * value
}

const outputSize = 64

var output [outputSize]byte
var used int

func writeNumber(value int) {
	const maxDigits = 20
	var digits [maxDigits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	used += copy(output[used:], digits[first:])
}

const maxSide = 12
const maxStates = 41835
const initialCapacity = 16384
const tableBits = 16
const tableSize = 1 << tableBits
const keyBits = 32
const hashMultiplier uint32 = 2654435761

var indexTable [tableSize]uint16
var free [maxSide + 1][maxSide + 1]bool

type layer struct {
	keys   []uint32
	counts []uint64
}

func newLayer() layer {
	return layer{make([]uint32, 0, initialCapacity), make([]uint64, 0, initialCapacity)}
}

func (state *layer) clear() {
	state.keys = state.keys[:0]
	state.counts = state.counts[:0]
	for i := range indexTable {
		indexTable[i] = 0
	}
}

func (next *layer) add(state uint32, count uint64) {
	slot := int((state * hashMultiplier) >> (keyBits - tableBits))
	for indexTable[slot] != 0 {
		index := int(indexTable[slot]) - 1
		if next.keys[index] == state {
			next.counts[index] += count
			return
		}
		slot = (slot + 1) & (tableSize - 1)
	}
	if len(next.keys) >= maxStates {
		panic("profile bound")
	}
	next.keys = append(next.keys, state)
	next.counts = append(next.counts, count)
	indexTable[slot] = uint16(len(next.keys))
}

const (
	// the ends of a path piece, matched like brackets
	opening, closing = 1, 2
	flip             = opening ^ closing // turns one end into the other
	bits             = 2                 // bits per plug
	mask             = 3                 // one plug
)

// partner finds the plug matching the bracket at pos, searching towards step.
func partner(state uint32, pos, step int) int {
	for depth := 0; ; pos += step {
		switch state >> uint(bits*pos) & mask {
		case opening:
			depth += step
		case closing:
			depth -= step
		}
		if depth == 0 {
			return pos
		}
	}
}

func main() {
	n, m := number(), number()
	transpose := m > n
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			c := nextByte()
			for c != 0 && c <= ' ' {
				c = nextByte()
			}
			if transpose {
				free[j][i] = c == '.'
			} else {
				free[i][j] = c == '.'
			}
		}
	}
	if transpose {
		n, m = m, n
	}
	last := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if free[i][j] {
				last = i*m + j
			}
		}
	}
	first, second := newLayer(), newLayer()
	ways, next := &first, &second
	ways.keys = append(ways.keys, 0)
	ways.counts = append(ways.counts, 1)
	total := uint64(0)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			next.clear()
			sl, su := uint(bits*j), uint(bits*(j+1))
			clear := ^(uint32(mask) << sl) & ^(uint32(mask) << su)
			down, right := free[i+1][j], free[i][j+1]
			for index, state := range ways.keys {
				count := ways.counts[index]
				left, up, base := state>>sl&mask, state>>su&mask, state&clear
				switch {
				case !free[i][j]:
					if left == 0 && up == 0 {
						next.add(state, count)
					}
				case left == 0 && up == 0:
					if down && right {
						next.add(base|opening<<sl|closing<<su, count)
					}
				case left == 0 || up == 0:
					end := left | up
					if down {
						next.add(base|end<<sl, count)
					}
					if right {
						next.add(base|end<<su, count)
					}
				case left == up:
					// two openings or two closings: the far end of one of the
					// joined pieces changes its kind
					var far int
					if left == opening {
						far = partner(state, j+1, 1)
					} else {
						far = partner(state, j, -1)
					}
					next.add(base^flip<<uint(bits*far), count)
				case left == closing:
					next.add(base, count)
				case i*m+j == last && base == 0:
					total += count // the loop closes on the last free cell
				}
			}
			ways, next = next, ways
		}
		// the next row starts with an empty left plug
		for index := range ways.keys {
			ways.keys[index] <<= bits
		}
	}
	writeNumber(int(total))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
