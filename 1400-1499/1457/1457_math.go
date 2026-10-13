package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	sum := 0
	for i := 0; i < n; i++ {
		var p int
		fmt.Fscan(reader, &p)
		sum += p
	}
	// the mean of squared distances is smallest at the arithmetic mean
	fmt.Printf("%.6f\n", float64(sum)/float64(n))
}
