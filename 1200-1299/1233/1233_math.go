package main

import (
	"fmt"
	"strconv"
)

func main() {
	var k, m int64
	fmt.Scan(&k, &m)
	digits := strconv.FormatInt(k, 10)
	// numbers not longer than k that come no later than k: for each length,
	// those from 10^(l-1) up to the first l digits of k; any N >= k has them
	var before, low int64 = 0, 1
	for l := 1; l <= len(digits); l++ {
		prefix, _ := strconv.Atoi(digits[:l])
		before += int64(prefix) - low + 1
		low *= 10
	}
	if m < before {
		fmt.Println(0)
		return
	}
	// each further number before k is longer than k: of length l it lies in
	// [10^(l-1), k * 10^(l-len(k))), and N is the (m - before)-th of them
	need, top := m-before, k*10
	if need == 0 {
		fmt.Println(k)
		return
	}
	for top > low {
		if top-low >= need {
			fmt.Println(low + need - 1)
			return
		}
		need -= top - low
		low *= 10
		top *= 10
	}
	// k is a power of ten, and no longer number comes before it
	fmt.Println(0)
}
