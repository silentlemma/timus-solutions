package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// times in tenths of a second; starts are 30 seconds apart
const (
	tenthsPerMinute = 600
	tenthsPerSecond = 10
	gap             = 300
)

func tenths(text string) int {
	colon, dot := strings.IndexByte(text, ':'), strings.IndexByte(text, '.')
	minutes, _ := strconv.Atoi(text[:colon])
	seconds, _ := strconv.Atoi(text[colon+1 : dot])
	tenth, _ := strconv.Atoi(text[dot+1:])
	return minutes*tenthsPerMinute + seconds*tenthsPerSecond + tenth
}

type finish struct {
	at, run int
	name    string
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	finishes := make([]finish, n)
	for i := range finishes {
		var time string
		fmt.Fscan(in, &finishes[i].name, &time)
		finishes[i].run = tenths(time)
		finishes[i].at = i*gap + finishes[i].run
	}
	sort.Slice(finishes, func(a, b int) bool { return finishes[a].at < finishes[b].at })
	// replay the finishes in order; the board changes on every new best run
	var leaders []string
	best := -1
	for _, f := range finishes {
		if best < 0 || f.run < best {
			best = f.run
			leaders = append(leaders, f.name)
		}
	}
	sort.Strings(leaders)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(leaders))
	for _, name := range leaders {
		fmt.Fprintln(out, name)
	}
}
