package main

import (
	"bufio"
	"fmt"
	"os"
)

const digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

func whole(x, k int) string {
	out := ""
	for {
		out = string(digits[x%k]) + out
		x /= k
		if x == 0 {
			return out
		}
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for {
		var a, b, k int
		fmt.Fscan(reader, &a, &b)
		if a == 0 && b == 0 {
			return
		}
		fmt.Fscan(reader, &k)
		text, rest := whole(a/b, k), a%b
		if rest != 0 {
			// long division; a remainder seen before starts the period
			seen := make([]int, b)
			for i := range seen {
				seen[i] = -1
			}
			var frac []byte
			for rest != 0 && seen[rest] < 0 {
				seen[rest] = len(frac)
				rest *= k
				frac = append(frac, digits[rest/b])
				rest %= b
			}
			if rest != 0 {
				s := seen[rest]
				frac = []byte(string(frac[:s]) + "(" + string(frac[s:]) + ")")
			}
			text += "." + string(frac)
		}
		fmt.Fprintln(writer, text)
	}
}
