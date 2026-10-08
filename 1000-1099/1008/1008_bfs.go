package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	maxCoord = 10
	side     = maxCoord + 2
	letters  = "RTLB"
)

var (
	dx = [len(letters)]int{1, 0, -1, 0}
	dy = [len(letters)]int{0, 1, 0, -1}
)

type pixel struct{ x, y int }

// describe: breadth-first search from the lowest of the leftmost pixels, each
// line naming the neighbours seen for the first time.
func describe(out *bufio.Writer, black *[side][side]bool, count int) {
	var start pixel
	for x := maxCoord; x >= 1; x-- {
		for y := maxCoord; y >= 1; y-- {
			if black[x][y] {
				start = pixel{x, y}
			}
		}
	}
	queue := []pixel{start}
	black[start.x][start.y] = false
	fmt.Fprintln(out, start.x, start.y)
	for head := 0; head < count; head++ {
		p := queue[head]
		var line strings.Builder
		for d := range letters {
			q := pixel{p.x + dx[d], p.y + dy[d]}
			if black[q.x][q.y] {
				black[q.x][q.y] = false
				queue = append(queue, q)
				line.WriteByte(letters[d])
			}
		}
		if head+1 < count {
			line.WriteByte(',')
		} else {
			line.WriteByte('.')
		}
		fmt.Fprintln(out, line.String())
	}
}

// list replays the same search: the lines tell which pixels it adds.
func list(out *bufio.Writer, start pixel, lines []string) {
	queue := []pixel{start}
	for head, line := range lines {
		p := queue[head]
		for _, c := range line {
			if d := strings.IndexRune(letters, c); d >= 0 {
				queue = append(queue, pixel{p.x + dx[d], p.y + dy[d]})
			}
		}
	}
	sort.Slice(queue, func(i, j int) bool {
		if queue[i].x != queue[j].x {
			return queue[i].x < queue[j].x
		}
		return queue[i].y < queue[j].y
	})
	fmt.Fprintln(out, len(queue))
	for _, p := range queue {
		fmt.Fprintln(out, p.x, p.y)
	}
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	var tokens []string
	for sc.Scan() {
		tokens = append(tokens, sc.Text())
	}
	num := func(i int) int {
		v, _ := strconv.Atoi(tokens[i])
		return v
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// only the description ends with a full stop
	if strings.HasSuffix(tokens[len(tokens)-1], ".") {
		list(out, pixel{num(0), num(1)}, tokens[2:])
		return
	}
	var black [side][side]bool
	count := num(0)
	for i := 0; i < count; i++ {
		black[num(1+2*i)][num(2+2*i)] = true
	}
	describe(out, &black, count)
}
