package main

import (
	"bufio"
	"os"
	"strings"
)

func main() {
	line, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	word := strings.TrimSpace(line)
	n := len(word)
	// n <= 10000, so every proper prefix length fits in uint16.
	border := make([]uint16, n)
	// address the reversed pattern through the original word to avoid a copy.
	for i := 1; i < n; i++ {
		k := int(border[i-1])
		for k > 0 && word[n-1-i] != word[n-1-k] {
			k = int(border[k-1])
		}
		if word[n-1-i] == word[n-1-k] {
			k++
		}
		border[i] = uint16(k)
	}
	longest := 0
	// scan only the proper tail: the appended word must not be empty.
	for i := 1; i < n; i++ {
		for longest > 0 && word[i] != word[n-1-longest] {
			longest = int(border[longest-1])
		}
		if word[i] == word[n-1-longest] {
			longest++
		}
	}
	out := bufio.NewWriter(os.Stdout)
	out.WriteString(word)
	for i := n - longest - 1; i >= 0; i-- {
		out.WriteByte(word[i])
	}
	out.WriteByte('\n')
	out.Flush()
}
