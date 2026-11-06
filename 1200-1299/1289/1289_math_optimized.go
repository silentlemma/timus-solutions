package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	blockSize = 1024
)

func writeDigits(out *bufio.Writer, digit byte, count int) {
	var block [blockSize]byte
	for i := range block {
		block[i] = digit
	}
	for count >= len(block) {
		out.Write(block[:])
		count -= len(block)
	}
	out.Write(block[:count])
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	if !in.Scan() {
		return
	}
	n, _ := strconv.Atoi(in.Text())
	half := n / 2
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	switch half {
	case 0:
		out.WriteString("1\n")
	case 1:
		out.WriteString("10\n")
	default:
		// Stream the runs in 1 + 9 k², where k is a string of half ones.
		writeDigits(out, '1', half-1)
		out.WriteByte('0')
		writeDigits(out, '8', half-2)
		out.WriteString("90\n")
	}
}
