package main

import (
	"bufio"
	"fmt"
	"os"
)

// edge is a wall or door: kind 0 lies above row r, kind 1 left of column c.
type edge struct{ kind, r, c int }

func edgeOf(r, c int, d byte) edge {
	switch d {
	case 'N':
		return edge{0, r, c}
	case 'S':
		return edge{0, r + 1, c}
	case 'W':
		return edge{1, r, c}
	}
	return edge{1, r, c + 1}
}

type scout struct {
	r, c               int // the position relative to the unknown start
	loR, hiR, loC, hiC int
	seen               map[edge]int     // 1 for a door, 0 for a wall
	byKind             [2][2][]edge     // [kind][door?]: the edges seen
}

var (
	w, h, width int
	scouts      [2]scout
	conflict    []int // reports ruling out the second start being the first shifted
)

// starts gives the start pairs left: 0, 1, or 2 for two or more.
func starts() int {
	a, b := &scouts[0], &scouts[1]
	lo1r, hi1r, lo1c, hi1c := -a.loR, h-1-a.hiR, -a.loC, w-1-a.hiC
	lo2r, hi2r, lo2c, hi2c := -b.loR, h-1-b.hiR, -b.loC, w-1-b.hiC
	total := 0
	for dr := -(h - 1); dr < h; dr++ {
		top, bottom := maxInt(lo1r, lo2r-dr), minInt(hi1r, hi2r-dr)
		if top > bottom {
			continue
		}
		for dc := -(w - 1); dc < w; dc++ {
			if conflict[(dr+h-1)*width+dc+w-1] != 0 {
				continue
			}
			left, right := maxInt(lo1c, lo2c-dc), minInt(hi1c, hi2c-dc)
			if left <= right {
				total += (bottom - top + 1) * (right - left + 1)
				if total > 1 {
					return 2
				}
			}
		}
	}
	return total
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var k int
	if _, err := fmt.Fscan(in, &w, &h, &k); err != nil {
		return
	}
	width = 2*w - 1
	conflict = make([]int, (2*h-1)*width)
	scouts[0].seen, scouts[1].seen = map[edge]int{}, map[edge]int{}
	safe, count := -1, starts()
	for step := 1; step <= k; step++ {
		var report string
		fmt.Fscan(in, &report)
		d, door := report[0], 0
		if report[1] == '+' {
			door = 1
		}
		who := (step - 1) % 2
		me, other := &scouts[who], &scouts[1-who]
		e := edgeOf(me.r, me.c, d)
		changed := false
		if old, ok := me.seen[e]; !ok {
			me.seen[e] = door
			me.byKind[e.kind][door] = append(me.byKind[e.kind][door], e)
			sign := 1
			if who == 1 {
				sign = -1
			}
			for _, f := range other.byKind[e.kind][1-door] {
				dr, dc := sign*(e.r-f.r), sign*(e.c-f.c)
				if -h < dr && dr < h && -w < dc && dc < w {
					conflict[(dr+h-1)*width+dc+w-1]++
					changed = true
				}
			}
		} else if old != door {
			fmt.Printf("A mistake has been made at step number %d\n", step)
			return
		}
		if door == 1 {
			switch d {
			case 'N':
				me.r--
			case 'S':
				me.r++
			case 'W':
				me.c--
			case 'E':
				me.c++
			}
			if me.r < me.loR || me.r > me.hiR || me.c < me.loC || me.c > me.hiC {
				me.loR, me.hiR = minInt(me.loR, me.r), maxInt(me.hiR, me.r)
				me.loC, me.hiC = minInt(me.loC, me.c), maxInt(me.hiC, me.c)
				changed = true
			}
		}
		if changed { // the count changes only with a new conflict or a wider path
			count = starts()
		}
		if count == 0 {
			fmt.Printf("A mistake has been made at step number %d\n", step)
			return
		}
		if count == 1 && safe < 0 {
			safe = step
		}
	}
	if safe > 0 {
		fmt.Printf("The scouts are safe at step number %d\n", safe)
	} else {
		fmt.Println("There is not enough data")
	}
}

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
