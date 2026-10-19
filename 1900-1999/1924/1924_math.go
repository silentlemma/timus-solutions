package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := bufio.NewReader(os.Stdin)
	var size int
	fmt.Fscan(input, &size)
	total := size * (size + 1) / 2
	if total%2 == 0 {
		fmt.Println("black")
	} else {
		fmt.Println("grimy")
	}
}
