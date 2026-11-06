package main

import "os"

const (
	inputSize       = 64
	outputSize      = 40
	maxDigits       = 20
	knownQuantities = 3
	names           = "pVnT"
	decimals        = int64(1000000)
)

var scale = [len(names)]int64{1000, 1000, 8314, 8314}
var input [inputSize]byte
var inputPosition, inputLength int

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func symbol() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	return c
}

func number() int64 {
	c := symbol()
	value := int64(0)
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	return value
}

func appendNumber(output []byte, value int64) []byte {
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
	return append(output, digits[first:]...)
}

func main() {
	var value [len(names)]int64
	var present [len(names)]bool
	for assignment := 0; assignment < knownQuantities; assignment++ {
		name := symbol()
		index := 0
		for names[index] != name {
			index++
		}
		symbol() // equals sign
		value[index] = number()
		present[index] = true
	}
	missing := 0
	for present[missing] {
		missing++
	}
	// Isolate the missing quantity from 1000pV = 8314nT.
	divisor := scale[missing] * value[missing^1]
	other := missing ^ 2
	numerator := scale[other] * value[other] * value[other^1]
	if divisor == 0 && numerator == 0 {
		os.Stdout.WriteString("undefined\n")
		return
	}
	if divisor == 0 || (numerator == 0 && missing%2 == 1) {
		os.Stdout.WriteString("error\n")
		return
	}
	var storage [outputSize]byte
	output := append(storage[:0], names[missing], ' ', '=', ' ')
	rounded := (numerator*decimals + divisor/2) / divisor
	output = append(appendNumber(output, rounded/decimals), '.')
	for place := decimals / 10; place > 0; place /= 10 {
		output = append(output, '0'+byte(rounded/place%10))
	}
	os.Stdout.Write(append(output, '\n'))
}
