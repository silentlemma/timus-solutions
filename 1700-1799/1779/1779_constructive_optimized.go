package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	outputSize = 24
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	if !in.Scan() {
		return
	}
	n, _ := strconv.Atoi(in.Text())
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var storage [outputSize]byte
	// Grouping by the larger endpoint gives floor(n/2) * ceil(n/2) pairs.
	left := n / 2
	out.Write(append(strconv.AppendInt(storage[:0], int64(left*(n-left)), 10), '\n'))
	for i := 1; i <= n; i++ {
		first := i + 1
		if first <= n-i {
			first = n - i + 1
		}
		prefix := append(strconv.AppendInt(storage[:0], int64(i), 10), ' ')
		for j := first; j <= n; j++ {
			line := strconv.AppendInt(prefix, int64(j), 10)
			out.Write(append(line, '\n'))
		}
	}
}
