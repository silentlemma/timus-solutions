package main

import "fmt"

func shortage(need, have int64) int64 {
	if need > have {
		return need - have
	}
	return 0
}

func main() {
	var a, b, c, x, y, z int64
	fmt.Scan(&a, &b, &c, &x, &y, &z)
	// the dual lands first cover what the red and blue lands miss, and every
	// land left over pays for the mana of any color
	missing := shortage(x, a) + shortage(y, b)
	if missing <= c && a+b+c >= x+y+z {
		fmt.Println("It is a kind of magic")
	} else {
		fmt.Println("There are no miracles in life")
	}
}
