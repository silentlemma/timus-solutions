package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxPeople = 400
const wordBits = 64
const words = (maxPeople + wordBits - 1) / wordBits

type claimSet [words]uint64

func intersects(a, b claimSet) bool {
	for i := range a {
		if a[i]&b[i] != 0 {
			return true
		}
	}
	return false
}

func solve(locations []string, claims []claimSet) []int {
	n := len(locations)
	graph := make([][]int, n)
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if locations[i] != locations[j] && intersects(claims[i], claims[j]) {
				graph[i] = append(graph[i], j)
				graph[j] = append(graph[j], i)
			}
		}
	}
	color := make([]int, n)
	for i := range color {
		color[i] = -1
	}
	answer := make([]int, 0, n)
	for start := 0; start < n; start++ {
		if color[start] != -1 {
			continue
		}
		color[start] = 0
		var sides [2][]int
		pending := []int{start}
		for at := 0; at < len(pending); at++ {
			vertex := pending[at]
			sides[color[vertex]] = append(sides[color[vertex]], vertex)
			for _, target := range graph[vertex] {
				if color[target] == -1 {
					color[target] = color[vertex] ^ 1
					pending = append(pending, target)
				}
			}
		}
		side := 0
		if len(sides[1]) < len(sides[0]) {
			side = 1
		}
		answer = append(answer, sides[side]...)
	}
	if len(answer) == 0 {
		answer = append(answer, 0)
	}
	return answer
}

func run(in *bufio.Reader, out *bufio.Writer) {
	var n int
	fmt.Fscan(in, &n)
	locations := make([]string, n)
	claims := make([]claimSet, n)
	for i := 0; i < n; i++ {
		var count int
		fmt.Fscan(in, &locations[i], &count)
		claims[i][i/wordBits] |= uint64(1) << uint(i%wordBits)
		for ; count > 0; count-- {
			var person int
			fmt.Fscan(in, &person)
			person--
			claims[i][person/wordBits] |= uint64(1) << uint(person%wordBits)
		}
	}
	answer := solve(locations, claims)
	fmt.Fprintln(out, len(answer))
	for i, vertex := range answer {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, vertex+1)
	}
	fmt.Fprintln(out)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	run(in, out)
}
