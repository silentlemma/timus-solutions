package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	minute   = 60
	hour     = minute * minute
	day      = 24 * hour
	elements = "AEFW"
	// eps: values closer than this are taken as equal
	eps = 1e-9
)

type element struct{ strong, top, weak, low int }

func seconds(text string) int {
	var h, m, s int
	fmt.Sscanf(text, "%d:%d:%d", &h, &m, &s)
	return h*hour + m*minute + s
}

// power falls linearly from the strong moment to the weak one and rises back
// over the rest of the day
func power(e element, t int) float64 {
	fall := ((e.weak-e.strong)%day + day) % day
	since := ((t-e.strong)%day + day) % day
	if since <= fall {
		return float64(e.top) + float64(e.low-e.top)*float64(since)/float64(fall)
	}
	return float64(e.low) + float64(e.top-e.low)*float64(since-fall)/float64(day-fall)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	moments := map[byte]element{}
	for range elements {
		var code, strong, weak string
		var top, low int
		fmt.Fscan(in, &code, &strong, &top, &weak, &low)
		moments[code[0]] = element{seconds(strong), top, seconds(weak), low}
	}
	var light, dark string
	fmt.Fscan(in, &light, &dark)
	side := map[byte]int{}
	for i := range light {
		side[light[i]]++
	}
	for i := range dark {
		side[dark[i]]--
	}
	advantage := func(t int) float64 {
		sum := 0.0
		for i := range elements {
			if c := side[elements[i]]; c != 0 {
				sum += float64(c) * power(moments[elements[i]], t)
			}
		}
		return sum
	}
	// the advantage is linear between the moments, so its largest value over
	// the day is at a moment or at either end of the day
	seen := map[int]bool{0: true, day - 1: true}
	for _, e := range moments {
		seen[e.strong], seen[e.weak] = true, true
	}
	var times []int
	for t := range seen {
		times = append(times, t)
	}
	sort.Ints(times)
	when, best := -1, 0.0
	for _, t := range times {
		if v := advantage(t); when < 0 || v > best+eps {
			best, when = v, t
		}
	}
	if best <= eps {
		fmt.Println("We can't win!")
	} else {
		fmt.Printf("%02d:%02d:%02d\n%.2f\n", when/hour, when/minute%minute, when%minute, best)
	}
}
