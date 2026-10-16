package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// bus holds the first and the last minute it may enter
type bus struct{ ready, last int64 }

func main() {
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	scanner.Split(bufio.ScanWords)
	next := func() int64 {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return int64(v)
	}
	var sides [2][]bus
	for s := range sides {
		count := int(next())
		side := make([]bus, count)
		for i := range side {
			t, p := next(), next()
			side[i] = bus{t, t + p - 1}
		}
		// a bus must enter before the next one on its side
		for i := count - 2; i >= 0; i-- {
			if side[i].last > side[i+1].last-1 {
				side[i].last = side[i+1].last - 1
			}
		}
		sides[s] = side
	}
	var head [2]int
	now := int64(0)
	for head[0] < len(sides[0]) || head[1] < len(sides[1]) {
		// among the waiting front buses, the one with the earlier last minute
		pick := -1
		soonest := int64(-1)
		for s := 0; s < 2; s++ {
			if head[s] == len(sides[s]) {
				continue
			}
			b := sides[s][head[s]]
			if soonest < 0 || b.ready < soonest {
				soonest = b.ready
			}
			if b.ready <= now && (pick < 0 || b.last < sides[pick][head[pick]].last) {
				pick = s
			}
		}
		if pick < 0 {
			now = soonest
			continue
		}
		if now > sides[pick][head[pick]].last {
			fmt.Println("NO")
			return
		}
		head[pick]++
		now++
	}
	fmt.Println("YES")
}
