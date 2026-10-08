package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const (
	decimals  = 4
	floatBits = 64
	lineBytes = 32
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var nums []uint64
	var cur uint64
	inNumber := false
	for {
		c, err := reader.ReadByte()
		if err == nil && c >= '0' && c <= '9' {
			cur = cur*10 + uint64(c-'0')
			inNumber = true
			continue
		}
		if inNumber {
			nums = append(nums, cur)
			cur, inNumber = 0, false
		}
		if err != nil {
			break
		}
	}

	buf := make([]byte, 0, lineBytes)
	for i := len(nums) - 1; i >= 0; i-- {
		buf = strconv.AppendFloat(buf[:0], math.Sqrt(float64(nums[i])), 'f', decimals, floatBits)
		buf = append(buf, '\n')
		writer.Write(buf)
	}
}
