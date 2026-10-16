package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var k, n int
	if _, err := fmt.Fscan(reader, &k, &n); err != nil {
		return
	}
	jam := 0
	for i := 0; i < n; i++ {
		var cars int
		fmt.Fscan(reader, &cars)
		// the light lets k cars through, but never more than are waiting
		jam += cars - k
		if jam < 0 {
			jam = 0
		}
	}
	fmt.Println(jam)
}
