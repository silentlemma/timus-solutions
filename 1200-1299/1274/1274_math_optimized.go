package main

import (
	"bufio"
	"bytes"
	"os"
	"strconv"
)

const lineBufferSize = 64

func digits(field []byte) int64 {
	var value int64
	for _, digit := range field {
		value = value*10 + int64(digit-'0')
	}
	return value
}

func readOperand(input *bufio.Reader) (int64, int64) {
	line, _ := input.ReadSlice('\n')
	line = bytes.TrimSpace(line)
	sign := int64(1)
	if line[0] == '-' {
		sign = -1
		line = line[1:]
	}
	slash := bytes.IndexByte(line, '/')
	if slash < 0 {
		return sign * digits(line), 1
	}
	denominator := digits(line[slash+1:])
	whole := int64(0)
	fraction := line[:slash]
	if space := bytes.IndexAny(fraction, " \t"); space >= 0 {
		whole = digits(fraction[:space])
		fraction = bytes.TrimSpace(fraction[space+1:])
	}
	return sign * (whole*denominator + digits(fraction)), denominator
}

func main() {
	input := bufio.NewReaderSize(os.Stdin, lineBufferSize)
	leftNum, leftDen := readOperand(input)
	line, _ := input.ReadSlice('\n')
	operation := bytes.TrimSpace(line)[0]
	rightNum, rightDen := readOperand(input)

	var num, den int64
	switch operation {
	case '+':
		num, den = leftNum*rightDen+rightNum*leftDen, leftDen*rightDen
	case '-':
		num, den = leftNum*rightDen-rightNum*leftDen, leftDen*rightDen
	case '*':
		num, den = leftNum*rightNum, leftDen*rightDen
	case '/':
		num, den = leftNum*rightDen, leftDen*rightNum
	}
	if den < 0 {
		num, den = -num, -den
	}
	var storage [lineBufferSize]byte
	output := storage[:0]
	if num < 0 {
		output = append(output, '-')
		num = -num
	}
	a, b := num, den
	for b != 0 {
		a, b = b, a%b
	}
	num, den = num/a, den/a
	whole, remainder := num/den, num%den
	if whole != 0 || remainder == 0 {
		output = strconv.AppendInt(output, whole, 10)
	}
	if remainder != 0 {
		if whole != 0 {
			output = append(output, ' ')
		}
		output = strconv.AppendInt(output, remainder, 10)
		output = append(output, '/')
		output = strconv.AppendInt(output, den, 10)
	}
	os.Stdout.Write(append(output, '\n'))
}
