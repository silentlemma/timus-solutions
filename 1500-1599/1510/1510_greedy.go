package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	// Boyer-Moore vote: a value met more often than all the others together
	// survives pairing every note with a different one
	leader, lead := 0, 0
	for i := 0; i < n && sc.Scan(); i++ {
		value, _ := strconv.Atoi(sc.Text())
		switch {
		case lead == 0:
			leader, lead = value, 1
		case value == leader:
			lead++
		default:
			lead--
		}
	}
	fmt.Println(leader)
}
