package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	// value[i] and locks[i]: the sum of values and the number of locked
	// buffers among the first i buffers
	value := make([]int, n+1)
	locks := make([]int, n+1)
	for i := 1; i <= n; {
		c, err := in.ReadByte()
		if err != nil {
			break
		}
		switch {
		case c == '*':
			locks[i] = locks[i-1] + 1
			value[i] = value[i-1]
		case c >= '0' && c <= '9':
			locks[i] = locks[i-1]
			value[i] = value[i-1] + int(c-'0')
		default:
			continue
		}
		i++
	}
	// the windows [l, l + k - 1] without locks; the first cheapest wins
	best, bestValue := 0, 0
	for l := 1; l+k-1 <= n; l++ {
		r := l + k - 1
		if locks[r] != locks[l-1] {
			continue
		}
		v := value[r] - value[l-1]
		if best == 0 || v < bestValue {
			best, bestValue = l, v
		}
	}
	fmt.Println(best)
}
