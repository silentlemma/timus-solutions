package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

func buildPath(start, finish, free int) []int {
	answer := make([]int, 0, 1<<uint(bits.OnesCount(uint(free))))
	var visit func(int, int, int)
	visit = func(first, last, dimensions int) {
		if dimensions&(dimensions-1) == 0 {
			answer = append(answer, first)
			if last != first {
				answer = append(answer, last)
			}
			return
		}
		difference := first ^ last
		split := difference & -difference
		remaining := dimensions ^ split
		bridge := remaining & -remaining
		if first^bridge^split == last && remaining != bridge {
			choices := remaining ^ bridge
			bridge = choices & -choices
		}
		middle := first ^ bridge
		visit(first, middle, remaining)
		visit(middle^split, last, remaining)
	}
	visit(start, finish, free)
	return answer
}

func readMask(in *bufio.Reader) int {
	var count int
	fmt.Fscan(in, &count)
	mask := 0
	for i := 0; i < count; i++ {
		var bit int
		fmt.Fscan(in, &bit)
		mask |= 1 << uint(bit-1)
	}
	return mask
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var dimensions int
	fmt.Fscan(in, &dimensions)
	start, finish := readMask(in), readMask(in)
	path := buildPath(start, finish, (1<<uint(dimensions))-1)
	fmt.Fprintln(out, len(path))
	for _, mask := range path {
		fmt.Fprint(out, bits.OnesCount(uint(mask)))
		for mask != 0 {
			bit := mask & -mask
			fmt.Fprint(out, " ", bits.TrailingZeros(uint(bit))+1)
			mask ^= bit
		}
		fmt.Fprintln(out)
	}
}
