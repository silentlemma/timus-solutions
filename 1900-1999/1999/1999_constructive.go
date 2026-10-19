package main

import (
	"bufio"
	"fmt"
	"os"
)

const base = 10

type Machine struct {
	terminal []int
	rows     [][base]int
}

func construct(old [][base]int, flags []int, offset int) Machine {
	n := len(old)
	stride := n + 1
	identifiers := make([]int, 2*n*stride)
	for i := range identifiers {
		identifiers[i] = -1
	}
	keys := []int{2 * n}
	identifiers[keys[0]] = 0
	result := Machine{}
	for head := 0; head < len(keys); head++ {
		key := keys[head]
		pair := key / 2
		normal, previous := pair/stride, pair%stride
		result.terminal = append(result.terminal, key&1)
		var row [base]int
		for digit := 0; digit < base; digit++ {
			nextNormal := old[normal][digit]
			nextPrevious := n
			if digit > 0 {
				nextPrevious = old[normal][digit-1]
			} else if previous != n {
				nextPrevious = old[previous][base-1]
			}
			accepted := 0
			if digit >= offset {
				accepted = flags[old[normal][digit-offset]]
			} else if previous != n {
				accepted = flags[old[previous][digit+base-offset]]
			}
			target := 2*(nextNormal*stride+nextPrevious) + accepted
			if identifiers[target] < 0 {
				identifiers[target] = len(keys)
				keys = append(keys, target)
			}
			row[digit] = identifiers[target]
		}
		result.rows = append(result.rows, row)
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var offset, n int
	fmt.Fscan(in, &offset, &n)
	flags := make([]int, n)
	for i := range flags {
		fmt.Fscan(in, &flags[i])
	}
	old := make([][base]int, n)
	for i := range old {
		for d := 0; d < base; d++ {
			fmt.Fscan(in, &old[i][d])
			old[i][d]--
		}
	}
	result := construct(old, flags, offset)
	fmt.Fprintln(out, "Success")
	fmt.Fprintln(out, len(result.rows))
	for i, v := range result.terminal {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, v)
	}
	fmt.Fprintln(out)
	for _, row := range result.rows {
		for d, v := range row {
			if d > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, v+1)
		}
		fmt.Fprintln(out)
	}
}
