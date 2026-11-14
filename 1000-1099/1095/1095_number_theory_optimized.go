package main

import (
	"bufio"
	"os"
	"strconv"
)

const divisor = 7
const keyLength = 4
const keyShift = 10000
const maxDigits = 20

var suffixes = [divisor]string{"3241", "1324", "1234", "2341", "1243", "1342", "2134"}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	input.Scan()
	count, _ := strconv.Atoi(input.Text())
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < count && input.Scan(); i++ {
		var answer [maxDigits + 1]byte
		var removed [keyLength]bool
		size, zeros, remainder := 0, 0, 0
		for _, digit := range input.Bytes() {
			switch {
			case digit == '0':
				zeros++
			case digit >= '1' && digit <= '4' && !removed[digit-'1']:
				removed[digit-'1'] = true
			default:
				answer[size] = digit
				size++
				remainder = (remainder*10 + int(digit-'0')) % divisor
			}
		}
		// Choose the four digits that cancel the shifted head remainder.
		needed := (divisor - remainder*keyShift%divisor) % divisor
		size += copy(answer[size:], suffixes[needed])
		for j := 0; j < zeros; j++ {
			answer[size] = '0'
			size++
		}
		answer[size] = '\n'
		out.Write(answer[:size+1])
	}
}
