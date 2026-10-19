package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const unknown = "unknown"

// fits checks that every block of size phrases is one language and that
// no language is used in two blocks
func fits(phrases []string, size int) bool {
	used := map[string]bool{}
	for start := 0; start < len(phrases); start += size {
		lang := ""
		for _, p := range phrases[start : start+size] {
			if p == unknown {
				continue
			}
			if lang == "" {
				lang = p
			}
			if p != lang {
				return false
			}
		}
		if lang == "" {
			continue
		}
		if used[lang] {
			return false
		}
		used[lang] = true
	}
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	phrases := make([]string, n)
	for i := range phrases {
		fmt.Fscan(reader, &phrases[i])
	}
	counts := []string{}
	for k := 1; k <= n; k++ {
		if n%k == 0 && fits(phrases, n/k) {
			counts = append(counts, strconv.Itoa(k))
		}
	}
	if len(counts) == 0 {
		fmt.Println("Igor is wrong.")
	} else {
		fmt.Println(strings.Join(counts, " "))
	}
}
