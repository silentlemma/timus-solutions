package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

const bufSize = 1 << 20

func main() {
	reader := bufio.NewReaderSize(os.Stdin, bufSize)
	first, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(first))
	// the soldiers to turn, for an all-W parade
	turn := make([][]byte, n)
	for i := range turn {
		line, _ := reader.ReadString('\n')
		line = strings.TrimSpace(line)
		turn[i] = make([]byte, n)
		for j := 0; j < n; j++ {
			if line[j] == 'B' {
				turn[i][j] = 1
			}
		}
	}
	// pressing every cell of row a and column b turns only (a, b) when N is
	// even, so (i, j) is pressed when its row, its column and itself add up odd
	row, col := make([]byte, n), make([]byte, n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			row[i] ^= turn[i][j]
			col[j] ^= turn[i][j]
		}
	}
	total := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			total += int(row[i] ^ col[j] ^ turn[i][j])
		}
	}
	// an all-B parade needs exactly the other cells
	var flip byte
	if 2*total > n*n {
		flip, total = 1, n*n-total
	}
	out := strconv.AppendInt(nil, int64(total), 10)
	out = append(out, '\n')
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if row[i]^col[j]^turn[i][j] != flip {
				out = strconv.AppendInt(out, int64(i+1), 10)
				out = append(out, ' ')
				out = strconv.AppendInt(out, int64(j+1), 10)
				out = append(out, '\n')
			}
		}
	}
	os.Stdout.Write(out)
}
