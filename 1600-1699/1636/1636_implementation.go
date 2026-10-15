package main

import "fmt"

const (
	problems   = 10
	perAttempt = 20 // minutes for each rejected attempt
)

func main() {
	var t1, t2 int
	if _, err := fmt.Scan(&t1, &t2); err != nil {
		return
	}
	clean := t2
	for i := 0; i < problems; i++ {
		var attempts int
		fmt.Scan(&attempts)
		clean -= perAttempt * attempts
	}
	// without the rejected attempts ZZZ wins only with strictly less time
	if clean < t1 {
		fmt.Println("Dirty debug :(")
	} else {
		fmt.Println("No chance.")
	}
}
