package main

import (
	"bufio"
	"fmt"
	"os"
)

const splitDivisor = 4

type answer struct {
	from, to []int
}

type state struct {
	volume, previous, following, groups, valuePrevious, valueFollowing []int
	oddHead, evenHead, evenCount                                       int
	result                                                             answer
}

func newState(size, target int) *state {
	s := &state{
		volume: make([]int, size+1), previous: make([]int, size+1),
		following: make([]int, size+1), groups: make([]int, size+1),
		valuePrevious: make([]int, size+1), valueFollowing: make([]int, size+1),
	}
	s.volume[1] = target
	s.attach(1)
	if size != target {
		s.volume[2] = size - target
		s.attach(2)
	}
	return s
}

func (s *state) attach(index int) {
	value, head := s.volume[index], 0
	if value%2 != 0 {
		head = s.groups[value]
		if head == 0 {
			s.valuePrevious[value] = 0
			s.valueFollowing[value] = s.oddHead
			if s.oddHead != 0 {
				s.valuePrevious[s.oddHead] = value
			}
			s.oddHead = value
		}
		s.groups[value] = index
	} else {
		head = s.evenHead
		s.evenHead = index
		s.evenCount++
	}
	s.previous[index] = 0
	s.following[index] = head
	if head != 0 {
		s.previous[head] = index
	}
}

func (s *state) detach(index int) {
	value := s.volume[index]
	if value == 0 {
		return
	}
	before, after := s.previous[index], s.following[index]
	if before != 0 {
		s.following[before] = after
	} else if value%2 != 0 {
		s.groups[value] = after
	} else {
		s.evenHead = after
	}
	if after != 0 {
		s.previous[after] = before
	}
	if value%2 != 0 {
		if s.groups[value] == 0 {
			before, after = s.valuePrevious[value], s.valueFollowing[value]
			if before != 0 {
				s.valueFollowing[before] = after
			} else {
				s.oddHead = after
			}
			if after != 0 {
				s.valuePrevious[after] = before
			}
		}
	} else {
		s.evenCount--
	}
}

func (s *state) undo(donor, receiver int) {
	s.detach(donor)
	s.detach(receiver)
	half := s.volume[receiver] / 2
	s.volume[receiver] = half
	s.volume[donor] += half
	s.attach(donor)
	s.attach(receiver)
	s.result.from = append(s.result.from, donor)
	s.result.to = append(s.result.to, receiver)
}

func solve(n, k int) *answer {
	size := k
	if k&(k-1) != 0 {
		size = k + 1 + (k & 1)
	}
	if size > n {
		return nil
	}
	s := newState(size, k)
	empty := []int{}
	for i := 1; i <= size; i++ {
		if s.volume[i] == 0 {
			empty = append(empty, i)
		}
	}
	for s.evenCount > 0 {
		receiver := s.evenHead
		if s.evenCount > 1 || s.volume[receiver]%splitDivisor == 0 {
			donor := empty[len(empty)-1]
			empty = empty[:len(empty)-1]
			s.undo(donor, receiver)
			continue
		}
		value := s.oddHead
		if value == s.volume[receiver]/2 {
			value = s.valueFollowing[value]
		}
		if value == 0 {
			donor := empty[len(empty)-1]
			empty = empty[:len(empty)-1]
			s.undo(donor, receiver)
			continue
		}
		donor := s.groups[value]
		for s.volume[receiver]%splitDivisor != 0 {
			s.undo(donor, receiver)
			receiver, donor = donor, receiver
		}
	}
	return &s.result
}

func writeAnswer(result *answer, out *bufio.Writer) {
	if result == nil {
		fmt.Fprintln(out, -1)
		return
	}
	fmt.Fprintln(out, len(result.from))
	for i := len(result.from) - 1; i >= 0; i-- {
		fmt.Fprintln(out, result.from[i], result.to[i])
	}
}

func main() {
	var n, k int
	fmt.Fscan(os.Stdin, &n, &k)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	writeAnswer(solve(n, k), out)
}
