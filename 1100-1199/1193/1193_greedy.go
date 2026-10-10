package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	type student struct{ ready, talk, deadline int }
	students := make([]student, n)
	for i := range students {
		s := &students[i]
		fmt.Fscan(in, &s.ready, &s.talk, &s.deadline)
	}
	sort.Slice(students, func(i, j int) bool { return students[i].ready < students[j].ready })
	// moving the start earlier changes nobody's order or wait, it only adds
	// the same amount to every deadline: the answer is the worst lateness
	busyUntil, worst := 0, 0
	for _, s := range students {
		if s.ready > busyUntil {
			busyUntil = s.ready
		}
		busyUntil += s.talk
		if busyUntil-s.deadline > worst {
			worst = busyUntil - s.deadline
		}
	}
	fmt.Println(worst)
}
