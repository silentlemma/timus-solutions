package main

import (
	"fmt"
	"strings"
)

const (
	oneDigit = 4 // floors 1 to 5 show every indicator lit and unlit

	short = 5 // blocks of the second digit: 6 through 9, 0 to 2
	long  = 7 // blocks of the second digit: 2 to 9, 0

	lowTop = 3 // a leading digit up to this needs blank, 1, 2 on top
	wide   = 3 // blocks of the leading digit otherwise: blank through 4
)

func main() {
	var n string
	fmt.Scan(&n)
	digits := len(n)
	if digits == 1 {
		fmt.Println(oneDigit)
		return
	}
	top, second := int(n[0]-'0'), int(n[1]-'0')
	var lead, zeros int
	if top == 1 {
		lead, zeros = long, digits-2
		if second >= 2 {
			lead = short
		}
	} else {
		lead, zeros = wide, digits-1
		if top <= lowTop {
			lead = 1
		}
	}
	// lead * 10^zeros + 1, written out
	if zeros == 0 {
		fmt.Println(lead + 1)
	} else {
		fmt.Printf("%d%s1\n", lead, strings.Repeat("0", zeros-1))
	}
}
