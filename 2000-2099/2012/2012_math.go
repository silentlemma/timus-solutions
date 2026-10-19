package main

import (
	"fmt"
	"os"
)

const totalTasks = 12
const firstHourMinutes = 60
const minutesPerTask = 45
const contestMinutes = 300

func solve(firstHour int) bool {
	return firstHourMinutes+(totalTasks-firstHour)*minutesPerTask <= contestMinutes
}

func main() {
	var firstHour int
	fmt.Fscan(os.Stdin, &firstHour)
	if solve(firstHour) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
