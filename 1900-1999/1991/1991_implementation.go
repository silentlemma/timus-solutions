package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := bufio.NewReader(os.Stdin)
	var count int
	var capacity, unused, survivors int64
	fmt.Fscan(input, &count, &capacity)
	for i := 0; i < count; i++ {
		var amount int64
		fmt.Fscan(input, &amount)
		if amount > capacity {
			unused += amount - capacity
		} else {
			survivors += capacity - amount
		}
	}
	fmt.Println(unused, survivors)
}
