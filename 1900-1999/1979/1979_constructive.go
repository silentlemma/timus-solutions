package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const faceCount = 6
const halfFaces = 3
const bandCount = 3
const beltFaces = 4

func label(n, band, row, col int) int {
	area := n * n
	complement := faceCount*area + 1
	if band == 0 {
		return 2*area + row*n + col + 1
	}
	if band == 2 {
		return complement - (halfFaces*area - row*n - n + col + 1)
	}
	face := col / n
	col %= n
	if face < 2 {
		return face*area + row*n + col + 1
	}
	return complement - ((face-2)*area + row*n + n - col)
}

func writeCube(n int, out *bufio.Writer) {
	for band := 0; band < bandCount; band++ {
		width := n
		if band == 1 {
			width = beltFaces * n
		}
		for row := 0; row < n; row++ {
			for col := 0; col < width; col++ {
				if col > 0 {
					out.WriteByte(' ')
				}
				out.WriteString(strconv.Itoa(label(n, band, row, col)))
			}
			out.WriteByte('\n')
		}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	out := bufio.NewWriter(os.Stdout)
	writeCube(n, out)
	out.Flush()
}
