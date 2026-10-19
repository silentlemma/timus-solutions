package main

import "fmt"

const legs = 40

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// either every right slipper turns up while the left legs are dressed,
	// or 39 rights do, and then every spare left slipper is thrown away
	// before the last right leg is dressed
	worst := 2*b + legs
	if 2*a+legs-1 > worst {
		worst = 2*a + legs - 1
	}
	fmt.Println(worst)
}
