package main

import (
	"bufio"
	"fmt"
	"os"
)

type movie struct {
	start, finish, count int
}

func augment(vertex int, edges [][]bool, own, other []int, active, visited []bool) bool {
	for target := range active {
		if !edges[vertex][target] || !active[target] || visited[target] {
			continue
		}
		visited[target] = true
		partner := other[target]
		if partner < 0 || augment(partner, edges, own, other, active, visited) {
			own[vertex] = target
			other[target] = vertex
			return true
		}
	}
	return false
}

func chooseMovies(movies []movie, students int) string {
	size := len(movies)
	following, preceding := make([][]bool, size), make([][]bool, size)
	for index := range movies {
		following[index], preceding[index] = make([]bool, size), make([]bool, size)
	}
	for first, before := range movies {
		for second, after := range movies {
			if before.finish <= after.start && before.count <= after.count {
				following[first][second] = true
				preceding[second][first] = true
			}
		}
	}
	left, right := make([]int, size), make([]int, size)
	for index := range movies {
		left[index], right[index] = -1, -1
	}
	active := make([]bool, size)
	chosen, matching := 0, 0
	answer := make([]byte, 0, size)
	for candidate := range movies {
		oldLeft, oldRight := append([]int(nil), left...), append([]int(nil), right...)
		oldMatching := matching
		visited := make([]bool, size)
		if augment(candidate, following, left, right, active, visited) {
			matching++
		}
		active[candidate] = true
		visited = make([]bool, size)
		if augment(candidate, preceding, right, left, active, visited) {
			matching++
		}
		if chosen+1-matching <= students {
			answer = append(answer, '1')
			chosen++
		} else {
			answer = append(answer, '0')
			active[candidate] = false
			left, right, matching = oldLeft, oldRight, oldMatching
		}
	}
	return string(answer)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var size, students int
	fmt.Fscan(in, &size, &students)
	movies := make([]movie, size)
	for index := range movies {
		fmt.Fscan(in, &movies[index].start, &movies[index].finish, &movies[index].count)
	}
	fmt.Println(chooseMovies(movies, students))
}
