package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const octetBits = 8

func address(s string) uint32 {
	var v uint32
	for _, part := range strings.Split(s, ".") {
		b, _ := strconv.Atoi(part)
		v = v<<octetBits | uint32(b)
	}
	return v
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// each interface is reduced to its subnet, IP AND mask
	nets := make([][]uint32, n)
	for i := range nets {
		var k int
		fmt.Fscan(in, &k)
		for j := 0; j < k; j++ {
			var ip, mask string
			fmt.Fscan(in, &ip, &mask)
			nets[i] = append(nets[i], address(ip)&address(mask))
		}
	}
	var start, end int
	fmt.Fscan(in, &start, &end)
	start--
	end--
	linked := func(u, v int) bool {
		for _, p := range nets[u] {
			for _, q := range nets[v] {
				if p == q {
					return true
				}
			}
		}
		return false
	}
	from := make([]int, n)
	for i := range from {
		from[i] = -1
	}
	from[start] = start
	queue := []int{start}
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		for v := 0; v < n; v++ {
			if from[v] < 0 && linked(u, v) {
				from[v] = u
				queue = append(queue, v)
			}
		}
	}
	if from[end] < 0 {
		fmt.Println("No")
		return
	}
	path := []int{end}
	for path[len(path)-1] != start {
		path = append(path, from[path[len(path)-1]])
	}
	parts := make([]string, 0, len(path))
	for i := len(path) - 1; i >= 0; i-- {
		parts = append(parts, strconv.Itoa(path[i]+1))
	}
	fmt.Println("Yes")
	fmt.Println(strings.Join(parts, " "))
}
