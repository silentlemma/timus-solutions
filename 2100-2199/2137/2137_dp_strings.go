package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const horizon = 25
const alphabetSize = 2

type seed struct {
	state int
	score int
}

type solver struct {
	text   []int
	border []int
	rank   []int
	answer [horizon + 1]int
	split  int
}

func (s *solver) append(symbol int) int {
	length := len(s.text)
	matched := s.border[length]
	for matched > 0 && s.text[matched] != symbol {
		matched = s.border[matched]
	}
	if length > 0 && s.text[matched] == symbol {
		matched++
	}
	s.text = append(s.text, symbol)
	s.border = append(s.border, matched)
	period := length + 1 - matched
	previousPeriod := matched - s.border[matched]
	// Equal minimal periods are consecutive along the border chain.
	value := s.rank[matched]
	if period != previousPeriod {
		value++
	}
	s.rank = append(s.rank, value)
	return s.rank[matched]
}

func (s *solver) update(step, score int) {
	if score > s.answer[step] {
		s.answer[step] = score
	}
}

func (s *solver) solveTail(score int) {
	length := len(s.text)
	remaining := horizon - s.split
	transition := make([][alphabetSize]int, length)
	for state := 0; state < length; state++ {
		for symbol := 0; symbol < alphabetSize; symbol++ {
			if s.text[state] == symbol {
				transition[state][symbol] = state + 1
			} else if state > 0 {
				transition[state][symbol] = transition[s.border[state]][symbol]
			}
		}
	}

	periods := make([]int, 0)
	state := s.border[length]
	for length-state <= remaining {
		periods = append(periods, length-state)
		if state == 0 {
			break
		}
		state = s.border[state]
	}

	seeds := make([][]seed, remaining+1)
	// A border reaching the fixed prefix forces a short periodic continuation.
	for _, period := range periods {
		pathScore := score
		for step := 1; step <= remaining; step++ {
			symbol := s.text[(length+step-1)%period]
			matched := s.border[len(s.border)-1]
			if matched >= length {
				other := 1 - symbol
				for matched >= length && s.text[matched] != other {
					matched = s.border[matched]
				}
				if matched < length {
					matched = transition[matched][other]
				} else {
					matched++
				}
				if matched < length {
					seeds[step] = append(seeds[step], seed{matched, pathScore + s.rank[matched]})
				}
			}
			pathScore += s.append(symbol)
			s.update(s.split+step, pathScore)
		}
		s.text = s.text[:length]
		s.border = s.border[:length+1]
		s.rank = s.rank[:length+1]
	}

	best := make([]int, length)
	next := make([]int, length)
	for state := 0; state < length; state++ {
		best[state] = -1
		next[state] = -1
	}
	active := []int{s.border[length]}
	nextActive := make([]int, 0)
	best[s.border[length]] = score
	for step := 1; step <= remaining; step++ {
		nextActive = nextActive[:0]
		relax := func(target, value int) {
			if next[target] < 0 {
				nextActive = append(nextActive, target)
			}
			if value > next[target] {
				next[target] = value
			}
		}
		for _, current := range active {
			for symbol := 0; symbol < alphabetSize; symbol++ {
				target := transition[current][symbol]
				if target < length {
					relax(target, best[current]+s.rank[target])
				}
			}
		}
		for _, item := range seeds[step] {
			relax(item.state, item.score)
		}
		for _, current := range active {
			best[current] = -1
		}
		best, next = next, best
		active, nextActive = nextActive, active
		for _, current := range active {
			s.update(s.split+step, best[current])
		}
	}
}

func (s *solver) search(depth, score int) {
	if depth == s.split {
		s.solveTail(score)
		return
	}
	for symbol := 0; symbol < alphabetSize; symbol++ {
		nextScore := score + s.append(symbol)
		s.update(depth+1, nextScore)
		s.search(depth+1, nextScore)
		s.text = s.text[:len(s.text)-1]
		s.border = s.border[:len(s.border)-1]
		s.rank = s.rank[:len(s.rank)-1]
	}
}

func main() {
	input, _ := ioutil.ReadAll(os.Stdin)
	s := solver{border: []int{0}, rank: []int{0}}
	score := 0
	for _, symbol := range input {
		if symbol == 'X' || symbol == '.' {
			value := 0
			if symbol == 'X' {
				value = 1
			}
			score += s.append(value)
		}
	}
	s.split = (horizon - len(s.text) + 1) / 2
	if s.split < 0 {
		s.split = 0
	}
	s.search(0, score)
	output := bufio.NewWriter(os.Stdout)
	for step := 1; step <= horizon; step++ {
		fmt.Fprintln(output, s.answer[step])
	}
	output.Flush()
}
