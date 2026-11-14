package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	corners    = 3
	inner      = 0.5
	outer      = -1.5
	digits     = 10
	floatBits  = 64
	bufferSize = 512
)

func coordinate(input *bufio.Scanner) float64 {
	input.Scan()
	value, _ := strconv.ParseFloat(input.Text(), floatBits)
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var scan [bufferSize]byte
	input.Buffer(scan[:], bufio.MaxScanTokenSize)
	input.Split(bufio.ScanWords)
	var points [corners][2]float64
	x, y := 0.0, 0.0
	for i := range points {
		px, py := coordinate(input), coordinate(input)
		points[i] = [2]float64{px, py}
		x += px
		y += py
	}
	x, y = x/corners, y/corners
	var buffer [bufferSize]byte
	output := buffer[:0]
	for _, scale := range [...]float64{inner, outer} {
		for _, point := range points {
			output = strconv.AppendFloat(output, x+scale*(point[0]-x), 'f', digits, floatBits)
			output = append(output, ' ')
			output = strconv.AppendFloat(output, y+scale*(point[1]-y), 'f', digits, floatBits)
			output = append(output, '\n')
		}
	}
	os.Stdout.Write(output)
}
