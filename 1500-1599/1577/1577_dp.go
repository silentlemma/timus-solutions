package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1000000007

func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b string
	fmt.Fscan(in, &a, &b)
	n, m := len(a), len(b)
	// length[j] and count[j]: the shortest common supersequences of a[i:] and
	// b[j:], their length and number; row i needs only row i + 1
	length, count := make([]int, m+1), make([]int, m+1)
	belowLen, belowCnt := make([]int, m+1), make([]int, m+1)
	for j := 0; j <= m; j++ {
		length[j], count[j] = m-j, 1 // i = n: only b[j:] itself
	}
	for i := n - 1; i >= 0; i-- {
		length, belowLen = belowLen, length
		count, belowCnt = belowCnt, count
		length[m], count[m] = n-i, 1 // only a[i:] itself
		for j := m - 1; j >= 0; j-- {
			if a[i] == b[j] {
				// the first letter is the common one and covers both
				length[j], count[j] = belowLen[j+1]+1, belowCnt[j+1]
				continue
			}
			// the first letter is a[i] or b[j]; the two kinds of strings differ
			// in their first letter, so their numbers add up
			takeA, takeB := belowLen[j], length[j+1]
			best := takeA
			if takeB < best {
				best = takeB
			}
			length[j] = best + 1
			ways := 0
			if takeA == best {
				ways += belowCnt[j]
			}
			if takeB == best {
				ways += count[j+1]
			}
			count[j] = ways % mod
		}
	}
	fmt.Println(count[0])
}
