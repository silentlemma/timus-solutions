package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// a turning pair "><" becomes "<>", a swap of neighbours that removes one
	// pair with '>' before '<', so the count of such pairs is the answer
	right, turns := int64(0), int64(0)
	for seen := 0; seen < n; {
		c, err := in.ReadByte()
		if err != nil {
			break
		}
		if c == '>' {
			right++
			seen++
		} else if c == '<' {
			turns += right
			seen++
		}
	}
	fmt.Println(turns)
}
