package main

import (
	"math/bits"
	"syscall"
)

const corners = 3
const inputSize = 256
const decimal = 10

type point struct {
	x, y int64
}

var input [inputSize]byte
var start, end int

func nextByte() byte {
	if start == end {
		for {
			n, err := syscall.Read(syscall.Stdin, input[:])
			if err == syscall.EINTR {
				continue
			}
			if n <= 0 {
				return 0
			}
			start, end = 0, n
			break
		}
	}
	value := input[start]
	start++
	return value
}

func number() int64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := int64(1)
	if c == '-' || c == '+' {
		if c == '-' {
			sign = -1
		}
		c = nextByte()
	}
	var value int64
	for '0' <= c && c <= '9' {
		value = decimal*value + int64(c-'0')
		c = nextByte()
	}
	return sign * value
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

func reachesWall(centre, start, end, apex point, height, top, radius int64) bool {
	ux, uy := end.x-start.x, end.y-start.y
	nx, ny := uy*top, -ux*top
	nz := ux*(apex.y-start.y) - uy*(apex.x-start.x)
	reach := nx*(centre.x-start.x) + ny*(centre.y-start.y) + nz*height
	if reach < 0 {
		reach = -reach
	}
	distanceHigh, distanceLow := bits.Mul64(uint64(reach), uint64(reach))
	radiusHigh, radiusLow := bits.Mul64(uint64(radius*radius), uint64(nx*nx+ny*ny+nz*nz))
	return distanceHigh < radiusHigh || distanceHigh == radiusHigh && distanceLow <= radiusLow
}

func main() {
	mana, height, top := number(), number(), number()
	radius := mana - height
	if radius <= 0 {
		write([]byte("NO\n"))
		return
	}
	if radius >= height {
		write([]byte("YES\n"))
		return
	}

	centre := point{number(), number()}
	var base [corners]point
	for i := range base {
		base[i] = point{number(), number()}
	}
	apex := point{number(), number()}
	for i, start := range base {
		if reachesWall(centre, start, base[(i+1)%corners], apex, height, top, radius) {
			write([]byte("YES\n"))
			return
		}
	}
	write([]byte("NO\n"))
}
