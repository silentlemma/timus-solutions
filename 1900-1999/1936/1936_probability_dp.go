package main

import (
	"bufio"
	"fmt"
	"os"
)

const gestureCount = 3
const outputDigits = 12

func expectedRounds(count int) float64 {
	expected := make([]float64, count+1)
	powerThree, powerTwo := 1.0, 2.0
	for players := 2; players <= count; players++ {
		powerThree *= gestureCount
		powerTwo *= 2
		weightedSuccessors, combination := 0.0, 1.0
		for survivors := 1; survivors < players; survivors++ {
			combination = combination * float64(players-survivors+1) / float64(survivors)
			weightedSuccessors += combination * expected[survivors]
		}
		expected[players] = (powerThree + weightedSuccessors) / (powerTwo - 2)
	}
	return expected[count]
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count int
	fmt.Fscan(input, &count)
	fmt.Printf("%.*f\n", outputDigits, expectedRounds(count))
}
