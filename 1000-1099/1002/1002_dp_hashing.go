package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	maxWordLength = 50
	keypad        = "22233344115566070778889990"
	endOfInput    = "-1"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	for {
		var phone string
		if _, err := fmt.Fscan(reader, &phone); err != nil || phone == endOfInput {
			return
		}
		var n int
		fmt.Fscan(reader, &n)
		words := make([]string, n)
		byDigits := make(map[string]int, n)
		for i := range words {
			fmt.Fscan(reader, &words[i])
			digits := []byte(words[i])
			for j, c := range digits {
				digits[j] = keypad[c-'a']
			}
			if _, ok := byDigits[string(digits)]; !ok {
				byDigits[string(digits)] = i
			}
		}

		// best[i]: fewest words for the first i digits; how[i]: last word used
		m := len(phone)
		best, how := make([]int, m+1), make([]int, m+1)
		for i := range best {
			best[i] = -1
		}
		best[0] = 0
		for i := 0; i < m; i++ {
			if best[i] < 0 {
				continue
			}
			for l := 1; l <= maxWordLength && i+l <= m; l++ {
				w, ok := byDigits[phone[i:i+l]]
				if ok && (best[i+l] < 0 || best[i]+1 < best[i+l]) {
					best[i+l], how[i+l] = best[i]+1, w
				}
			}
		}

		if best[m] < 0 {
			fmt.Fprintln(writer, "No solution.")
			continue
		}
		var used []string
		for pos := m; pos > 0; pos -= len(words[how[pos]]) {
			used = append(used, words[how[pos]])
		}
		for i, j := 0, len(used)-1; i < j; i, j = i+1, j-1 {
			used[i], used[j] = used[j], used[i]
		}
		fmt.Fprintln(writer, strings.Join(used, " "))
	}
}
