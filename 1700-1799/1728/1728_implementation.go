package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

const (
	lyoshaName = "Efremov"
	vadikName  = "Kantorov"
)

func team(names ...string) string {
	sorted := append([]string{}, names...)
	sort.Strings(sorted)
	return strings.Join(sorted, " ")
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	played := map[string]bool{}
	for i := 0; i < n; i++ {
		var size int
		fmt.Fscan(in, &size)
		names := make([]string, size)
		for j := range names {
			fmt.Fscan(in, &names[j])
		}
		played[team(names...)] = true
	}
	var lyosha, vadik, m int
	fmt.Fscan(in, &lyosha, &vadik, &m)
	best, chosen := -1, ""
	for i := 0; i < m; i++ {
		var name string
		var rating, strength int
		fmt.Fscan(in, &name, &rating)
		// Lyosha stays away from a team that has played before, and the
		// pair left over must then be new, or the team is out
		if !played[team(lyoshaName, vadikName, name)] {
			strength = lyosha + vadik + rating
		} else if !played[team(vadikName, name)] {
			strength = vadik + rating
		} else {
			continue
		}
		if strength > best {
			best, chosen = strength, name
		}
	}
	if best < 0 {
		fmt.Println("Fail")
	} else {
		fmt.Println("Win")
		fmt.Println(chosen)
	}
}
