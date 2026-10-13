package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

func isLetter(c byte) bool {
	return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z'
}

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	// best sums with the last word kept and dropped; neighbours may not both stay
	kept, dropped := 0, 0
	length := 0
	for i := 0; i <= len(data); i++ {
		if i < len(data) && isLetter(data[i]) {
			length++
			continue
		}
		if length > 0 {
			next := dropped + length
			if kept > dropped {
				dropped = kept
			}
			kept = next
			length = 0
		}
	}
	if dropped > kept {
		kept = dropped
	}
	fmt.Println(kept)
}
