package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	step        = 10
	unreachable = 10001
)

func plan(good string, limit int) (int, []int) {
	n := len(good)
	stride := limit + 1
	history := make([]byte, ((n+limit)/step)*stride)
	costs, next := make([]int, stride), make([]int, stride)
	for j := 1; j <= limit; j++ {
		costs[j] = unreachable
	}
	window := make([]int, stride)
	best, lastPlace, lastFriends := unreachable, 0, 0
	if n < step {
		best = 0
	}
	for place := step; place <= n+limit; place += step {
		head, tail := 0, 0
		parents := history[(place/step-1)*stride:]
		for friends := 0; friends <= limit; friends++ {
			next[friends] = unreachable
			// Before extending the window, a block ending in a friend
			// can use one to ten friends.
			parent, friendCost := 0, unreachable
			if head < tail {
				parent = window[head]
				friendCost = costs[parent] + 1
				if window[head] == friends-step {
					head++
				}
			}
			// With this column included, a block ending in a conductor
			// can use zero to nine friends.
			for head < tail && costs[window[tail-1]] >= costs[friends] {
				tail--
			}
			window[tail] = friends
			tail++
			conductors := place - friends
			if conductors < 0 || conductors > n {
				continue
			}
			conductorParent := window[head]
			conductorCost := unreachable
			if conductors != 0 {
				conductorCost = costs[conductorParent]
				if good[conductors-1] == '1' {
					conductorCost++
				}
			}
			if conductorCost <= friendCost {
				next[friends], parents[friends] = conductorCost, byte(2*conductorParent)
			} else {
				next[friends], parents[friends] = friendCost, byte(2*parent+1)
			}
			if n-conductors < step && next[friends] < best {
				best, lastPlace, lastFriends = next[friends], place, friends
			}
		}
		costs, next = next, costs
	}

	places := make([]int, 0, lastFriends)
	for lastPlace > 0 {
		code := int(history[(lastPlace/step-1)*stride+lastFriends])
		parent, finedFriend := code/2, code%2
		if finedFriend != 0 {
			places = append(places, lastPlace)
		}
		first := lastPlace - step + 1
		for position := first + lastFriends - parent - finedFriend - 1; position >= first; position-- {
			places = append(places, position)
		}
		lastFriends, lastPlace = parent, lastPlace-step
	}
	for lo, hi := 0, len(places)-1; lo < hi; lo, hi = lo+1, hi-1 {
		places[lo], places[hi] = places[hi], places[lo]
	}
	return best, places
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var n, limit int
	var good string
	fmt.Fscan(input, &n, &limit, &good)
	best, places := plan(good, limit)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	fmt.Fprintln(output, best)
	fmt.Fprint(output, len(places))
	for _, position := range places {
		fmt.Fprint(output, " ", position)
	}
	fmt.Fprintln(output)
}
