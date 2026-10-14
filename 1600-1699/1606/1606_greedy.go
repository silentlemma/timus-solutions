package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type flag struct{ x, y, number int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	flags := make([]flag, n)
	for i := range flags {
		fmt.Fscan(in, &flags[i].x, &flags[i].y)
		flags[i].number = i + 1
	}
	sort.Slice(flags, func(a, b int) bool { return flags[a].y > flags[b].y })
	// down the slope the x coordinates must zigzag; the longest zigzag keeps
	// the first flag, the last one of every run in one direction, and the end
	path := []string{strconv.Itoa(flags[0].number)}
	for i := 1; i < n; i++ {
		last := i == n-1
		turns := !last && (flags[i].x > flags[i-1].x) != (flags[i+1].x > flags[i].x)
		if last || turns {
			path = append(path, strconv.Itoa(flags[i].number))
		}
	}
	fmt.Println(len(path))
	fmt.Println(strings.Join(path, " "))
}
