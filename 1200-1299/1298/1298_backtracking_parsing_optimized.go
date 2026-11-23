package main

import (
	"os"
)

var moves = [8][2]int{{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}}

var (
	n    int
	seen []bool
	path [][2]int
)

func freeSquares(c, r int, out *[8][2]int) int {
	count := 0
	for _, m := range moves {
		nc, nr := c+m[0], r+m[1]
		if nc >= 0 && nc < n && nr >= 0 && nr < n && !seen[nc*n+nr] {
			if out != nil {
				out[count] = [2]int{nc, nr}
			}
			count++
		}
	}
	return count
}

func tour(c, r int) bool {
	seen[c*n+r] = true
	path = append(path, [2]int{c, r})
	if len(path) == n*n {
		return true
	}
	// Warnsdorff's rule: try first the squares with the fewest onward
	// moves, and the search still backtracks, so it is exact
	var next [8][2]int
	count := freeSquares(c, r, &next)
	var degree, order [8]int
	for i, sq := range next[:count] {
		degree[i] = freeSquares(sq[0], sq[1], nil)
		order[i] = i
	}
	// Stable insertion sorting preserves the exact old move tie order.
	for i := 1; i < count; i++ {
		value, at := order[i], i
		for at > 0 && degree[order[at-1]] > degree[value] {
			order[at] = order[at-1]
			at--
		}
		order[at] = value
	}
	for _, i := range order[:count] {
		if tour(next[i][0], next[i][1]) {
			return true
		}
	}

	seen[c*n+r] = false
	path = path[:len(path)-1]
	return false
}

func main() {
	n = integer()
	if n >= 2 && n <= 4 {
		writeBytes([]byte("IMPOSSIBLE\n"))
		return
	}
	path = make([][2]int, 0, n*n)
	seen = make([]bool, n*n)
	found := false
	for c := 0; c < n && !found; c++ {
		for r := 0; r < n && !found; r++ {
			found = tour(c, r)
		}
	}
	if !found {
		writeBytes([]byte("IMPOSSIBLE\n"))
		return
	}
	const outputCapacity = 4096
	out := make([]byte, 0, outputCapacity)
	for _, sq := range path {
		out = append(out, byte('a'+sq[0]))
		out = appendInteger(out, int64(sq[1]+1))
		out = append(out, '\n')
		if len(out) > outputCapacity-24 {
			writeBytes(out)
			out = out[:0]
		}
	}
	writeBytes(out)
}

const inputBufferBytes = 256

var inputBuffer [inputBufferBytes]byte
var inputPosition, inputLength int

// Keep only a bounded refill buffer and the current token; Read may return partial data.
// Refill a fixed byte buffer; EOF is separate from every possible input byte.

// Read the single input stream once and convert tokens without fmt reflection.
// Parse decimal input directly to avoid fmt's reflection and token allocations.
func integer() int {
	position, length := inputPosition, inputLength
	for {
		for position < length && inputBuffer[position] <= ' ' {
			position++
		}
		if position < length {
			break
		}
		length, _ = os.Stdin.Read(inputBuffer[:])
		position = 0
		if length == 0 {
			inputPosition, inputLength = 0, 0
			return 0
		}
	}
	negative := inputBuffer[position] == '-'
	if negative || inputBuffer[position] == '+' {
		position++
	}
	value := 0
	for {
		// Keep the cursor local until the number ends or the current block is exhausted.
		for position < length {
			ch := inputBuffer[position]
			if ch < '0' || ch > '9' {
				inputPosition, inputLength = position, length
				if negative {
					return value
				}
				return -value
			}
			value = value*10 - int(ch-'0')
			position++
		}
		length, _ = os.Stdin.Read(inputBuffer[:])
		position = 0
		if length == 0 {
			inputPosition, inputLength = 0, 0
			if negative {
				return value
			}
			return -value
		}
	}
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

// Only the fixed integer, character, string and decimal formats used here are needed.
