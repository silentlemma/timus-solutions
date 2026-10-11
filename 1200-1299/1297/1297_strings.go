package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	line, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	s := strings.TrimRight(line, "\r\n ")
	n := len(s)
	bestStart, bestLen := 0, 0
	// every letter and every gap between two letters is a centre, 2n - 1 in all, and
	// each is expanded as far as it goes; ties keep the leftmost start
	for centre := 0; centre < 2*n-1; centre++ {
		lo, hi := centre/2, (centre+1)/2
		for lo >= 0 && hi < n && s[lo] == s[hi] {
			lo--
			hi++
		}
		length, start := hi-lo-1, lo+1
		if length > bestLen || (length == bestLen && start < bestStart) {
			bestStart, bestLen = start, length
		}
	}
	fmt.Println(s[bestStart : bestStart+bestLen])
}
