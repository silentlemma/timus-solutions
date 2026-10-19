package main

import (
	"fmt"
	"strings"
)

const (
	hosts   = 2 // Marshall and Lily
	unlucky = 13
	price   = 100
	plus    = "+one"
)

func main() {
	var n int
	fmt.Scan(&n)
	people := hosts
	for i := 0; i < n; i++ {
		var s string
		fmt.Scan(&s)
		if strings.HasSuffix(s, plus) {
			people += 2
		} else {
			people++
		}
	}
	if people == unlucky {
		people++ // a dummy takes the extra seat
	}
	fmt.Println(people * price)
}
