package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const (
	indexBits = 10
	indexMask = 1<<indexBits - 1
	fieldSize = 8
	decimal   = 10
)

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	size := nextInt(input)
	ordered := make([]int, size)
	for i := range ordered {
		ordered[i] = nextInt(input)<<indexBits | (i + 1)
	}
	sort.Ints(ordered)
	sizes := make([]int, 0, size)
	for count := 1; count <= size; count++ {
		if ordered[count-1]>>indexBits <= count &&
			(count == size || ordered[count]>>indexBits > count+1) {
			sizes = append(sizes, count)
		}
	}
	output := bufio.NewWriter(os.Stdout)
	var buffer [fieldSize]byte
	output.Write(strconv.AppendInt(buffer[:0], int64(len(sizes)), decimal))
	output.WriteByte('\n')
	for _, count := range sizes {
		output.Write(strconv.AppendInt(buffer[:0], int64(count), decimal))
		for _, member := range ordered[:count] {
			output.WriteByte(' ')
			output.Write(strconv.AppendInt(buffer[:0], int64(member&indexMask), decimal))
		}
		output.WriteByte('\n')
	}
	output.Flush()
}
