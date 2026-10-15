package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	readLine := func() string {
		line, _ := in.ReadString('\n')
		return strings.TrimSpace(line)
	}
	var year, n, q int
	fmt.Sscan(readLine(), &year, &n, &q)
	taken := map[string]bool{}
	for i := 0; i < n; i++ {
		team := readLine()
		// the university is everything before " #k"; names differing only
		// in letter case are the same university
		university := team
		if hash := strings.LastIndex(team, "#"); hash >= 0 {
			university = strings.TrimSpace(team[:hash])
		}
		university = strings.ToLower(university)
		if taken[university] {
			continue
		}
		if len(taken) == q {
			fmt.Println(team)
			return
		}
		taken[university] = true
	}
}
