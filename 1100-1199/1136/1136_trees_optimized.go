package main

import (
	"bufio"
	"os"
	"strconv"
)

// nextInt parses a number by hand from a buffered reader, faster than fmt.Fscan
func nextInt(in *bufio.Reader) int {
	c, err := in.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.ReadByte()
	}
	negative := c == '-'
	if negative {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, _ = in.ReadByte()
	}
	if negative {
		return -value
	}
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	n := nextInt(in)
	// input positions are positive and below the array size, so 0 means none
	post := make([]int, n+1)
	for k := 1; k <= n; k++ {
		post[k] = nextInt(in)
	}
	left, right := make([]int, n+1), make([]int, n+1)
	stack := make([]int, 0, n)
	// read backwards, the odd-session order gives every chairman, then the
	// right wing, then the left wing; a stack of the open chairmen rebuilds the
	// tree from that
	for k := n; k > 0; k-- {
		if len(stack) > 0 && post[k] > post[stack[len(stack)-1]] {
			right[stack[len(stack)-1]] = k
		} else if len(stack) > 0 {
			parent := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for len(stack) > 0 && post[stack[len(stack)-1]] > post[k] {
				parent = stack[len(stack)-1]
				stack = stack[:len(stack)-1]
			}
			left[parent] = k
		}
		stack = append(stack, k)
	}
	// the even-session order is the plain order root, left, right reversed
	order := make([]int, 0, n)
	stack = stack[:0]
	if n > 0 {
		stack = append(stack, n)
	}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, post[node])
		if right[node] != 0 {
			stack = append(stack, right[node])
		}
		if left[node] != 0 {
			stack = append(stack, left[node])
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for k := n - 1; k >= 0; k-- {
		out.WriteString(strconv.Itoa(order[k]))
		out.WriteByte('\n')
	}
}
