package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const bufferSize = 1 << 16

func main() {
	reader := bufio.NewReaderSize(os.Stdin, bufferSize)
	var n int
	fmt.Fscan(reader, &n)
	s := make([]int64, n)
	r := make([]int64, n)
	for i := range s {
		fmt.Fscan(reader, &s[i], &r[i])
	}
	// v, u are best friends exactly when every other point lies on the
	// segment vu: all points collinear, v and u the two extreme ones
	low, high := 0, 0
	for i := 1; i < n; i++ {
		if (s[1]-s[0])*(r[i]-r[0]) != (s[i]-s[0])*(r[1]-r[0]) {
			fmt.Println(0)
			return
		}
		if s[i] < s[low] || (s[i] == s[low] && r[i] < r[low]) {
			low = i
		}
		if s[i] > s[high] || (s[i] == s[high] && r[i] > r[high]) {
			high = i
		}
	}
	fmt.Println(1)
	fmt.Println(strconv.Itoa(low+1) + " " + strconv.Itoa(high+1))
}
