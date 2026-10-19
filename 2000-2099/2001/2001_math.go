package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(first, second, emptyFirst, emptySecond int) (int, int) {
	return first - emptyFirst, second - emptySecond
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var a1, b1, a2, b2, a3, b3 int
	fmt.Fscan(input, &a1, &b1, &a2, &b2, &a3, &b3)
	first, second := solve(a1, b1, a3, b2)
	fmt.Println(first, second)
}
