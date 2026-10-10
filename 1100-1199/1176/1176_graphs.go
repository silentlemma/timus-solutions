package main

import (
	"bufio"
	"os"
	"strconv"
)

// buffer is the scanner's buffer size in bytes
const buffer = 1 << 20

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Buffer(make([]byte, buffer), buffer)
	in.Split(bufio.ScanWords)
	read := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	n, a := read(), read()
	// the channels still to lay are the missing ones; every planet has as
	// many of them going out as coming in, so they form one Euler circuit
	todo := make([][]int, n+1)
	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			if read() == 0 && i != j {
				todo[i] = append(todo[i], j)
			}
		}
	}
	// Hierholzer: walk until stuck, then back up and splice in side loops
	next := make([]int, n+1)
	stack := []int{a}
	var circuit []int
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		if next[v] < len(todo[v]) {
			stack = append(stack, todo[v][next[v]])
			next[v]++
		} else {
			circuit = append(circuit, v)
			stack = stack[:len(stack)-1]
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for k := len(circuit) - 1; k > 0; k-- {
		out.WriteString(strconv.Itoa(circuit[k]) + " " + strconv.Itoa(circuit[k-1]) + "\n")
	}
}
