package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

const limbLimit = 1000000

func main() {
	var k, n int
	if _, err := fmt.Scan(&k, &n); err != nil {
		return
	}
	// the numbers are kept in limbs of base k^m, the largest power of k up
	// to a million, and digitSum[v] is the sum of the base-k digits of a limb
	base := 1
	for base <= limbLimit/k {
		base *= k
	}
	digitSum := make([]int, base)
	for v := 1; v < base; v++ {
		digitSum[v] = digitSum[v/k] + v%k
	}

	cost := make([]int, n)
	cost[0], cost[1] = 1, 1
	a, b := []int{1}, []int{1}
	for i := 2; i < n; i++ {
		// a, b = b, a + b, summing the digits on the way
		for len(a) < len(b) {
			a = append(a, 0)
		}
		sum, carry := 0, 0
		for j := range b {
			v := a[j] + b[j] + carry
			carry = 0
			if v >= base {
				v -= base
				carry = 1
			}
			a[j] = v
			sum += digitSum[v]
		}
		if carry == 1 {
			a = append(a, 1)
			sum++
		}
		a, b = b, a
		cost[i] = sum
	}
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.SliceStable(order, func(x, y int) bool { return cost[order[x]] < cost[order[y]] })
	parts := make([]string, n)
	for i, v := range order {
		parts[i] = strconv.Itoa(v + 1)
	}
	fmt.Println(strings.Join(parts, " "))
}
