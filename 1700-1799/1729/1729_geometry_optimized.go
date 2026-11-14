package main

import (
	"math"
	"syscall"
)

const (
	inputCapacity  = 32
	outputCapacity = 24
	decimal        = 10
	thousand       = 1000
	halfTurn       = 180 * thousand
	outputScale    = 10000000
)

func readValues() (int, int) {
	var input [inputCapacity]byte
	var values [2]int
	index, scale := 0, thousand
	reading, fractional := false, false
	for {
		size, err := syscall.Read(syscall.Stdin, input[:])
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return values[0], values[1]
		}
		for _, c := range input[:size] {
			switch {
			case c >= '0' && c <= '9':
				reading = true
				digit := int(c - '0')
				if fractional {
					scale /= decimal
					values[index] += scale * digit
				} else {
					values[index] = values[index]*decimal + thousand*digit
				}
			case c == '.':
				fractional = true
			case c <= ' ' && reading:
				index++
				if index == len(values) {
					return values[0], values[1]
				}
				scale, reading, fractional = thousand, false, false
			}
		}
		if err != nil {
			return values[0], values[1]
		}
	}
}

func writeDistance(distance float64) {
	digits := uint64(math.Round(distance * outputScale))
	whole, fractional := digits/outputScale, digits%outputScale
	var output [outputCapacity]byte
	end := len(output) - 1
	output[end] = '\n'
	for scale := outputScale; scale > 1; scale /= decimal {
		end--
		output[end] = '0' + byte(fractional%decimal)
		fractional /= decimal
	}
	end--
	output[end] = '.'
	for {
		end--
		output[end] = '0' + byte(whole%decimal)
		whole /= decimal
		if whole == 0 {
			break
		}
	}
	for rest := output[end:]; len(rest) > 0; {
		size, err := syscall.Write(syscall.Stdout, rest)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return
		}
		rest = rest[size:]
	}
}

func main() {
	scaledRadius, angle := readValues()
	radius := float64(scaledRadius) / thousand
	fullChords, rest := halfTurn/angle-1, halfTurn%angle
	const radiansPerUnit = math.Pi / halfTurn
	shore := float64(fullChords)*math.Sin(float64(angle)*radiansPerUnit) +
		math.Sin(float64(rest)*radiansPerUnit)
	writeDistance(radius + 2*radius*shore)
}
