package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
	"strings"
)

const rounds = 300000 // large neighbourhood search rounds
const share = 50      // the first threshold is the first cost over this
const most = 8        // at most this many random items removed at once

const kinds = 3          // removal kinds: random items, a whole trip, one client
const unreached = 0xFFFF // no path yet in the subset table

// xorshift64 from a fixed seed: the same numbers in every language
const seed = 88172645463325252
const shiftA, shiftB, shiftC = 13, 7, 17

var rngState uint64 = seed

func below(k int) int {
	rngState ^= rngState << shiftA
	rngState ^= rngState >> shiftB
	rngState ^= rngState << shiftC
	return int(rngState % uint64(k))
}

var m, n, capacity int
var dist [][]int
var weight, client, tour []int
var path []uint16 // path[S*m+j]: shortest walk from the depot through S ending at j

var trip, load, clients []int // trip of each item; per trip the load and the client set
var perClient [][]int         // perClient[t][c]: items of client c in trip t
var cost int64

func put(i, t int) {
	if t == len(load) {
		load = append(load, 0)
		clients = append(clients, 0)
		perClient = append(perClient, make([]int, m))
	}
	cost -= int64(tour[clients[t]])
	trip[i] = t
	load[t] += weight[i]
	perClient[t][client[i]]++
	if perClient[t][client[i]] == 1 {
		clients[t] |= 1 << uint(client[i])
	}
	cost += int64(tour[clients[t]])
}

func take(i int) {
	t := trip[i]
	cost -= int64(tour[clients[t]])
	load[t] -= weight[i]
	perClient[t][client[i]]--
	if perClient[t][client[i]] == 0 {
		clients[t] &^= 1 << uint(client[i])
	}
	cost += int64(tour[clients[t]])
	trip[i] = -1
}

// insertBest: the cheapest place for item i, an existing trip or a new one; the
// first trip that costs no more than a new one, so that emptied trips are reused.
func insertBest(i int) {
	fresh := len(load)
	best, bit := fresh, 1<<uint(client[i])
	extra := tour[bit]
	for t := 0; t < fresh; t++ {
		if load[t]+weight[i] > capacity {
			continue
		}
		d := tour[clients[t]|bit] - tour[clients[t]]
		if d < extra || (d == extra && best == fresh) {
			extra, best = d, t
		}
	}
	put(i, best)
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	m, n, capacity = next(), next(), next()
	dist = make([][]int, m+1)
	for i := range dist {
		dist[i] = make([]int, m+1)
		for j := range dist[i] {
			dist[i][j] = next()
		}
	}
	weight, client = make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		weight[i], client[i] = next(), next()-1
	}
	// Held-Karp over the clients: shortest walks from the depot through every subset
	full := 1 << uint(m)
	path = make([]uint16, full*m)
	for i := range path {
		path[i] = unreached
	}
	tour = make([]int, full)
	for j := 0; j < m; j++ {
		path[(1<<uint(j))*m+j] = uint16(dist[0][j+1])
	}
	for s := 1; s < full; s++ {
		best := unreached
		// only the clients in s can end the walk, only the others can come next
		for js := uint(s); js != 0; js &= js - 1 {
			j := bits.TrailingZeros(js)
			here := int(path[s*m+j])
			if here+dist[j+1][0] < best {
				best = here + dist[j+1][0]
			}
			for ks := ^uint(s) & uint(full-1); ks != 0; ks &= ks - 1 {
				k := bits.TrailingZeros(ks)
				at := (s|1<<uint(k))*m + k
				if v := here + dist[j+1][k+1]; v < int(path[at]) {
					path[at] = uint16(v)
				}
			}
		}
		tour[s] = best
	}
	// a first plan by cheapest insertion; then rounds of removing some items
	// and putting them back in the cheapest places, undone when the cost grows
	// by more than a threshold that falls to zero
	trip = make([]int, n)
	for i := range trip {
		trip[i] = -1
	}
	for i := 0; i < n; i++ {
		insertBest(i)
	}
	bestTrip := append([]int(nil), trip...)
	bestCost, start := cost, cost
	var removed, oldTrip []int
	for round := 0; round < rounds; round++ {
		before := cost
		removed, oldTrip = removed[:0], oldTrip[:0]
		kind := below(kinds)
		limit := n
		if most < limit {
			limit = most
		}
		count := 1 + below(limit)
		pick := below(n)
		target := client[pick]
		if kind == 1 {
			target = trip[pick]
		}
		for i := 0; i < n; i++ {
			if (kind == 1 && trip[i] == target) || (kind == 2 && client[i] == target) {
				removed = append(removed, i)
				oldTrip = append(oldTrip, trip[i])
			}
		}
		for k := 0; kind == 0 && k < count; k++ {
			i, seen := below(n), false
			for _, r := range removed {
				seen = seen || r == i
			}
			if !seen {
				removed = append(removed, i)
				oldTrip = append(oldTrip, trip[i])
			}
		}
		for _, i := range removed {
			take(i)
		}
		for k := len(removed) - 1; k > 0; k-- {
			r := below(k + 1)
			removed[k], removed[r] = removed[r], removed[k]
			oldTrip[k], oldTrip[r] = oldTrip[r], oldTrip[k]
		}
		for _, i := range removed {
			insertBest(i)
		}
		threshold := start * int64(rounds-round) / rounds / share
		if cost > before+threshold {
			for _, i := range removed {
				take(i)
			}
			for k, i := range removed {
				put(i, oldTrip[k])
			}
		}
		if cost < bestCost {
			bestCost = cost
			bestTrip = append(bestTrip[:0], trip...)
		}
	}
	// rebuild the best plan and print its non-empty trips, each route
	// recovered from the subset table
	trips := 0
	for _, t := range bestTrip {
		if t+1 > trips {
			trips = t + 1
		}
	}
	load, clients, perClient = make([]int, trips), make([]int, trips), make([][]int, trips)
	for t := range perClient {
		perClient[t] = make([]int, m)
	}
	cost = 0
	for i := 0; i < n; i++ {
		put(i, bestTrip[i])
	}
	var used []int
	for t := 0; t < trips; t++ {
		if clients[t] != 0 {
			used = append(used, t)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintf(out, "%d\n\n", len(used))
	total := 0
	for _, t := range used {
		var items []string
		for i := 0; i < n; i++ {
			if trip[i] == t {
				items = append(items, strconv.Itoa(i+1))
			}
		}
		fmt.Fprintf(out, "%s\n%d\n", strings.Join(items, " "), load[t])
		s := clients[t]
		length, last := tour[s], -1
		for j := 0; j < m && last < 0; j++ {
			if s>>uint(j)&1 == 1 && int(path[s*m+j])+dist[j+1][0] == length {
				last = j
			}
		}
		var route []int
		for s != 0 {
			route = append(route, last+1)
			prev, rest := -1, s&^(1<<uint(last))
			for j := 0; j < m && rest != 0 && prev < 0; j++ {
				if rest>>uint(j)&1 == 1 && int(path[rest*m+j])+dist[j+1][last+1] == int(path[s*m+last]) {
					prev = j
				}
			}
			s, last = rest, prev
		}
		fmt.Fprint(out, "0")
		for k := len(route) - 1; k >= 0; k-- {
			fmt.Fprintf(out, " %d", route[k])
		}
		fmt.Fprintf(out, " 0\n%d\n\n", length)
		total += length
	}
	fmt.Fprintln(out, total)
}
