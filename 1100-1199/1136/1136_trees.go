package main

import (
	"bufio"
	"fmt"
	"os"
)

// a binary search tree in slices: the number of node v and its children,
// -1 for a missing child
var number, leftChild, rightChild []int

func insert(value int) {
	node := len(number)
	number = append(number, value)
	leftChild = append(leftChild, -1)
	rightChild = append(rightChild, -1)
	for v := 0; node > 0; {
		child := &rightChild[v]
		if value < number[v] {
			child = &leftChild[v]
		}
		if *child < 0 {
			*child = node
			return
		}
		v = *child
	}
}

// speak prints the even-session order: right wing, left wing, then the chairman
func speak(out *bufio.Writer, v int) {
	if v < 0 {
		return
	}
	speak(out, rightChild[v])
	speak(out, leftChild[v])
	fmt.Fprintln(out, number[v])
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	post := make([]int, n)
	for k := range post {
		fmt.Fscan(in, &post[k])
	}
	// read backwards, the odd-session order names every chairman before the
	// members of the wings, so inserting in that order rebuilds the tree
	for k := n - 1; k >= 0; k-- {
		insert(post[k])
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if n > 0 {
		speak(out, 0)
	}
}
