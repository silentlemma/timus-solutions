package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Scan()
	n, _ := strconv.Atoi(strings.TrimSpace(in.Text()))
	seen := map[string]bool{}
	repeats := 0
	for i := 0; i < n && in.Scan(); i++ {
		// a name is the whole line, spaces included; only the line end goes
		name := strings.TrimSuffix(in.Text(), "\r")
		if seen[name] {
			repeats++
		}
		seen[name] = true
	}
	fmt.Println(repeats)
}
