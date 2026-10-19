package main

import (
	"bufio"
	"fmt"
	"os"
)

const teamSize = 3

func waysToChoose(available, count int) int {
	if count < 0 || count > available {
		return 0
	}
	if count == 0 {
		return 1
	}
	if count == 1 {
		return available
	}
	return available * (available - 1) / 2
}

func countTeams(total, specialCount, firstSpecial int) int {
	special := specialCount - firstSpecial
	ordinary := total - specialCount - (1 - firstSpecial)
	remainingTeams := total/teamSize - 1
	answer := 0
	for chosenSpecial := 0; chosenSpecial < teamSize; chosenSpecial++ {
		removedSpecial := firstSpecial + chosenSpecial
		if removedSpecial == 0 || specialCount-removedSpecial < remainingTeams {
			continue
		}
		answer += waysToChoose(special, chosenSpecial) * waysToChoose(ordinary, teamSize-1-chosenSpecial)
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var total, specialCount int
	fmt.Fscan(input, &total, &specialCount)
	firstSpecial := 0
	for i := 0; i < specialCount; i++ {
		var identifier int
		fmt.Fscan(input, &identifier)
		if identifier == 1 {
			firstSpecial = 1
		}
	}
	fmt.Println(countTeams(total, specialCount, firstSpecial))
}
