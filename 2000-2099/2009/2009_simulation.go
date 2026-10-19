package main

import (
	"bufio"
	"fmt"
	"os"
)

type group struct {
	time     int
	students []int
}
type result struct{ time, side int }

func readCase(in *bufio.Reader) ([][]int, []group) {
	var count, groupCount int
	fmt.Fscan(in, &count, &groupCount)
	friends := make([][]int, count)
	for i := range friends {
		for {
			var id int
			fmt.Fscan(in, &id)
			if id == 0 {
				break
			}
			friends[i] = append(friends[i], id-1)
		}
	}
	groups := make([]group, groupCount)
	for i := range groups {
		var size int
		fmt.Fscan(in, &groups[i].time, &size)
		groups[i].students = make([]int, size)
		for j := range groups[i].students {
			fmt.Fscan(in, &groups[i].students[j])
			groups[i].students[j]--
		}
	}
	return friends, groups
}

func solve(friends [][]int, groups []group) []result {
	count := len(friends)
	var queues [2][]int
	var nextCompletion [2]int
	which, position := make([]int, count), make([]int, count)
	for i := range which {
		which[i] = -1
		position[i] = -1
	}
	answer := make([]result, count)
	for _, g := range groups {
		now := g.time
		for side := range queues {
			queue := queues[side]
			if len(queue) == 0 || nextCompletion[side] > now {
				continue
			}
			served := now - nextCompletion[side] + 1
			if served > len(queue) {
				served = len(queue)
			}
			for at, student := range queue[:served] {
				answer[student] = result{nextCompletion[side] + at, side}
				which[student] = -1
			}
			queue = queue[served:]
			queues[side] = queue
			for at, student := range queue {
				position[student] = at
			}
			if len(queue) == 0 {
				nextCompletion[side] = 0
			} else {
				nextCompletion[side] += served
			}
		}
		for _, student := range g.students {
			best := [2]int{len(queues[0]), len(queues[1])}
			for _, friend := range friends[student] {
				side := which[friend]
				if side >= 0 && position[friend]+1 < best[side] {
					best[side] = position[friend] + 1
				}
			}
			side := 1
			if best[0] < best[1] {
				side = 0
			}
			queue := append(queues[side], 0)
			at := best[side]
			copy(queue[at+1:], queue[at:len(queue)-1])
			queue[at] = student
			queues[side] = queue
			which[student] = side
			for index := at; index < len(queue); index++ {
				position[queue[index]] = index
			}
			if len(queue) == 1 {
				nextCompletion[side] = now + 1
			}
		}
	}
	for side, queue := range queues {
		for at, student := range queue {
			answer[student] = result{nextCompletion[side] + at, side}
		}
	}
	return answer
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	friends, groups := readCase(in)
	labels := [2]string{"left", "right"}
	for _, answer := range solve(friends, groups) {
		fmt.Fprintln(out, answer.time, labels[answer.side])
	}
}
