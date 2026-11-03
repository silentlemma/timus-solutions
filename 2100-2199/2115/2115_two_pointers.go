package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

var input []byte
var position int

func nextInt() int {
	for position < len(input) && input[position] <= ' ' {
		position++
	}
	value := 0
	for position < len(input) && input[position] >= '0' && input[position] <= '9' {
		value = value*10 + int(input[position]-'0')
		position++
	}
	return value
}

func firstBad(a []int, direction int) int {
	i := 0
	for i+1 < len(a) && a[i]*direction <= a[i+1]*direction {
		i++
	}
	return i
}

func main() {
	input, _ = ioutil.ReadAll(os.Stdin)
	n := nextInt()
	a := make([]int, n)
	for i := range a {
		a[i] = nextInt()
	}
	up, down := firstBad(a, 1), firstBad(a, -1)
	if up == n-1 || down == n-1 {
		fmt.Println("Nothing to do here")
		return
	}
	for _, direction := range []int{1, -1} {
		left, right := up, n-1
		if direction < 0 {
			left = down
		}
		// Equal runs can hide the actual swapped endpoint behind a violation.
		for left > 0 && a[left-1] == a[left] {
			left--
		}
		for a[right-1]*direction <= a[right]*direction {
			right--
		}
		for right+1 < n && a[right+1] == a[right] {
			right++
		}
		a[left], a[right] = a[right], a[left]
		if firstBad(a, direction) == n-1 {
			fmt.Printf("Yes\n%d %d\n", left+1, right+1)
			return
		}
		a[left], a[right] = a[right], a[left]
	}
	fmt.Println("No hope")
}
