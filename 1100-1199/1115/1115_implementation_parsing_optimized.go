package main

import (
	"os"
)

// no row is longer than all the ships together: 99 * 100
const rngMultiplier = 97
const maxShipLength = 100

const (
	searchLimit = 256
	attempts    = 128
	rngMod      = 65536
	maxSum      = 10000
	bits        = 64
)

type sums []uint64

func (s sums) has(v int) bool { return s[v/bits]>>(uint(v)%bits)&1 == 1 }

// shiftOr returns s | s << by
func (s sums) shiftOr(by int, out sums) sums {
	copy(out, s)
	w, b := by/bits, uint(by)%bits
	for i := len(s) - 1; i >= w; i-- {
		v := s[i-w] << b
		if b > 0 && i-w-1 >= 0 {
			v |= s[i-w-1] >> (bits - b)
		}
		out[i] |= v
	}
	return out
}

var (
	n, m               int
	ships, rows, order []int
	owner              []int
	calls              int
	limited            bool
)

func pick(pos int, free []int, reach []sums, k, need int) bool {
	if limited {
		calls++
		if calls > searchLimit {
			return false
		}
	}
	if need == 0 {
		return fill(pos + 1)
	}
	if !reach[k].has(need) {
		return false
	}
	last := -1
	for j := k; j < len(free); j++ {
		length := ships[free[j]]
		// equal ships are interchangeable: try each length once per place
		if length == last || length > need || !reach[j+1].has(need-length) {
			continue
		}
		last = length
		owner[free[j]] = order[pos]
		if pick(pos, free, reach, j+1, need-length) {
			return true
		}
		owner[free[j]] = -1
		if limited && calls > searchLimit {
			return false
		}
	}
	return false
}

func fill(pos int) bool {
	var free []int
	for i := 0; i < n; i++ {
		if owner[i] < 0 {
			free = append(free, i)
		}
	}
	if pos == m-1 {
		// the last row takes every ship that is left
		sum := 0
		for _, i := range free {
			sum += ships[i]
		}
		if sum != rows[order[pos]] {
			return false
		}
		for _, i := range free {
			owner[i] = order[pos]
		}
		return true
	}
	// reach[k]: the sums that the free ships from k on can make
	limit, largest := maxSum, 0
	for q := pos; q < m; q++ {
		if rows[order[q]] > largest {
			largest = rows[order[q]]
		}
	}
	if largest < limit {
		limit = largest
	}
	width := limit/bits + 1
	storage := make([]uint64, (len(free)+1)*width)
	reach := make([]sums, len(free)+1)
	for i := range reach {
		reach[i] = storage[i*width : (i+1)*width]
	}
	reach[len(free)][0] = 1
	for k := len(free) - 1; k >= 0; k-- {
		reach[k] = reach[k+1].shiftOr(ships[free[k]], reach[k])
	}
	for q := pos; q < m; q++ {
		if !reach[0].has(rows[order[q]]) {
			return false
		}
	}
	return pick(pos, free, reach, 0, rows[order[pos]])
}

func main() {
	n, m = integer(), integer()
	ships = make([]int, n)
	rows = make([]int, m)
	for i := range ships {
		ships[i] = integer()
	}
	for i := range rows {
		rows[i] = integer()
	}
	for i := 1; i < len(ships); i++ {
		value, j := ships[i], i
		for j > 0 && ships[j-1] < value {
			ships[j] = ships[j-1]
			j--
		}
		ships[j] = value
	}
	// try the shortest rows first as a heuristic
	order = make([]int, m)
	for r := range order {
		order[r] = r
	}
	for i := 1; i < len(order); i++ {
		value, j := order[i], i
		for j > 0 && (rows[order[j-1]] > rows[value] ||
			rows[order[j-1]] == rows[value] && order[j-1] > value) {
			order[j] = order[j-1]
			j--
		}
		order[j] = value
	}
	owner = make([]int, n)
	for i := range owner {
		owner[i] = -1
	}
	state := 1
	// restart costly searches in a reproducible order; the final search is complete
	for attempt := 0; attempt <= attempts; attempt++ {
		calls = 0
		limited = attempt < attempts
		if fill(0) {
			break
		}
		for i := m - 1; i > 0; i-- {
			state = (state*rngMultiplier + 1) % rngMod
			j := state % (i + 1)
			order[i], order[j] = order[j], order[i]
		}
		rank := make([]int, (maxShipLength + 1))
		for i := range rank {
			rank[i] = i
		}
		for i := maxShipLength; i > 1; i-- {
			state = (state*rngMultiplier + 1) % rngMod
			j := 1 + state%i
			rank[i], rank[j] = rank[j], rank[i]
		}
		for i := 1; i < len(ships); i++ {
			value, j := ships[i], i
			for j > 0 && rank[ships[j-1]] > rank[value] {
				ships[j] = ships[j-1]
				j--
			}
			ships[j] = value
		}
	}
	out := make([]byte, 0, 4*n+1)
	for r := 0; r < m; r++ {
		count := 0
		for _, row := range owner {
			if row == r {
				count++
			}
		}
		writeInteger(count)
		out = out[:0]
		first := true
		for i, row := range owner {
			if row == r {
				if !first {
					out = append(out, ' ')
				}
				first = false
				out = appendInteger(out, int64(ships[i]))
			}
		}
		out = append(out, '\n')
		writeBytes(out)
	}
}

const inputBufferBytes = 256

var inputBuffer [inputBufferBytes]byte
var inputPosition, inputLength int

// Keep only a bounded refill buffer and the current token; Read may return partial data.
// Refill a fixed byte buffer; EOF is separate from every possible input byte.
func nextByte() int {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(inputBuffer[:])
		inputPosition = 0
		if inputLength == 0 {
			return -1
		}
	}
	ch := inputBuffer[inputPosition]
	inputPosition++
	return int(ch)
}

// Read the single input stream once and convert tokens without fmt reflection.
// Parse decimal input directly to avoid fmt's reflection and token allocations.
func integer() int {
	position, length := inputPosition, inputLength
	read := func() int {
		if position == length {
			inputPosition = position
			ch := nextByte()
			position, length = inputPosition, inputLength
			return ch
		}
		ch := int(inputBuffer[position])
		position++
		return ch
	}
	ch := read()
	for ch >= 0 && ch <= ' ' {
		ch = read()
	}
	negative := ch == '-'
	if negative || ch == '+' {
		ch = read()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		if negative {
			value = value*10 - (ch - '0')
		} else {
			value = value*10 + ch - '0'
		}
		ch = read()
	}
	if ch >= 0 {
		position--
	}
	inputPosition = position
	return value
}

// Reuse one output buffer; io.Writer cannot retain it after Write returns.
func writeBytes(data []byte) {
	for len(data) > 0 {
		count, err := os.Stdout.Write(data)
		if count > 0 {
			data = data[count:]
		}
		if err != nil || count == 0 {
			return
		}
	}
}
func appendInteger(out []byte, value int64) []byte {
	var buffer [24]byte
	at := len(buffer)
	negative := value < 0
	var magnitude uint64
	if negative {
		magnitude = uint64(-(value + 1)) + 1
	} else {
		magnitude = uint64(value)
	}
	for {
		at--
		buffer[at] = byte('0' + magnitude%10)
		magnitude /= 10
		if magnitude == 0 {
			break
		}
	}
	if negative {
		at--
		buffer[at] = '-'
	}
	return append(out, buffer[at:]...)
}
func writeInteger(value int) {
	var bytes [24]byte
	out := appendInteger(bytes[:0], int64(value))
	out = append(out, '\n')
	writeBytes(out)
}
