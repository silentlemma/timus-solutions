package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
)

const (
	letters  = 26
	alphabet = letters + 1
	noState  = -1
)

type state struct {
	next      [alphabet]int32
	length    int32
	link      int32
	negative  int
	favorite  int
	missing   int
	documents map[int]struct{}
}

type automaton struct {
	states        []state
	teamLimit     int
	positionLimit int
}

func (sam *automaton) addState(length int32) int32 {
	index := int32(len(sam.states))
	sam.states = append(sam.states, state{
		length:   length,
		link:     noState,
		negative: sam.teamLimit,
		favorite: sam.positionLimit,
		missing:  1,
	})
	return index
}

func (sam *automaton) cloneState(source, length int32) int32 {
	clone := sam.addState(length)
	sam.states[clone].next = sam.states[source].next
	sam.states[clone].link = sam.states[source].link
	return clone
}

func (sam *automaton) redirect(parent int32, character int, target, replacement int32) {
	for parent != noState && sam.states[parent].next[character] == target {
		sam.states[parent].next[character] = replacement
		parent = sam.states[parent].link
	}
}

func (sam *automaton) extend(last int32, character int) int32 {
	target := sam.states[last].next[character]
	if target != 0 {
		if sam.states[target].length == sam.states[last].length+1 {
			return target
		}
		clone := sam.cloneState(target, sam.states[last].length+1)
		sam.redirect(last, character, target, clone)
		sam.states[target].link = clone
		return clone
	}

	current := sam.addState(sam.states[last].length + 1)
	parent := last
	for parent != noState && sam.states[parent].next[character] == 0 {
		sam.states[parent].next[character] = current
		parent = sam.states[parent].link
	}
	if parent == noState {
		sam.states[current].link = 0
	} else {
		target = sam.states[parent].next[character]
		if sam.states[target].length == sam.states[parent].length+1 {
			sam.states[current].link = target
		} else {
			clone := sam.cloneState(target, sam.states[parent].length+1)
			sam.redirect(parent, character, target, clone)
			sam.states[target].link = clone
			sam.states[current].link = clone
		}
	}
	return current
}

type candidate struct {
	length int
	left   int
}

func better(first, second candidate) candidate {
	if second.length < first.length || second.length == first.length && second.left < first.left {
		return second
	}
	return first
}

func minimum(first, second int) int {
	if first < second {
		return first
	}
	return second
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	fields := bytes.Fields(data)
	teamCount, _ := strconv.Atoi(string(fields[0]))
	names := fields[1:]
	positive := make([]bool, teamCount)
	totalLength, maximumLength := 0, 0
	for team, name := range names {
		positive[team] = name[len(name)-1] == '+'
		if positive[team] {
			names[team] = name[:len(name)-1]
		}
		length := len(names[team])
		totalLength += length
		if length > maximumLength {
			maximumLength = length
		}
	}

	sam := automaton{
		states:        make([]state, 0, 2*totalLength+1),
		teamLimit:     teamCount,
		positionLimit: totalLength,
	}
	sam.addState(0)
	positiveTimes := make([]int, 0, teamCount+1)
	for team, name := range names {
		document := len(positiveTimes)
		if positive[team] {
			positiveTimes = append(positiveTimes, team)
		}
		last := int32(0)
		for position, character := range name {
			letter := int(character - 'a')
			if character == '_' {
				letter = letters
			}
			last = sam.extend(last, letter)
			current := &sam.states[last]
			if team == 0 {
				current.favorite = minimum(current.favorite, position)
			} else if positive[team] {
				if current.documents == nil {
					current.documents = make(map[int]struct{})
				}
				current.documents[document] = struct{}{}
			} else {
				current.negative = minimum(current.negative, team)
			}
		}
	}
	positiveTimes = append(positiveTimes, teamCount)
	states := sam.states

	counts := make([]int, maximumLength+1)
	for _, current := range states {
		counts[current.length]++
	}
	for length := 1; length <= maximumLength; length++ {
		counts[length] += counts[length-1]
	}
	order := make([]int32, len(states))
	for index := range states {
		length := states[index].length
		counts[length]--
		order[counts[length]] = int32(index)
	}

	absent := candidate{totalLength + 1, totalLength}
	best := make([]candidate, teamCount+1)
	for index := range best {
		best[index] = absent
	}
	for index := len(order) - 1; index > 0; index-- {
		current := &states[order[index]]
		for {
			if _, found := current.documents[current.missing]; !found {
				break
			}
			current.missing++
		}
		parent := &states[current.link]
		if current.favorite != totalLength {
			length := int(parent.length) + 1
			left := current.favorite - length + 1
			expiration := minimum(current.negative, positiveTimes[current.missing])
			best[expiration] = better(best[expiration], candidate{length, left})
		}

		// Suffix-link subtrees contain exactly the occurrences of each state.
		parent.negative = minimum(parent.negative, current.negative)
		parent.favorite = minimum(parent.favorite, current.favorite)
		if current.missing > parent.missing {
			parent.missing = current.missing
		}
		if len(parent.documents) < len(current.documents) {
			parent.documents, current.documents = current.documents, parent.documents
		}
		for document := range current.documents {
			parent.documents[document] = struct{}{}
		}
		current.documents = nil
	}

	answer := absent
	answers := make([]candidate, teamCount)
	for team := teamCount - 1; team >= 0; team-- {
		answer = better(answer, best[team+1])
		answers[team] = answer
	}
	output := bufio.NewWriter(os.Stdout)
	for _, result := range answers {
		if result == absent {
			fmt.Fprintln(output, "-1 -1")
		} else {
			fmt.Fprintln(output, result.left, result.left+result.length-1)
		}
	}
	output.Flush()
}
