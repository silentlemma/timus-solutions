package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type segment struct{ left, right int }

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() (int, bool) {
		if !in.Scan() {
			return 0, false
		}
		v, _ := strconv.Atoi(in.Text())
		return v, true
	}
	m, _ := next()
	var segments []segment
	for {
		left, ok := next()
		right, _ := next()
		if !ok || (left == 0 && right == 0) {
			break
		}
		segments = append(segments, segment{left, right})
	}
	sort.Slice(segments, func(a, b int) bool {
		if segments[a].left != segments[b].left {
			return segments[a].left < segments[b].left
		}
		return segments[a].right < segments[b].right
	})
	var chosen []segment
	covered, i := 0, 0
	for covered < m {
		// among the segments that start inside the covered part, take the
		// one that reaches furthest; it is never worse than any other
		best := -1
		for ; i < len(segments) && segments[i].left <= covered; i++ {
			if best < 0 || segments[i].right > segments[best].right {
				best = i
			}
		}
		if best < 0 || segments[best].right <= covered {
			fmt.Println("No solution")
			return
		}
		chosen = append(chosen, segments[best])
		covered = segments[best].right
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(chosen))
	for _, s := range chosen {
		fmt.Fprintln(out, s.left, s.right)
	}
}
