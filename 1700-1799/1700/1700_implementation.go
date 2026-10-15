package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	readLine := func() string {
		line, _ := in.ReadString('\n')
		return strings.TrimRight(line, "\r\n")
	}
	n, _ := strconv.Atoi(strings.TrimSpace(readLine()))
	known := map[string]map[string]bool{}
	for i := 0; i < n; i++ {
		line := readLine()
		colon := strings.Index(line, ":")
		set := map[string]bool{}
		for _, w := range strings.Fields(line[colon+1:]) {
			set[w] = true
		}
		known[line[:colon]] = set
	}
	m, _ := strconv.Atoi(strings.TrimSpace(readLine()))
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < m; i++ {
		names := strings.Fields(readLine())
		// the common associations are the intersection of the sets
		var common []string
		for w := range known[names[0]] {
			shared := true
			for _, name := range names[1:] {
				shared = shared && known[name][w]
			}
			if shared {
				common = append(common, w)
			}
		}
		if len(common) == 0 {
			fmt.Fprintln(out, "No solution.")
			continue
		}
		sort.Strings(common)
		fmt.Fprintln(out, strings.Join(common, " "))
	}
}
