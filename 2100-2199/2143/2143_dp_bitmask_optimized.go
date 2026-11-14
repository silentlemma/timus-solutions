package main

import (
	"strconv"
	"syscall"
)

const sideSeats = 3
const rightStart = 6
const stateCount = 5
const unreachable = -1000
const maxRows = 100
const inputSize = 1024
const layoutLength = rightStart + sideSeats
const seatLabelBytes = 5 // three row digits, seat letter and newline
const outputSize = maxRows*2*sideSeats*seatLabelBytes + len("POBEDA\n")

var masks = [stateCount]byte{0, 1, 2, 1 << 2, 1 | (1 << 2)}
var people = [stateCount]int{0, 1, 1, 1, 2}

func arrange(rows []byte) int {
	var previous [maxRows][stateCount]byte
	scores := [stateCount]int{}
	for i := 1; i < stateCount; i++ {
		scores[i] = unreachable
	}
	for row, free := range rows {
		var next [stateCount]int
		for state, mask := range masks {
			next[state] = unreachable
			if mask&free != mask {
				continue
			}
			blocked := mask | mask<<1 | mask>>1
			best := 0
			for prior, other := range masks {
				if blocked&other == 0 && scores[prior] > scores[best] {
					best = prior
				}
			}
			next[state] = scores[best] + people[state]
			previous[row][state] = byte(best)
		}
		scores = next
	}
	state := 0
	for i, score := range scores {
		if score > scores[state] {
			state = i
		}
	}
	count := scores[state]
	for row := len(rows) - 1; row >= 0; row-- {
		rows[row] = masks[state]
		state = int(previous[row][state])
	}
	return count
}

const decimalBase = 10

type reader struct {
	data     [inputSize]byte
	pos, end int
}

func (r *reader) next() byte {
	if r.pos == r.end {
		for {
			n, err := syscall.Read(syscall.Stdin, r.data[:])
			if err == syscall.EINTR {
				continue
			}
			if n <= 0 {
				return 0
			}
			r.pos, r.end = 0, n
			break
		}
	}
	b := r.data[r.pos]
	r.pos++
	return b
}

func (r *reader) first() byte {
	for b := r.next(); b != 0; b = r.next() {
		if b > ' ' {
			return b
		}
	}
	return 0
}

func (r *reader) number() int {
	n := 0
	for b := r.first(); b >= '0' && b <= '9'; b = r.next() {
		n = n*decimalBase + int(b-'0')
	}
	return n
}

func write(data []byte) {
	for len(data) > 0 {
		n, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		data = data[n:]
	}
}

func main() {
	var input reader
	n := input.number()
	needed := input.number()
	if n < 1 || n > maxRows || needed < 1 {
		return
	}
	var rows [2][maxRows]byte
	for row := 0; row < n; row++ {
		var layout [layoutLength]byte
		layout[0] = input.first()
		for i := 1; i < len(layout); i++ {
			layout[i] = input.next()
		}
		for side := range rows {
			for column := 0; column < sideSeats; column++ {
				if layout[side*rightStart+column] == '.' {
					rows[side][row] |= 1 << column
				}
			}
		}
	}
	if arrange(rows[0][:n])+arrange(rows[1][:n]) < needed {
		write([]byte("PORAZHENIE\n"))
		return
	}
	var buffer [outputSize]byte
	output := append(buffer[:0], "POBEDA\n"...)
	for side, masks := range rows {
		for row, mask := range masks[:n] {
			for column := 0; column < sideSeats; column++ {
				if mask&(1<<column) != 0 {
					output = strconv.AppendInt(output, int64(row+1), decimalBase)
					output = append(output, byte('A'+side*sideSeats+column), '\n')
					needed--
					if needed == 0 {
						write(output)
						return
					}
				}
			}
		}
	}
}
