package main

import (
	"math"
	"math/bits"
	"strconv"
	"syscall"
)

const (
	eps         = 1e-6
	sky         = 1000000
	decimal     = 10
	crossTerm   = 4
	floatBits   = 64
	maxSide     = 50
	maxCells    = maxSide * maxSide
	inputSize   = 4096
	outputSize  = 32
	stationCell = -1
)

type station struct {
	row, col, height int16
	reach            int64
}

var terrain [maxCells]int16
var entries [maxCells]station
var bands [maxCells]int64

type reader struct {
	data       [inputSize]byte
	start, end int
	token      []byte
}

func (r *reader) next() byte {
	for r.start == r.end {
		n, err := syscall.Read(syscall.Stdin, r.data[:])
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return 0
		}
		r.start, r.end = 0, n
	}
	c := r.data[r.start]
	r.start++
	return c
}

func (r *reader) first() byte {
	c := r.next()
	for c != 0 && c <= ' ' {
		c = r.next()
	}
	return c
}

func (r *reader) number() int {
	value := 0
	for c := r.first(); c > ' '; c = r.next() {
		value = value*decimal + int(c-'0')
	}
	return value
}

func (r *reader) radius() float64 {
	r.token = r.token[:0]
	for c := r.first(); c > ' '; c = r.next() {
		r.token = append(r.token, c)
	}
	value, _ := strconv.ParseFloat(string(r.token), floatBits)
	return value
}

func square(value int64) int64 {
	return value * value
}

func contains(outer, inner station) bool {
	separation := square(int64(outer.row-inner.row)) +
		square(int64(outer.col-inner.col)) + square(int64(outer.height-inner.height))
	margin := outer.reach - inner.reach - separation
	if margin < 0 {
		return false
	}
	// Compare the squares exactly even for the largest radius.
	leftHigh, leftLow := bits.Mul64(uint64(margin), uint64(margin))
	rightHigh, rightLow := bits.Mul64(crossTerm*uint64(inner.reach), uint64(separation))
	return leftHigh > rightHigh || (leftHigh == rightHigh && leftLow >= rightLow)
}

func placements(rows, cols int, heights []int16, stations []station) int64 {
	if len(stations) > 0 {
		nearest := 0
		for index, s := range stations {
			if s.reach < stations[nearest].reach {
				nearest = index
			}
		}
		stations[0], stations[nearest] = stations[nearest], stations[0]
		inner := stations[0]
		essential := stations[:1]
		for _, s := range stations[1:] {
			if !contains(s, inner) {
				essential = append(essential, s)
			}
		}
		stations = essential
	}
	var total int64
	for row := 0; row < rows; row++ {
		for index, s := range stations {
			bands[index] = s.reach - square(int64(row-int(s.row)))
		}
		for col := 0; col < cols; col++ {
			cell := row*cols + col
			if heights[cell] == stationCell {
				continue
			}
			low, high := int64(heights[cell]), int64(sky)
			for index, s := range stations {
				reach := bands[index] - square(int64(col-int(s.col)))
				height := int64(s.height)
				if reach < 0 {
					high = -1
					break
				}
				if square(low-height) <= reach && square(high-height) <= reach {
					continue
				}
				extent := int64(math.Sqrt(float64(reach)))
				if extent*extent > reach {
					extent--
				}
				if height-extent > low {
					low = height - extent
				}
				if height+extent < high {
					high = height + extent
				}
				if low > high {
					break
				}
			}
			if low <= high {
				total += high - low + 1
			}
		}
	}
	return total
}

func main() {
	var input reader
	rows, cols, count := input.number(), input.number(), input.number()
	heights := terrain[:rows*cols]
	for index := range heights {
		heights[index] = int16(input.number())
	}
	stations := entries[:count]
	for index := range stations {
		row, col := input.number()-1, input.number()-1
		radius := input.radius()
		cell := row*cols + col
		stations[index] = station{int16(row), int16(col), heights[cell], int64(radius*radius + eps)}
		// The station retains its altitude and the cell marks itself as occupied.
		heights[cell] = stationCell
	}
	total := placements(rows, cols, heights, stations)
	var digits [outputSize]byte
	output := append(strconv.AppendInt(digits[:0], total, decimal), '\n')
	for len(output) > 0 {
		n, err := syscall.Write(syscall.Stdout, output)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		output = output[n:]
	}
}
