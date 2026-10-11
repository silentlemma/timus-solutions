package main

import (
	"bufio"
	"os"
	"strconv"
)

const largest = 25000

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		x, _ := strconv.Atoi(in.Text())
		return x
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	n := next()
	// counting each value is a sort in descending order, and printing the
	// conjugate partition twice gives back the sorted array
	count := make([]int, largest+1)
	for i := 0; i < n; i++ {
		count[next()]++
	}
	for value := largest; value >= 1; value-- {
		line := strconv.Itoa(value) + "\n"
		for k := 0; k < count[value]; k++ {
			out.WriteString(line)
		}
	}
}
