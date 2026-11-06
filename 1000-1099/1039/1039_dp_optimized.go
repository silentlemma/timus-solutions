package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	outputSize = 16
)

const maxEmployees = 6000

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	nextInt := func() int {
		in.Scan()
		x, _ := strconv.Atoi(in.Text())
		return x
	}
	n := nextInt()
	var parent, children [maxEmployees + 1]uint16
	var take, skip [maxEmployees + 1]int32
	for employee := 1; employee <= n; employee++ {
		take[employee] = int32(nextInt())
	}
	for child := nextInt(); child != 0; child = nextInt() {
		boss := nextInt()
		parent[child] = uint16(boss)
		children[boss]++
	}
	var ready [maxEmployees]uint16
	queued := 0
	for employee := 1; employee <= n; employee++ {
		if children[employee] == 0 {
			ready[queued] = uint16(employee)
			queued++
		}
	}
	var total int32
	// A boss becomes ready when all direct reports have contributed their scores.
	for head := 0; head < queued; head++ {
		employee := ready[head]
		best := skip[employee]
		if take[employee] > best {
			best = take[employee]
		}
		boss := parent[employee]
		if boss == 0 {
			total += best
			continue
		}
		take[boss] += skip[employee]
		skip[boss] += best
		children[boss]--
		if children[boss] == 0 {
			ready[queued] = boss
			queued++
		}
	}
	var answer [outputSize]byte
	os.Stdout.Write(append(strconv.AppendInt(answer[:0], int64(total), 10), '\n'))
}
