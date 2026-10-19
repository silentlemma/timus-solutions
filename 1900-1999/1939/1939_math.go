package main

import (
	"bufio"
	"fmt"
	"os"
)

func canCrash(length, height, gateHeight, speed, gateSpeed, deceleration int64) bool {
	stoppingBound := gateSpeed * (speed*speed + 2*deceleration*length)
	passingBound := 2 * deceleration * speed * (gateHeight - height)
	return stoppingBound >= passingBound
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var length, height, gateHeight, speed, gateSpeed, deceleration int64
	fmt.Fscan(input, &length, &height, &gateHeight, &speed, &gateSpeed, &deceleration)
	if canCrash(length, height, gateHeight, speed, gateSpeed, deceleration) {
		fmt.Println("Crash")
	} else {
		fmt.Println("Safe")
	}
}
