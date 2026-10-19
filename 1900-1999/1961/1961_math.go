package main

import (
	"bufio"
	"fmt"
	"os"
)

func bestCount(sample, successes, population int64) int64 {
	answer := successes * (population + 1) / sample
	if answer > population {
		return population
	}
	return answer
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var sample, successes, population int64
	fmt.Fscan(in, &sample, &successes, &population)
	fmt.Println(bestCount(sample, successes, population))
}
