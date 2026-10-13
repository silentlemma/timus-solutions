package main

import (
	"bufio"
	"os"
	"sort"
	"strings"
)

const limit = 20

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	names := []string{"sun"} // the base starts with this one name, kept sorted
	for in.Scan() {
		line := in.Text()
		arg := line[1:]
		i := sort.SearchStrings(names, arg)
		if line[0] == '+' {
			if i == len(names) || names[i] != arg {
				names = append(names, "")
				copy(names[i+1:], names[i:])
				names[i] = arg
			}
			continue
		}
		out.WriteString(arg + "\n")
		// names with this prefix form a run starting where the prefix would go
		for j := i; j < len(names) && j < i+limit && strings.HasPrefix(names[j], arg); j++ {
			out.WriteString("  " + names[j] + "\n")
		}
	}
}
