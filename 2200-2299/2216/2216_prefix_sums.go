package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	nextInt := func() int {
		for position < len(data) && data[position] <= ' ' {
			position++
		}
		value := 0
		for position < len(data) && data[position] >= '0' && data[position] <= '9' {
			value = value*10 + int(data[position]-'0')
			position++
		}
		return value
	}

	floors, elevators := nextInt(), nextInt()
	difference := make([]int, floors+1)
	for i := 0; i < elevators; i++ {
		left, right := nextInt(), nextInt()
		difference[left]++
		difference[right]--
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if floors == 1 {
		fmt.Fprintln(out, -1)
		return
	}

	crossing, answer := 0, elevators
	// Every route crosses each gap; cover all elevators crossing the cheapest gap.
	for floor := 1; floor < floors; floor++ {
		crossing += difference[floor]
		if crossing < answer {
			answer = crossing
		}
	}
	fmt.Fprintln(out, answer)
}
