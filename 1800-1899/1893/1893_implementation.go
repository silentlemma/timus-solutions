package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const premiumLast = 2
const businessLast = 20

func main() {
	var seat string
	fmt.Fscan(os.Stdin, &seat)
	row, _ := strconv.Atoi(seat[:len(seat)-1])
	letter := seat[len(seat)-1:]
	var rightWindow, aisles string
	if row <= premiumLast {
		rightWindow, aisles = "D", "BC"
	} else if row <= businessLast {
		rightWindow, aisles = "F", "BCDE"
	} else {
		rightWindow, aisles = "K", "CDGH"
	}
	if letter == "A" || letter == rightWindow {
		fmt.Println("window")
	} else if strings.Contains(aisles, letter) {
		fmt.Println("aisle")
	} else {
		fmt.Println("neither")
	}
}
