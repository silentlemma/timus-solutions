package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var groups, pots int
	if _, err := fmt.Fscan(reader, &groups, &pots); err != nil {
		return
	}
	total := groups * pots
	// each team is an edge from its pot to its party; a colouring of the
	// edges with one colour per group, never repeated at a vertex, is an
	// answer
	team := make([]string, total)
	pot := make([]int, total)
	party := make([]int, total)
	partyID := map[string]int{}
	var size []int
	for e := 0; e < total; e++ {
		var name string
		fmt.Fscan(reader, &team[e], &name)
		id, ok := partyID[name]
		if !ok {
			id = len(size)
			partyID[name] = id
			size = append(size, 0)
		}
		pot[e] = e / groups
		party[e] = id
		size[id]++
	}
	for _, s := range size {
		if s > groups {
			fmt.Println("No")
			return
		}
	}
	// atPot[u*groups+c], atParty[v*groups+c]: the edge of colour c
	atPot := make([]int, pots*groups)
	atParty := make([]int, len(size)*groups)
	for i := range atPot {
		atPot[i] = -1
	}
	for i := range atParty {
		atParty[i] = -1
	}
	colour := make([]int, total)
	paint := func(e, c int) {
		colour[e] = c
		atPot[pot[e]*groups+c] = e
		atParty[party[e]*groups+c] = e
	}
	var path []int
	for e := 0; e < total; e++ {
		u, v, a, b := pot[e], party[e], 0, 0
		for atPot[u*groups+a] != -1 {
			a++
		}
		for atParty[v*groups+b] != -1 {
			b++
		}
		// colour a is free at the pot and b at the party; swap a and b along
		// the path from the pot that alternates b and a, which cannot reach
		// the party, and b becomes free at both ends
		path = path[:0]
		at, want, onPot := u, b, true
		for a != b {
			var next int
			if onPot {
				next = atPot[at*groups+want]
			} else {
				next = atParty[at*groups+want]
			}
			if next == -1 {
				break
			}
			path = append(path, next)
			if onPot {
				at = party[next]
			} else {
				at = pot[next]
			}
			onPot = !onPot
			want = a + b - want
		}
		for _, f := range path {
			atPot[pot[f]*groups+colour[f]] = -1
			atParty[party[f]*groups+colour[f]] = -1
		}
		for _, f := range path {
			paint(f, a+b-colour[f])
		}
		paint(e, b)
	}
	members := make([][]string, groups)
	for g := range members {
		members[g] = make([]string, pots)
	}
	for e := 0; e < total; e++ {
		members[colour[e]][pot[e]] = team[e]
	}
	var out strings.Builder
	out.WriteString("Yes\n")
	for _, group := range members {
		out.WriteString("\n")
		for _, name := range group {
			out.WriteString(name + "\n")
		}
	}
	fmt.Print(out.String())
}
