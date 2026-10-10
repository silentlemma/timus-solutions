package main

import (
	"bufio"
	"fmt"
	"os"
)

// mirror copies the left half with its middle digit backwards onto the right half
func mirror(digits []byte) []byte {
	out := append([]byte(nil), digits...)
	for i := 0; i < len(out)/2; i++ {
		out[len(out)-1-i] = out[i]
	}
	return out
}

func main() {
	var s string
	fmt.Fscan(bufio.NewReader(os.Stdin), &s)
	best := mirror([]byte(s))
	// same length strings of digits compare like the numbers they spell
	if string(best) < s {
		// add one to the left half with its middle digit; it is not all nines,
		// since all nines mirror to the largest number of this length
		half := []byte(s)
		k := (len(s)+1)/2 - 1
		for half[k] == '9' {
			half[k] = '0'
			k--
		}
		half[k]++
		best = mirror(half)
	}
	fmt.Println(string(best))
}
