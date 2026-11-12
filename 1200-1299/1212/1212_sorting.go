package main

import (
	"sort"
	"syscall"
)

const (
	maxShips   = 30
	maxLength  = 4
	maxAnchors = maxShips * (maxLength + 2) * (maxLength + 2)
	inputSize  = 128
	maxDigits  = 10
)

type zone struct{ top, bottom, left, right int }

type anchorIDs []uint32

func (ids anchorIDs) Len() int           { return len(ids) }
func (ids anchorIDs) Less(i, j int) bool { return ids[i] < ids[j] }
func (ids anchorIDs) Swap(i, j int)      { ids[i], ids[j] = ids[j], ids[i] }

var zones [maxShips]zone
var blocked [maxAnchors]uint32
var ships, length int
var input [inputSize]byte
var position, available int

func nextByte() byte {
	for position == available {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, available = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func nonSpace() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	return c
}

func nextInt() int {
	value := 0
	for c := nonSpace(); c >= '0' && c <= '9'; c = nextByte() {
		value = value*10 + int(c-'0')
	}
	return value
}

func writeAnswer(answer int64) {
	var output [maxDigits + 1]byte
	start := maxDigits
	output[start] = '\n'
	for {
		start--
		output[start] = '0' + byte(answer%10)
		answer /= 10
		if answer == 0 {
			break
		}
	}
	remaining := output[start:]
	for len(remaining) > 0 {
		count, err := syscall.Write(syscall.Stdout, remaining)
		if count > 0 {
			remaining = remaining[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return
		}
	}
}

func countLines(rows, cols int, flipped bool) int64 {
	if cols < length {
		return 0
	}
	used := 0
	for i := 0; i < ships; i++ {
		z := zones[i]
		if flipped {
			z = zone{z.left, z.right, z.top, z.bottom}
		}
		top, bottom, left, right := z.top, z.bottom, z.left-length+1, z.right
		if top < 1 {
			top = 1
		}
		if bottom > rows {
			bottom = rows
		}
		if left < 1 {
			left = 1
		}
		if right > cols-length+1 {
			right = cols - length + 1
		}
		// Each existing ship excludes at most 36 anchors, not a whole board scan.
		for row := top; row <= bottom; row++ {
			for col := left; col <= right; col++ {
				blocked[used] = uint32((row-1)*cols + col - 1)
				used++
			}
		}
	}
	sort.Sort(anchorIDs(blocked[:used]))
	distinct := 0
	for i := 0; i < used; i++ {
		if i == 0 || blocked[i] != blocked[i-1] {
			distinct++
		}
	}
	return int64(rows)*int64(cols-length+1) - int64(distinct)
}

func main() {
	rows, cols := nextInt(), nextInt()
	ships = nextInt()
	for i := 0; i < ships; i++ {
		col, row, size := nextInt(), nextInt(), nextInt()
		way := nonSpace()
		bottom, right := row, col
		if way == 'V' {
			bottom += size - 1
		} else {
			right += size - 1
		}
		zones[i] = zone{row - 1, bottom + 1, col - 1, right + 1}
	}
	length = nextInt()
	answer := countLines(rows, cols, false)
	if length > 1 {
		answer += countLines(cols, rows, true)
	}
	writeAnswer(answer)
}
