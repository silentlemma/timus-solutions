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
	in := bufio.NewScanner(os.Stdin)
	// names of the current topic and its ancestors
	var path []string
	// problem -> descriptions of its topics
	topics := map[int]map[string]bool{}
	current := ""
	for in.Scan() {
		words := strings.Fields(in.Text())
		if len(words) == 0 {
			continue
		}
		if strings.HasSuffix(words[0], ".") {
			// a heading "1.2. name": its depth is the number of dots
			depth := strings.Count(words[0], ".")
			path = append(path[:depth-1], strings.Join(words[1:], " "))
			current = strings.Join(path, ".")
			continue
		}
		for _, w := range words {
			problem, _ := strconv.Atoi(w)
			if topics[problem] == nil {
				topics[problem] = map[string]bool{}
			}
			topics[problem][current] = true
		}
	}
	groups := map[string][]int{}
	for problem, own := range topics {
		var names []string
		for t := range own {
			names = append(names, t)
		}
		sort.Strings(names)
		key := strings.Join(names, ", ")
		groups[key] = append(groups[key], problem)
	}
	var lines []string
	for key, problems := range groups {
		sort.Ints(problems)
		numbers := make([]string, len(problems))
		for i, p := range problems {
			numbers[i] = strconv.Itoa(p)
		}
		lines = append(lines, strings.Join(numbers, ", ")+" : "+key)
	}
	sort.Strings(lines)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, s := range lines {
		fmt.Fprintln(out, s)
	}
}
