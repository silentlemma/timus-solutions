package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

func main() {
	const teamSize = 3
	const inputBufferSize = 1024
	// names are read with a word scanner over a 1 KB buffer and numbered, so
	// the graph holds ints instead of strings
	in := bufio.NewScanner(os.Stdin)
	in.Buffer(make([]byte, inputBufferSize), inputBufferSize)
	in.Split(bufio.ScanWords)
	in.Scan()
	teams, _ := strconv.Atoi(in.Text())
	ids := make(map[string]int, teamSize*teams)
	names := make([]string, 0, teamSize*teams)
	mates := make([][]int, 0, teamSize*teams)
	for t := 0; t < teams; t++ {
		var team [teamSize]int
		for i := range team {
			in.Scan()
			name := in.Text()
			id, exists := ids[name]
			if !exists {
				id = len(names)
				ids[name] = id
				names = append(names, name)
				mates = append(mates, nil)
			}
			team[i] = id
		}
		for _, a := range team {
			for _, b := range team {
				if a != b {
					mates[a] = append(mates[a], b)
				}
			}
		}
	}
	// breadth-first search from the champion over shared teams
	distance := make([]int, len(names))
	for i := range distance {
		distance[i] = -1
	}
	queue := make([]int, 0, len(names))
	if source, exists := ids["Isenbaev"]; exists {
		distance[source] = 0
		queue = append(queue, source)
	}
	for head := 0; head < len(queue); head++ {
		current := queue[head]
		for _, next := range mates[current] {
			if distance[next] == -1 {
				distance[next] = distance[current] + 1
				queue = append(queue, next)
			}
		}
	}
	sort.Strings(names)
	out := bufio.NewWriterSize(os.Stdout, inputBufferSize)
	for _, name := range names {
		out.WriteString(name)
		out.WriteByte(' ')
		value := distance[ids[name]]
		if value == -1 {
			out.WriteString("undefined")
		} else {
			out.WriteString(strconv.Itoa(value))
		}
		out.WriteByte('\n')
	}
	out.Flush()
}
