package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	where := make(map[int]int, n) // a value and the number of one element holding it
	var a []int
	for i := 1; i <= n; i++ {
		var s int
		fmt.Fscan(reader, &s)
		if _, ok := where[s]; !ok {
			where[s] = i
			a = append(a, s)
		}
	}
	sort.Ints(a)
	bestLength, bestFirst, bestStep := 1, a[0], 1
	for i := 0; i < len(a); i++ {
		for j := i + 1; j < len(a); j++ {
			d := a[j] - a[i]
			// walk each progression only from its first member, so every
			// pair of neighbours in it is visited once
			if _, ok := where[a[i]-d]; ok {
				continue
			}
			length, last := 2, a[j]
			for {
				if _, ok := where[last+d]; !ok {
					break
				}
				last += d
				length++
			}
			if length > bestLength {
				bestLength, bestFirst, bestStep = length, a[i], d
			}
		}
	}
	parts := make([]string, bestLength)
	for k := range parts {
		parts[k] = strconv.Itoa(where[bestFirst+k*bestStep])
	}
	fmt.Println(bestLength)
	fmt.Println(strings.Join(parts, " "))
}
