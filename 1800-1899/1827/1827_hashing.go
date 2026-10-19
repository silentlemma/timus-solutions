package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	longest = 50
	shift   = 28 // star counts fit in 28 bits
	bufSize = 1 << 20
)

func main() {
	sc := bufio.NewScanner(bufio.NewReaderSize(os.Stdin, bufSize))
	sc.Buffer(make([]byte, bufSize), bufSize)
	sc.Split(bufio.ScanWords)
	readInt := func() uint64 {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return uint64(v)
	}
	n := int(readInt())
	stars := make([]uint64, n)
	for i := range stars {
		stars[i] = readInt()
	}
	m := int(readInt())
	wanted := make([]map[uint64]bool, longest+1)
	for i := 0; i < m; i++ {
		x, y, d := readInt(), readInt(), int(readInt())
		if wanted[d] == nil {
			wanted[d] = map[uint64]bool{}
		}
		wanted[d][x<<shift|y] = true
	}
	// a war of d days ending k days ago began k + d - 1 days ago; reach[k]
	// is the oldest day of a matching war that ends k days ago
	reach := make([]int, n)
	for k := range reach {
		reach[k] = -1
	}
	for d := 2; d <= longest && d <= n; d++ {
		if wanted[d] == nil {
			continue
		}
		for k := 0; k+d <= n; k++ {
			if wanted[d][stars[k+d-1]<<shift|stars[k]] && reach[k] < k+d-1 {
				reach[k] = k + d - 1
			}
		}
	}
	out := make([]byte, n)
	cover := -1
	for k := 0; k < n; k++ {
		if reach[k] > cover {
			cover = reach[k]
		}
		out[k] = '0'
		if cover >= k {
			out[k] = '1'
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.Write(out)
	w.WriteByte('\n')
}
