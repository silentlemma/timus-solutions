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

const inputSize = 256

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

const maxSide = 100
const maxCells = maxSide * maxSide
const letters = 26
const searches = 3
const infinity = uint16(65535)

var rows, columns, cells int
var grid [maxCells]byte
var heads [letters]uint16
var nextPortal [maxCells]uint16
var distances [searches][maxCells]uint16
var queue [maxCells]uint16

func isPortal(c byte) bool { return 'A' <= c && c <= 'Z' }

func bfs(run, start, forbidden int) {
	distance := &distances[run]
	for cell := 0; cell < cells; cell++ {
		distance[cell] = infinity
	}
	head, tail := 0, 0
	visit := func(cell int, day uint16) {
		if distance[cell] != infinity {
			return
		}
		if isPortal(grid[cell]) {
			// Expanding at discovery contracts the free group: each cell queues only once.
			for other := heads[grid[cell]-'A']; other != infinity; other = nextPortal[other] {
				distance[other] = day
				queue[tail] = other
				tail++
			}
		} else {
			distance[cell] = day
			queue[tail] = uint16(cell)
			tail++
		}
	}
	visit(start, 0)
	for head < tail {
		cell := int(queue[head])
		head++
		row, column := cell/columns, cell%columns
		for dr := -1; dr <= 1; dr++ {
			for dc := -1; dc <= 1; dc++ {
				r, c := row+dr, column+dc
				if (dr == 0 && dc == 0) || r < 0 || r >= rows || c < 0 || c >= columns {
					continue
				}
				other := r*columns + c
				if grid[other] != '#' && other != forbidden {
					visit(other, distance[cell]+1)
				}
			}
		}
	}
}

func main() {
	rows, columns = number(), number()
	cells = rows * columns
	for letter := range heads {
		heads[letter] = infinity
	}
	first, second, fortress := 0, 0, 0
	for cell := 0; cell < cells; cell++ {
		c := nextByte()
		for c != 0 && c <= ' ' {
			c = nextByte()
		}
		grid[cell] = c
		if c == '$' {
			first = cell
		} else if c == '!' {
			second = cell
		} else if c == '*' {
			fortress = cell
		} else if isPortal(c) {
			nextPortal[cell] = heads[c-'A']
			heads[c-'A'] = uint16(cell)
		}
	}
	bfs(0, first, fortress)
	bfs(1, second, fortress)
	bfs(searches-1, fortress, -1)
	answer := int(infinity)
	for cell := 0; cell < cells; cell++ {
		firstDay, secondDay := distances[0][cell], distances[1][cell]
		afterMeeting := distances[searches-1][cell]
		if cell == fortress || firstDay == infinity || secondDay == infinity || afterMeeting == infinity {
			continue
		}
		if secondDay > firstDay {
			firstDay = secondDay
		}
		total := int(firstDay) + int(afterMeeting)
		if total < answer {
			answer = total
		}
	}
	if answer == int(infinity) {
		used = copy(output[:], "Impossible")
	} else {
		writeNumber(answer)
	}
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
