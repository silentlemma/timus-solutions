package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type participant struct {
	threshold int
	index     int
}

func reliableTeams(values []int) [][]int {
	count := len(values)
	ordered := make([]participant, count)
	for index, value := range values {
		ordered[index] = participant{value, index + 1}
	}
	sort.Slice(ordered, func(first, second int) bool {
		if ordered[first].threshold != ordered[second].threshold {
			return ordered[first].threshold < ordered[second].threshold
		}
		return ordered[first].index < ordered[second].index
	})
	teams := make([][]int, 0)
	members := make([]int, 0, count)
	for size := 1; size <= count; size++ {
		members = append(members, ordered[size-1].index)
		if ordered[size-1].threshold <= size &&
			(size == count || ordered[size].threshold > size+1) {
			teams = append(teams, append([]int(nil), members...))
		}
	}
	return teams
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var count int
	fmt.Fscan(input, &count)
	values := make([]int, count)
	for index := range values {
		fmt.Fscan(input, &values[index])
	}
	teams := reliableTeams(values)
	fmt.Fprintln(output, len(teams))
	for _, team := range teams {
		fmt.Fprint(output, len(team))
		for _, member := range team {
			fmt.Fprint(output, " ", member)
		}
		fmt.Fprintln(output)
	}
}
