package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var houses = []string{"Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	readLine := func() string {
		line, _ := reader.ReadString('\n')
		return strings.TrimRight(line, "\r\n")
	}
	n, _ := strconv.Atoi(strings.TrimSpace(readLine()))
	lists := map[string][]string{}
	for i := 0; i < n; i++ {
		// names keep their inner spaces, so only the line break is dropped
		name := readLine()
		house := strings.TrimSpace(readLine())
		lists[house] = append(lists[house], name)
	}
	for h, house := range houses {
		if h > 0 {
			fmt.Fprintln(writer)
		}
		fmt.Fprintln(writer, house+":")
		for _, name := range lists[house] {
			fmt.Fprintln(writer, name)
		}
	}
}
