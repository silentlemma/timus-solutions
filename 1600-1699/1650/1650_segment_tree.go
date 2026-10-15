package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	name, city, money := make([]string, n), make([]string, n), make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &name[i], &city[i], &money[i])
	}
	var m, k int
	fmt.Fscan(in, &m, &k)
	day, who, to := make([]int, k), make([]string, k), make([]string, k)
	for i := 0; i < k; i++ {
		fmt.Fscan(in, &day[i], &who[i], &to[i])
	}
	cityID := map[string]int{}
	var cityName []string
	id := func(c string) int {
		if v, ok := cityID[c]; ok {
			return v
		}
		cityID[c] = len(cityName)
		cityName = append(cityName, c)
		return cityID[c]
	}
	for _, c := range city {
		id(c)
	}
	for _, c := range to {
		id(c)
	}
	size := 1
	for size < len(cityName) {
		size *= 2
	}
	// a max tree over cities: the best total, how many leaves reach it,
	// and one of them
	best := make([]int64, 2*size)
	count, where := make([]int, 2*size), make([]int, 2*size)
	for c := 0; c < size; c++ {
		count[size+c], where[size+c] = 1, c
	}
	for i := size - 1; i > 0; i-- {
		count[i], where[i] = count[2*i]+count[2*i+1], where[2*i]
	}
	add := func(c int, amount int64) {
		i := c + size
		best[i] += amount
		for i /= 2; i > 0; i /= 2 {
			a, b := 2*i, 2*i+1
			switch {
			case best[a] > best[b]:
				best[i], count[i], where[i] = best[a], count[a], where[a]
			case best[a] < best[b]:
				best[i], count[i], where[i] = best[b], count[b], where[b]
			default:
				best[i], count[i], where[i] = best[a], count[a]+count[b], where[a]
			}
		}
	}
	home, wealth := map[string]int{}, map[string]int64{}
	for i := 0; i < n; i++ {
		home[name[i]], wealth[name[i]] = id(city[i]), money[i]
		add(home[name[i]], money[i])
	}
	days := make([]int, len(cityName))
	lead := func(span int) {
		if span > 0 && count[1] == 1 { // a strict leader only
			days[where[1]] += span
		}
	}
	today := 1
	for i := 0; i < k; i++ {
		// the moves of a day count from the next morning
		lead(day[i] + 1 - today)
		if day[i]+1 > today {
			today = day[i] + 1
		}
		add(home[who[i]], -wealth[who[i]])
		home[who[i]] = id(to[i])
		add(home[who[i]], wealth[who[i]])
	}
	lead(m + 1 - today)
	var leaders []int
	for c, d := range days {
		if d > 0 {
			leaders = append(leaders, c)
		}
	}
	sort.Slice(leaders, func(a, b int) bool { return cityName[leaders[a]] < cityName[leaders[b]] })
	for _, c := range leaders {
		fmt.Fprintln(out, cityName[c], days[c])
	}
}
