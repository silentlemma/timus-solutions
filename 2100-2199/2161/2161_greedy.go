package main

import (
	"bufio"
	"fmt"
	"os"
)

// topTwo keeps the largest value over all knights but one, from the two
// largest; -1 stands for a missing value, so a lone knight needs nothing.
type topTwo struct {
	first, second int64
	where         int
}

func (t *topTwo) add(value int64, index int) {
	if value > t.first {
		t.second = t.first
		t.first = value
		t.where = index
	} else if value > t.second {
		t.second = value
	}
}

func (t *topTwo) without(index int) int64 {
	if index == t.where {
		return t.second
	}
	return t.first
}

func positive(x int64) int64 {
	if x > 0 {
		return x
	}
	return 0
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	a := make([]int64, n)
	d := make([]int64, n)
	g := make([]int64, n)
	// the strongest attack and shield each rival can afford
	attack := topTwo{-1, -1, -1}
	shield := topTwo{-1, -1, -1}
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &a[i], &d[i], &g[i])
		attack.add(a[i]+g[i], i)
		shield.add(d[i]+g[i], i)
	}
	for i := 0; i < n; i++ {
		// The shield must exceed every rival's best attack and the attack must
		// reach every rival's best shield, whatever the rivals do.
		cost := positive(attack.without(i)+1-d[i]) + positive(shield.without(i)-a[i])
		if cost <= g[i] {
			fmt.Println(i + 1)
			return
		}
	}
	fmt.Println(-1)
}
