package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	minutes    = 60
	firstHour  = 7
	withLeonid = 13
	alreadyIn  = 42
)

type bus struct{ start, route int }

var (
	place  [][]int
	buses  []bus
	chosen bus
)

// key orders buses for a trip: by the minute at src, then at dst, then by
// route number
type key struct{ atSrc, atDst, route int }

func (a key) less(b key) bool {
	if a.atSrc != b.atSrc {
		return a.atSrc < b.atSrc
	}
	if a.atDst != b.atDst {
		return a.atDst < b.atDst
	}
	return a.route < b.route
}

// picked tells whether a passenger waiting at src for dst takes the chosen
// bus: no bus seen by Leonid serves the trip and comes to src sooner, or at
// the same minute reaching dst sooner, or as soon with a smaller route
func picked(src, dst int) bool {
	here := place[chosen.route]
	if here[src] < 0 || here[dst] < 0 || here[src] >= here[dst] {
		return false
	}
	mine := key{chosen.start + here[src], chosen.start + here[dst], chosen.route}
	for _, b := range buses {
		there := place[b.route]
		if b.start < 0 || there[src] < 0 || there[dst] < 0 || there[src] >= there[dst] {
			continue
		}
		if (key{b.start + there[src], b.start + there[dst], b.route}).less(mine) {
			return false
		}
	}
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, m int
	if _, err := fmt.Fscan(reader, &n, &m); err != nil {
		return
	}
	order := make([][]int, m)
	place = make([][]int, m)
	for r := 0; r < m; r++ {
		place[r] = make([]int, n+1)
		for s := range place[r] {
			place[r][s] = -1
		}
		for {
			var s int
			fmt.Fscan(reader, &s)
			if s == -1 {
				break
			}
			place[r][s] = len(order[r])
			order[r] = append(order[r], s)
		}
	}
	var k int
	fmt.Fscan(reader, &k)
	for i := 0; i < k; i++ {
		var stamp string
		var route int
		fmt.Fscan(reader, &stamp, &route)
		parts := strings.Split(stamp, ":")
		hh, _ := strconv.Atoi(parts[0])
		mm, _ := strconv.Atoi(parts[1])
		route--
		// the minute this bus left the first stop of its route
		buses = append(buses, bus{(hh-firstHour)*minutes + mm - place[route][1], route})
	}
	chosen = buses[k-1]
	// buses not seen at stop 1 either come to a stop before it later than
	// the chosen bus, or need not run at all
	stops := order[chosen.route]
	one, two := place[chosen.route][1], place[chosen.route][2]
	var leaveNew, stayNew, leaveOld, stayOld bool
	for d := one + 1; d < len(stops); d++ {
		early := d < two
		if picked(1, stops[d]) {
			leaveNew, stayNew = leaveNew || early, stayNew || !early
		}
		for s := 0; s < one; s++ {
			if picked(stops[s], stops[d]) {
				leaveOld, stayOld = leaveOld || early, stayOld || !early
			}
		}
	}
	// each group can all ride to a stop of one kind, so the counts are all
	// or nothing for the 13 who got on with Leonid and the 42 already inside
	count := func(flag bool, size int) int {
		if flag {
			return size
		}
		return 0
	}
	low := count(!leaveNew, withLeonid) + count(!leaveOld, alreadyIn)
	high := count(stayNew, withLeonid) + count(stayOld, alreadyIn)
	fmt.Println(low, high)
}
