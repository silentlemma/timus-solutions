package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const money = 100

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	bought := make([]int, n)
	total := 0
	for i := range bought {
		fmt.Fscan(in, &bought[i])
		total += bought[i]
	}
	// everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
	// litre, friend i paid for bought[i] (n + 1) - total litres of others
	over := make([]int, n)
	all := 0
	for i, b := range bought {
		if b*(n+1) > total {
			over[i] = b*(n+1) - total
		}
		all += over[i]
	}
	parts := make([]string, n)
	for i, x := range over {
		parts[i] = strconv.Itoa(money * x / all)
	}
	fmt.Println(strings.Join(parts, " "))
}
