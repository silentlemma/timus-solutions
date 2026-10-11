package main

import (
	"bufio"
	"fmt"
	"os"
)

const three = 3

func main() {
	in := bufio.NewReader(os.Stdin)
	readInt := func() int {
		c, _ := in.ReadByte()
		for c < '0' || c > '9' {
			c, _ = in.ReadByte()
		}
		v := 0
		for c >= '0' && c <= '9' {
			v = v*10 + int(c-'0')
			c, _ = in.ReadByte()
		}
		return v
	}
	n, m := readInt(), readInt()
	// every dark region is a rectangle exactly when no 2 x 2 window holds
	// three dark cells, so two rows are enough, and the image never fits in
	// 4 MB anyway
	prev, cur := make([]int, m), make([]int, m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			c, _ := in.ReadByte()
			for c != '0' && c != '1' {
				c, _ = in.ReadByte()
			}
			cur[j] = int(c - '0')
			if i > 0 && j > 0 && prev[j-1]+prev[j]+cur[j-1]+cur[j] == three {
				fmt.Println("No")
				return
			}
		}
		prev, cur = cur, prev
	}
	fmt.Println("Yes")
}
