package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	// a fold of x cm needs x <= length - x, so a strip shrinks at best to
	// half its length, rounded up; folding exactly half each time reaches that
	var folds []string
	for n > 1 {
		folds = append(folds, strconv.Itoa(n/2))
		n -= n / 2
	}
	fmt.Println(len(folds))
	fmt.Println(strings.Join(folds, " "))
}
