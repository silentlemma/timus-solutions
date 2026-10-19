package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(x, y, total int64) (int64, int64, bool) {
	a := x
	if total < a {
		a = total
	}
	b := total - a
	return a, b, b <= y
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var x, y, total int64
	if _, err := fmt.Fscan(input, &x, &y, &total); err != nil {
		return
	}
	a, b, ok := solve(x, y, total)
	if ok {
		fmt.Println(a, b)
	} else {
		fmt.Println("Impossible")
	}
}
