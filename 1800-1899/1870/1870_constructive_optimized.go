package main

import (
	"bufio"
	"os"
	"strconv"
)

const divisorThree = 3

const digitsPerRow = 6

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	in.Scan()
	size, _ := strconv.Atoi(in.Text())
	if size%2 == 0 || size%divisorThree == 0 {
		os.Stdout.WriteString("No\n")
		return
	}

	out := bufio.NewWriter(os.Stdout)
	out.WriteString("Yes\n")
	var digits [digitsPerRow]byte
	// For odd size, the modular sequence visits the odd rows, then the even rows.
	for first := 1; first <= 2; first++ {
		for row := first; row <= size; row += 2 {
			if row != 1 {
				out.WriteByte(' ')
			}
			out.Write(strconv.AppendInt(digits[:0], int64(row), 10))
		}
	}
	out.WriteByte('\n')
	out.Flush()
}
