package main

import (
	"bufio"
	"fmt"
	"os"
)

type schedule struct {
	busy   int
	starts [][2]int
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func solve(window, capacity int, deadlines []int) schedule {
	n := len(deadlines)
	width := n + 1
	stateCount, target := width*width, width*width-1
	infinity := deadlines[n-1] + 1
	releases := make([]int, n)
	for i, deadline := range deadlines {
		if deadline > window {
			releases[i] = deadline - window
		}
	}
	initial := make([]int, stateCount)
	for i := range initial {
		initial[i] = infinity
	}
	initial[0] = -1
	layers, parents := [][]int{initial}, [][]int{nil}
	active := []int{0}
	for busy := 1; busy <= 2*n; busy++ {
		following, previous := make([]int, stateCount), make([]int, stateCount)
		for i := range following {
			following[i], previous[i] = infinity, -1
		}
		nextActive := []int{}
		for _, state := range active {
			firstDone, secondDone := state/width, state%width
			earliest := layers[len(layers)-1][state] + 1
			for newFirst := 0; newFirst <= min(capacity, n-firstDone); newFirst++ {
				newSecond := min(capacity-newFirst, firstDone-secondDone)
				if newFirst+newSecond == 0 {
					continue
				}
				ni, nj := firstDone+newFirst, secondDone+newSecond
				minute := earliest
				if newFirst > 0 && releases[ni-1] > minute {
					minute = releases[ni-1]
				}
				if newSecond > 0 && minute >= deadlines[secondDone] {
					continue
				}
				if nj < n {
					remainingSides := 2
					if nj < ni {
						remainingSides = 1
					}
					if minute+1+remainingSides > deadlines[nj] {
						continue
					}
				}
				destination := ni*width + nj
				if minute < following[destination] {
					if following[destination] == infinity {
						nextActive = append(nextActive, destination)
					}
					following[destination] = minute
					previous[destination] = state
				}
			}
		}
		layers, parents = append(layers, following), append(parents, previous)
		if following[target] != infinity {
			starts := make([][2]int, n)
			state := target
			for used := busy; used > 0; used-- {
				oldState := parents[used][state]
				ni, nj, oi, oj := state/width, state%width, oldState/width, oldState%width
				minute := layers[used][state]
				for job := oi; job < ni; job++ {
					starts[job][0] = minute
				}
				for job := oj; job < nj; job++ {
					starts[job][1] = minute
				}
				state = oldState
			}
			return schedule{busy, starts}
		}
		if len(nextActive) == 0 {
			return schedule{busy: -1}
		}
		active = nextActive
	}
	return schedule{busy: -1}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var window, capacity, n int
	fmt.Fscan(in, &window, &capacity, &n)
	deadlines := make([]int, n)
	for i := range deadlines {
		fmt.Fscan(in, &deadlines[i])
	}
	answer := solve(window, capacity, deadlines)
	fmt.Fprintln(out, answer.busy)
	for _, starts := range answer.starts {
		fmt.Fprintln(out, starts[0], starts[1])
	}
}
