package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	white = 255
	half  = 127 // the carried error always stays within [-127, 127]
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n, m := next(), next()
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	row, res := make([]int, m), make([]int, m)
	for i := 0; i < n; i++ {
		for j := range row {
			row[j] = next()
		}
		// carry the rounding error along the row, in alternate directions so
		// that a window at either side meets short prefixes in half its rows
		err := 0
		for k := 0; k < m; k++ {
			j := k
			if i%2 == 1 {
				j = m - 1 - k
			}
			err -= row[j]
			res[j] = 0
			if err < -half {
				err += white
				res[j] = white
			}
		}
		for j, v := range res {
			out.WriteString(strconv.Itoa(v))
			if j+1 < m {
				out.WriteByte(' ')
			} else {
				out.WriteByte('\n')
			}
		}
	}
}
