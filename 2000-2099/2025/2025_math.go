package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(count, groups int64) int64 {
	small, larger := count/groups, count%groups
	squares := (groups-larger)*small*small + larger*(small+1)*(small+1)
	return (count*count - squares) / 2
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var tests int
	if _, err := fmt.Fscan(in, &tests); err != nil {
		return
	}
	for ; tests > 0; tests-- {
		var count, groups int64
		fmt.Fscan(in, &count, &groups)
		fmt.Fprintln(out, solve(count, groups))
	}
}
