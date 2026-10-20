package main

import (
	"bufio"
	"fmt"
	"os"
)

const faces = 6 // a six lets the player roll again in the same turn

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	jump := make([]int, n+1)
	for i := 2; i < n; i++ {
		fmt.Fscan(reader, &jump[i])
	}
	// land[i]: where the token rests after arriving at i and following snakes
	land := make([]int, n+1)
	for i := 1; i <= n; i++ {
		if jump[i] > 0 {
			land[i] = land[i-jump[i]]
		} else {
			land[i] = i
		}
	}

	// turns holds the fewest turns begun when the token is about to roll at a
	// cell, and a six keeps the turn going at weight 0 while other rolls cost 1
	infinity := n + 1
	turns := make([]int, n+1)
	for i := range turns {
		turns[i] = infinity
	}
	turns[1] = 1
	// a deque made of a stack for the front and a queue for the back
	front := []int{1}
	var back []int
	head := 0
	best := infinity
	for len(front) > 0 || head < len(back) {
		var cell int
		if len(front) > 0 {
			cell = front[len(front)-1]
			front = front[:len(front)-1]
		} else {
			cell = back[head]
			head++
		}
		current := turns[cell]
		if current >= best {
			continue
		}
		for face := 1; face <= faces; face++ {
			position := cell + face
			if position > n {
				position = n
			}
			target := land[position]
			if target == n {
				if current < best {
					best = current
				}
				continue
			}
			cost := current + 1
			if face == faces {
				cost = current
			}
			if cost < turns[target] {
				turns[target] = cost
				if face == faces {
					front = append(front, target)
				} else {
					back = append(back, target)
				}
			}
		}
	}
	if best < infinity {
		fmt.Println(best)
	} else {
		fmt.Println(-1)
	}
}
