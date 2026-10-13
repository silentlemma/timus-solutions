package main

import (
	"bufio"
	"fmt"
	"os"
)

const buffer = 1 << 20

func main() {
	reader := bufio.NewReaderSize(os.Stdin, buffer)
	readInt := func() int {
		x := 0
		c, _ := reader.ReadByte()
		for c < '0' || c > '9' {
			c, _ = reader.ReadByte()
		}
		for c >= '0' && c <= '9' {
			x = x*10 + int(c-'0')
			var err error
			if c, err = reader.ReadByte(); err != nil {
				break
			}
		}
		return x
	}
	n := readInt()
	taken := make([]int, n)
	for i := range taken {
		taken[i] = readInt()
	}
	// the pocket is a stack: roll the balls in order, and whenever the top
	// one is the next ball the inspector took out, take it out
	var pocket []int
	next := 0
	for ball := 1; ball <= n; ball++ {
		pocket = append(pocket, ball)
		for len(pocket) > 0 && next < n && pocket[len(pocket)-1] == taken[next] {
			pocket = pocket[:len(pocket)-1]
			next++
		}
	}
	if next == n {
		fmt.Println("Not a proof")
	} else {
		fmt.Println("Cheater")
	}
}
