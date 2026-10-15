package main

import (
	"bufio"
	"fmt"
	"os"
)

// the stack after each prefix is a tree node: a push makes a new node, a
// matching close returns to the parent, a wrong close starts a lone node,
// and a piece is human exactly when it ends on the node it started on
func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var dna string
	fmt.Fscan(in, &dna)
	parent := []int{-1}
	letter := []byte{0}
	state := make([]int, len(dna)+1)
	cur := 0
	for i := 0; i < len(dna); i++ {
		c := dna[i]
		if c >= 'A' && c <= 'Z' {
			parent = append(parent, cur)
			letter = append(letter, c)
			cur = len(parent) - 1
		} else if letter[cur] == c-'a'+'A' {
			cur = parent[cur]
		} else {
			parent = append(parent, -1)
			letter = append(letter, 0)
			cur = len(parent) - 1
		}
		state[i+1] = cur
	}
	var q int
	fmt.Fscan(in, &q)
	answer := make([]byte, q)
	for k := range answer {
		var left, right int
		fmt.Fscan(in, &left, &right)
		answer[k] = '0'
		if state[left-1] == state[right] {
			answer[k] = '1'
		}
	}
	fmt.Fprintln(out, string(answer))
}
