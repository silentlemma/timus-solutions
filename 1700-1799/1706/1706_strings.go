package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const copies = 4 // the text repeated so that every comparison below stays inside it

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var k int
	var s string
	fmt.Fscan(reader, &k, &s)
	n := len(s)
	t := strings.Repeat(s, copies)
	// a substring is counted at its leftmost start j in the window [a, a + k):
	// its lengths up to a + k - j minus the longest common prefix of j with an
	// earlier start of the window, best[j]; going down over a adds start a
	top := n + 2*k
	common := make([]int, k) // common[d] = lcp of positions a and a + d
	best := make([]int, top+k)
	answers := make([]int64, n)
	for a := top; a >= 0; a-- {
		ca := t[a]
		for d := 1; d < k; d++ {
			j := a + d
			if t[j] == ca {
				common[d]++
				if common[d] > best[j] {
					best[j] = common[d]
				}
			} else {
				common[d] = 0
			}
		}
		if a < n {
			end := a + k
			var total int64
			for j := a; j < end; j++ {
				if fresh := end - j - best[j]; fresh > 0 {
					total += int64(fresh)
				}
			}
			answers[a] = total
		}
	}
	for i, v := range answers {
		if i > 0 {
			writer.WriteString(" ")
		}
		writer.WriteString(strconv.FormatInt(v, 10))
	}
	writer.WriteString("\n")
}
