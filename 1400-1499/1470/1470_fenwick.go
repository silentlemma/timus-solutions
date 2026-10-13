package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	add    = 1 // record kinds; any other kind ends the input
	ask    = 2
	buffer = 1 << 20
)

var n, side int
var tree []int64 // a 3D Fenwick tree, indices from 1

func update(x, y, z int, k int64) {
	for i := x; i <= n; i += i & -i {
		for j := y; j <= n; j += j & -j {
			row := tree[(i*side+j)*side:]
			for w := z; w <= n; w += w & -w {
				row[w] += k
			}
		}
	}
}

func prefix(x, y, z int) int64 {
	var total int64
	for i := x; i > 0; i -= i & -i {
		for j := y; j > 0; j -= j & -j {
			row := tree[(i*side+j)*side:]
			for w := z; w > 0; w -= w & -w {
				total += row[w]
			}
		}
	}
	return total
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, buffer)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	readInt := func() int {
		x, sign := 0, 1
		c, _ := reader.ReadByte()
		for c != '-' && (c < '0' || c > '9') {
			c, _ = reader.ReadByte()
		}
		if c == '-' {
			sign = -1
			c, _ = reader.ReadByte()
		}
		for c >= '0' && c <= '9' {
			x = x*10 + int(c-'0')
			var err error
			if c, err = reader.ReadByte(); err != nil {
				break
			}
		}
		return sign * x
	}
	n = readInt()
	side = n + 1
	tree = make([]int64, side*side*side)
	for {
		kind := readInt()
		if kind == add {
			x, y, z := readInt(), readInt(), readInt()
			update(x+1, y+1, z+1, int64(readInt()))
		} else if kind == ask {
			x1, y1, z1 := readInt(), readInt(), readInt()
			x2, y2, z2 := readInt()+1, readInt()+1, readInt()+1
			// inclusion and exclusion over the eight corners of the box
			total := prefix(x2, y2, z2) - prefix(x1, y2, z2) - prefix(x2, y1, z2) -
				prefix(x2, y2, z1) + prefix(x1, y1, z2) + prefix(x1, y2, z1) +
				prefix(x2, y1, z1) - prefix(x1, y1, z1)
			writer.WriteString(strconv.FormatInt(total, 10) + "\n")
		} else {
			return
		}
	}
}
