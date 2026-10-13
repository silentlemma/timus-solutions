package main

import (
	"bufio"
	"fmt"
	"os"
)

const full = 100 // brightness is given in percent

func main() {
	var n, b int
	fmt.Scan(&n, &b)
	// lamp i is on when floor((i + 1) b / 100) grows: every stretch then holds
	// less than one lamp more or less than L b / 100, and the pattern repeats
	row := make([]byte, n+1)
	for i := 0; i < n; i++ {
		row[i] = '0'
		if (i%full+1)*b/full > i%full*b/full {
			row[i] = '1'
		}
	}
	row[n] = '\n'
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	writer.Write(row)
}
