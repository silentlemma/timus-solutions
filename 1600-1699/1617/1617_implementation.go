package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	pairsPerCar = 4
	largest     = 700 // the widest diameter in millimetres
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	var count [largest + 1]int
	for i := 0; i < n; i++ {
		var d int
		fmt.Fscan(in, &d)
		count[d]++
	}
	// each diameter equips as many cars as it has full sets of four pairs
	cars := 0
	for _, c := range count {
		cars += c / pairsPerCar
	}
	fmt.Println(cars)
}
