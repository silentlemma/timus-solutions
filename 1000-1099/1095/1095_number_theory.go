package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	divisor = 7
	key     = "1234"
)

func remainderOf(s string) int {
	r := 0
	for i := 0; i < len(s); i++ {
		r = (r*10 + int(s[i]-'0')) % divisor
	}
	return r
}

func permute(prefix, rest string, out *[]string) {
	if rest == "" {
		*out = append(*out, prefix)
		return
	}
	for i := 0; i < len(rest); i++ {
		permute(prefix+rest[i:i+1], rest[:i]+rest[i+1:], out)
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	// the 24 orders of 1, 2, 3, 4 leave every remainder modulo 7
	var orders []string
	permute("", key, &orders)
	var n int
	fmt.Fscan(in, &n)
	for ; n > 0; n-- {
		var number string
		fmt.Fscan(in, &number)
		for _, d := range key {
			number = strings.Replace(number, string(d), "", 1)
		}
		// zeros go to the end, where they do not change divisibility by 7
		head := strings.ReplaceAll(number, "0", "")
		zeros := strings.Repeat("0", len(number)-len(head))
		for _, o := range orders {
			if remainderOf(head+o) == 0 {
				fmt.Fprintln(w, head+o+zeros)
				break
			}
		}
	}
}
