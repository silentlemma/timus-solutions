package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const longest = 140

var prefix = len("RT @: ")

func main() {
	reader := bufio.NewReader(os.Stdin)
	readLine := func() string {
		s, _ := reader.ReadString('\n')
		return strings.TrimRight(s, "\r\n")
	}
	n, _ := strconv.Atoi(strings.TrimSpace(readLine()))
	names := make([]string, n)
	followNames := make([][]string, n)
	for i := 0; i < n; i++ {
		// a description is a name, a count and that many names
		words := []string{}
		for {
			if len(words) >= 2 {
				c, _ := strconv.Atoi(words[1])
				if len(words) >= 2+c {
					break
				}
			}
			words = append(words, strings.Fields(readLine())...)
		}
		names[i] = words[0]
		followNames[i] = words[2:]
	}
	tweet := readLine()
	index := map[string]int{}
	for i, name := range names {
		index[name] = i
	}
	// length[u] is the shortest message u can hold; a retweet of u's message
	// is longer by the prefix and u's name
	length := make([]int, n)
	for i := range length {
		length[i] = longest + 1
	}
	length[0] = len(tweet)
	done := make([]bool, n)
	for {
		u := -1
		for i := 0; i < n; i++ {
			if !done[i] && (u < 0 || length[i] < length[u]) {
				u = i
			}
		}
		if u < 0 || length[u] > longest {
			break
		}
		done[u] = true
		longer := length[u] + prefix + len(names[u])
		for _, f := range followNames[u] {
			if v := index[f]; longer < length[v] {
				length[v] = longer
			}
		}
	}
	// everybody who holds a message shows it to all followers
	knows := make([]bool, n)
	for u := 0; u < n; u++ {
		if done[u] {
			knows[u] = true
			for _, f := range followNames[u] {
				knows[index[f]] = true
			}
		}
	}
	told := []string{}
	for i := 0; i < n; i++ {
		if knows[i] {
			told = append(told, names[i])
		}
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprintln(writer, len(told))
	for _, name := range told {
		fmt.Fprintln(writer, name)
	}
}
