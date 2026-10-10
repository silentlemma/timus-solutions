package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	n := read()
	// the teacher's dates come sorted, so each of the student's dates is
	// looked up by binary search, counting repeats every time
	known := make([]int, n)
	for i := range known {
		known[i] = read()
	}
	m, count := read(), 0
	for i := 0; i < m; i++ {
		year := read()
		if k := sort.SearchInts(known, year); k < n && known[k] == year {
			count++
		}
	}
	fmt.Println(count)
}
