package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const decimalBase = 10

func timesTen(value string) string {
	carry := 0
	result := make([]byte, 0, len(value))
	for i := len(value) - 1; i >= 0; i-- {
		carry += int(value[i]-'0') * decimalBase
		result = append(result, byte('0'+carry%2))
		carry /= 2
	}
	for carry > 0 {
		result = append(result, byte('0'+carry%2))
		carry /= 2
	}
	for left, right := 0, len(result)-1; left < right; left, right = left+1, right-1 {
		result[left], result[right] = result[right], result[left]
	}
	return string(result)
}

func optimalLengths(bits string) []int {
	powers := []string{}
	power := "1"
	end := len(bits)
	lengths := []int{}
	for end > 0 {
		index := 0
		for {
			if index == len(powers) {
				power = timesTen(power)
				powers = append(powers, power)
			}
			threshold := powers[index]
			length := len(threshold)
			if length >= end {
				lengths = append(lengths, end)
				for left, right := 0, len(lengths)-1; left < right; left, right = left+1, right-1 {
					lengths[left], lengths[right] = lengths[right], lengths[left]
				}
				return lengths
			}
			start := end - length
			if bits[start] == '1' && bits[start:end] < threshold {
				lengths = append(lengths, length)
				end = start
				break
			}
			index++
		}
	}
	for left, right := 0, len(lengths)-1; left < right; left, right = left+1, right-1 {
		lengths[left], lengths[right] = lengths[right], lengths[left]
	}
	return lengths
}

func makeBits(maximum int) string {
	var bits strings.Builder
	for value := 1; value <= maximum; value++ {
		bits.WriteString(strconv.FormatInt(int64(value), 2))
	}
	return bits.String()
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var maximum int
	fmt.Fscan(input, &maximum)
	lengths := optimalLengths(makeBits(maximum))
	fmt.Fprintln(output, len(lengths))
	for _, length := range lengths {
		fmt.Fprint(output, length, " ")
	}
	fmt.Fprintln(output)
}
