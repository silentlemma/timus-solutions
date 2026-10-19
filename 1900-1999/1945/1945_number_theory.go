package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	primeThree     = 3
	primeFive      = 5
	maxThreeWeight = 3
	fiveWeight     = 4
)

func hall(value, groups int) int {
	threeWeight := groups - 1
	if threeWeight > maxThreeWeight {
		threeWeight = maxThreeWeight
	}
	primes := [...]int{2, primeThree, primeFive}
	weights := [...]int{1, threeWeight, fiveWeight}
	color := 0
	for index, prime := range primes {
		for value%prime == 0 {
			value /= prime
			color += weights[index]
		}
	}
	return color%groups + 1
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var size, groups int
	fmt.Fscan(in, &size, &groups)
	fmt.Fprintln(out, "Yes")
	for index := 0; index < size; index++ {
		var value int
		fmt.Fscan(in, &value)
		fmt.Fprintln(out, hall(value, groups))
	}
}
