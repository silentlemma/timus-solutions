package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	healthy    = 3
	teamSize   = 4
	tripleSize = teamSize - 1
)

func find(parent []int, player int) int {
	for parent[player] != player {
		parent[player] = parent[parent[player]]
		player = parent[player]
	}
	return player
}

func unite(parent []int, first, second int) {
	first = find(parent, first)
	second = find(parent, second)
	if first > second {
		first, second = second, first
	}
	parent[second] = first
}

func solve(in *bufio.Reader) string {
	var n int
	fmt.Fscan(in, &n)
	names := make([]string, n)
	index := make(map[string]int, n)
	parent := make([]int, n)
	health := make([]int, n)
	for i := range names {
		fmt.Fscan(in, &names[i])
		index[names[i]] = i
		parent[i] = i
		health[i] = healthy
	}
	var m int
	fmt.Fscan(in, &m)
	for event := 0; event < m; event++ {
		var actorName, action string
		fmt.Fscan(in, &actorName, &action)
		actor := index[actorName]
		if health[actor] < 2 {
			return "FAKE\n"
		}
		switch action {
		case "HIT":
			var targetName, inWord, part string
			fmt.Fscan(in, &targetName, &inWord, &part)
			target := index[targetName]
			damage := 1
			if part == "HEAD" {
				damage = 2
			}
			health[target] -= damage
			if health[target] < 0 {
				health[target] = 0
			}
		case "USES":
			var medkit string
			fmt.Fscan(in, &medkit)
			health[actor] = healthy
		case "REVIVE":
			var targetName string
			fmt.Fscan(in, &targetName)
			target := index[targetName]
			if health[target] != 1 {
				return "FAKE\n"
			}
			health[target] = 2
			unite(parent, actor, target)
		}
	}
	groups := make([][]int, n)
	for player := range names {
		root := find(parent, player)
		groups[root] = append(groups[root], player)
	}
	var buckets [teamSize + 1][][]int
	for _, group := range groups {
		if len(group) > teamSize {
			return "FAKE\n"
		}
		if len(group) > 0 {
			buckets[len(group)] = append(buckets[len(group)], group)
		}
	}
	if len(buckets[1]) < len(buckets[tripleSize]) {
		return "FAKE\n"
	}
	teams := buckets[teamSize]
	single := 0
	for _, group := range buckets[tripleSize] {
		team := append([]int{}, group...)
		team = append(team, buckets[1][single][0])
		teams = append(teams, team)
		single++
	}
	pair := 0
	for pair+1 < len(buckets[2]) {
		team := append([]int{}, buckets[2][pair]...)
		team = append(team, buckets[2][pair+1]...)
		teams = append(teams, team)
		pair += 2
	}
	if pair < len(buckets[2]) {
		team := append([]int{}, buckets[2][pair]...)
		team = append(team, buckets[1][single][0], buckets[1][single+1][0])
		teams = append(teams, team)
		single += 2
	}
	for single < len(buckets[1]) {
		team := make([]int, 0, teamSize)
		for member := 0; member < teamSize; member++ {
			team = append(team, buckets[1][single][0])
			single++
		}
		teams = append(teams, team)
	}
	var out strings.Builder
	out.WriteString("CORRECT\n")
	for _, team := range teams {
		for member, player := range team {
			if member > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(names[player])
		}
		out.WriteByte('\n')
	}
	return out.String()
}

func main() {
	fmt.Print(solve(bufio.NewReader(os.Stdin)))
}
