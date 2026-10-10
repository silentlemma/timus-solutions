package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// identification numbers are positive and below this bound, so 0 means none
const limit = 65536

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	post := make([]int, n)
	for k := range post {
		fmt.Fscan(in, &post[k])
	}
	// read backwards, the odd-session order gives every chairman, then the
	// right wing, then the left wing; a stack of the open chairmen rebuilds the
	// tree from that
	left := make([]int, limit)
	right := make([]int, limit)
	var stack []int
	for k := n - 1; k >= 0; k-- {
		v := post[k]
		if len(stack) > 0 && v > stack[len(stack)-1] {
			right[stack[len(stack)-1]] = v
		} else if len(stack) > 0 {
			parent := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for len(stack) > 0 && stack[len(stack)-1] > v {
				parent = stack[len(stack)-1]
				stack = stack[:len(stack)-1]
			}
			left[parent] = v
		}
		stack = append(stack, v)
	}
	// the even-session order is the plain order root, left, right reversed
	var order []int
	stack = []int{post[n-1]}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, v)
		if right[v] != 0 {
			stack = append(stack, right[v])
		}
		if left[v] != 0 {
			stack = append(stack, left[v])
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for k := n - 1; k >= 0; k-- {
		out.WriteString(strconv.Itoa(order[k]) + "\n")
	}
}
