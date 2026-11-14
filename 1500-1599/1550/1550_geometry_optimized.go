package main

import (
	"math"
	"strconv"
	"syscall"
)

const (
	outputSize = 32
	bufferSize = 256
	precision  = 5
	floatBits  = 64
	third      = 1.0 / 3
)

func next(data []byte, cursor *int) float64 {
	i := *cursor
	for i < len(data) && data[i] <= ' ' {
		i++
	}
	start := i
	for i < len(data) && data[i] > ' ' {
		i++
	}
	*cursor = i
	value, _ := strconv.ParseFloat(string(data[start:i]), floatBits)
	return value
}

func readInput() []byte {
	var block [bufferSize]byte
	size := 0
	for size < len(block) {
		count, err := syscall.Read(syscall.Stdin, block[size:])
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return block[:size]
		}
		size += count
	}
	data := append([]byte(nil), block[:]...)
	for {
		count, err := syscall.Read(syscall.Stdin, block[:])
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return data
		}
		data = append(data, block[:count]...)
	}
}

func writeOutput(data []byte) {
	for len(data) != 0 {
		count, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return
		}
		data = data[count:]
	}
}

func main() {
	data := readInput()
	pos := 0
	h, w := next(data, &pos), next(data, &pos)
	x, y, r := next(data, &pos), next(data, &pos), next(data, &pos)
	centre := h * (1 - 2*math.Max(math.Abs(x), math.Abs(y))/w)
	volume := h*w*w*third - math.Pi*r*r*centre
	var output [outputSize]byte
	result := strconv.AppendFloat(output[:0], volume, 'f', precision, floatBits)
	writeOutput(append(result, '\n'))
}
