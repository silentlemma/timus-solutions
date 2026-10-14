package main

import "fmt"

func main() {
	var blue, red, yellow int64
	fmt.Scan(&blue, &red, &yellow)
	bags := map[string]int64{"Blue": blue, "Red": red, "Yellow": yellow}
	var k int
	fmt.Scan(&k)
	// one reagent from each needed bag, chosen independently
	ways := int64(1)
	for i := 0; i < k; i++ {
		var color string
		fmt.Scan(&color)
		ways *= bags[color]
	}
	fmt.Println(ways)
}
