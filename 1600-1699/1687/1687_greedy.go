package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	boxes := make([][]int, k)
	for i := range boxes {
		var size int
		fmt.Fscan(in, &size)
		boxes[i] = make([]int, size)
		for j := range boxes[i] {
			fmt.Fscan(in, &boxes[i][j])
		}
	}
	var m int
	fmt.Fscan(in, &m)
	wanted := make([]bool, n+1)
	for i := 0; i < m; i++ {
		var c int
		fmt.Fscan(in, &c)
		wanted[c] = true
	}
	var useful []int
	coverable := make([]bool, n+1)
	coverableCount := 0
	for i, box := range boxes {
		any := false
		for _, c := range box {
			if wanted[c] {
				any = true
				if !coverable[c] {
					coverable[c] = true
					coverableCount++
				}
			}
		}
		if any {
			useful = append(useful, i)
		}
	}
	// no set of boxes is worth more than all coverable coins, nor holds more
	// than all useful boxes; one box per coverable coin reaches every coin,
	// so the answer is min(useful, coverable): those boxes, then any others
	chosen := make([]bool, k)
	covered := make([]bool, n+1)
	count := 0
	for coin := 1; coin <= n; coin++ {
		if !coverable[coin] || covered[coin] {
			continue
		}
		for _, i := range useful {
			holds := false
			for _, c := range boxes[i] {
				holds = holds || c == coin
			}
			if holds {
				chosen[i] = true
				count++
				for _, c := range boxes[i] {
					covered[c] = true
				}
				break
			}
		}
	}
	for _, i := range useful {
		if count < coverableCount && !chosen[i] {
			chosen[i] = true
			count++
		}
	}
	var picked []string
	for i := 0; i < k; i++ {
		if chosen[i] {
			picked = append(picked, strconv.Itoa(i+1))
		}
	}
	fmt.Println(count)
	fmt.Println(strings.Join(picked, " "))
}
