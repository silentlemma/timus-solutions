package main

import (
	"bufio"
	"fmt"
	"os"
)

const limit = 2000000 // the largest possible sum of two notes

var (
	composite []bool
	odd, even []int
	partner   []int // the odd note matched to each even note, -1 if none
	visited   []bool
)

func augment(u int) bool {
	for v := range even {
		if visited[v] || composite[odd[u]+even[v]] {
			continue
		}
		visited[v] = true
		if partner[v] < 0 || augment(partner[v]) {
			partner[v] = u
			return true
		}
	}
	return false
}

func main() {
	composite = make([]bool, limit+1)
	composite[0], composite[1] = true, true
	for i := 2; i*i <= limit; i++ {
		if !composite[i] {
			for j := i * i; j <= limit; j += i {
				composite[j] = true
			}
		}
	}
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	ones := 0
	for i := 0; i < n; i++ {
		var c int
		fmt.Fscan(reader, &c)
		switch {
		case c == 1:
			ones++
		case c%2 == 1:
			odd = append(odd, c)
		default:
			even = append(even, c)
		}
	}
	// A prime sum is 2 = 1 + 1 or an odd prime, the sum of an odd and an even
	// note. So the surplus of odd notes must be paired as ones among themselves.
	surplus := ones + len(odd) - len(even)
	if surplus < 0 || surplus > ones {
		fmt.Fprintln(writer, "NO")
		return
	}
	onePairs := surplus / 2
	for i := 0; i < ones-2*onePairs; i++ {
		odd = append(odd, 1)
	}
	partner = make([]int, len(even))
	for v := range partner {
		partner[v] = -1
	}
	for u := range odd {
		visited = make([]bool, len(even))
		if !augment(u) {
			fmt.Fprintln(writer, "NO")
			return
		}
	}
	fmt.Fprintln(writer, "YES")
	for i := 0; i < onePairs; i++ {
		fmt.Fprintln(writer, "1 1")
	}
	for v := range even {
		fmt.Fprintln(writer, odd[partner[v]], even[v])
	}
}
