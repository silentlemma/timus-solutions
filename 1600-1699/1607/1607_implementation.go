package main

import "fmt"

func main() {
	var a, b, c, d int
	if _, err := fmt.Scan(&a, &b, &c, &d); err != nil {
		return
	}
	petya, driver := a, c
	// the driver never asks less than Petya offers, and the other way round
	if petya >= driver {
		fmt.Println(petya)
		return
	}
	for {
		petya += b
		if petya >= driver {
			fmt.Println(driver)
			return
		}
		driver -= d
		if driver <= petya {
			fmt.Println(petya)
			return
		}
	}
}
