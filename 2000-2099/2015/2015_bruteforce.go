package main

import (
	"bufio"
	"fmt"
	"os"
)

type apartment struct{ rooms, price, benefit int }

func solve(budget int, alone [2]int, friends [][2]int, apartments []apartment) [2]int {
	best := -1
	choice := [2]int{}
	for i, apt := range apartments {
		if apt.price <= budget {
			score := apt.benefit + alone[apt.rooms-1]
			if score > best {
				best = score
				choice = [2]int{i + 1, 0}
			}
		}
		if apt.rooms == 2 && apt.price <= 2*budget {
			for j, friend := range friends {
				if apt.price <= 2*friend[0] {
					score := apt.benefit + friend[1]
					if score > best {
						best = score
						choice = [2]int{i + 1, j + 1}
					}
				}
			}
		}
	}
	return choice
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var budget, n, m int
	var alone [2]int
	fmt.Fscan(in, &budget, &alone[0], &alone[1], &n)
	friends := make([][2]int, n)
	for i := range friends {
		fmt.Fscan(in, &friends[i][0], &friends[i][1])
	}
	fmt.Fscan(in, &m)
	apartments := make([]apartment, m)
	for i := range apartments {
		apt := &apartments[i]
		fmt.Fscan(in, &apt.rooms, &apt.price, &apt.benefit)
	}
	choice := solve(budget, alone, friends, apartments)
	if choice[0] == 0 {
		fmt.Println("Forget about apartments. Live in the dormitory.")
	} else if choice[1] == 0 {
		fmt.Printf("You should rent the apartment #%d alone.\n", choice[0])
	} else {
		fmt.Printf("You should rent the apartment #%d with the friend #%d.\n", choice[0], choice[1])
	}
}
