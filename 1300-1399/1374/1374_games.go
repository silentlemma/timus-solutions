package main

import (
	"fmt"
	"math/bits"
	"strings"
)

const (
	players   = 3
	suits     = 4
	ranks     = 8
	handSize  = 10 // cards per player
	suitBits  = 14 // an owner string of a suit fits in this many bits
	cacheBits = 20 // 8 MB of remembered positions, well inside 16 MB
	fullSuit  = 1<<ranks - 1
	golden    = 0x9E3779B97F4A7C15
	keyBits   = 64
)

var rankNames = []string{"7", "8", "9", "10", "J", "Q", "K", "A"}

// hand[p] holds player p's cards, suit s in bits 8 s .. 8 s + 7, rank upwards
var hand [players]uint32
var cache = make([]uint64, 1<<cacheBits)

// key: the suits play alike and only the order of the cards inside a suit
// matters, so a position is the sorted owner strings of the suits. Fixed
// arrays instead of slices: no garbage, so the heap stays near the cache size.
func key(leader int) uint64 {
	var codes [suits]int
	for s := 0; s < suits; s++ {
		v := 1
		for c := s * ranks; c < (s+1)*ranks; c++ {
			for p := 0; p < players; p++ {
				if hand[p]>>uint(c)&1 == 1 {
					v = v*players + p
				}
			}
		}
		i := s
		for ; i > 0 && codes[i-1] > v; i-- {
			codes[i] = codes[i-1]
		}
		codes[i] = v
	}
	k := uint64(leader + 1)
	for _, v := range codes {
		k = k<<suitBits | uint64(v)
	}
	return k
}

// choices: one card from each run of touching cards, where no other
// player's card lies between two cards of a run.
func choices(p int, allowed, everyone uint32) (out [handSize]int, n int) {
	for c := 0; c < suits*ranks; c++ {
		if allowed>>uint(c)&1 == 0 {
			continue
		}
		s := c / ranks
		below := everyone & (1<<uint(c) - 1) & (fullSuit << uint(s*ranks))
		if below == 0 || hand[p]>>uint(bits.Len32(below)-1)&1 == 0 {
			out[n] = c
			n++
		}
	}
	return out, n
}

// play: the first player looks for any good card, the other two for any
// card that makes the first player take the trick.
func play(leader, step, suit, best, bestPlayer int, everyone uint32) bool {
	p := (leader + step) % players
	allowed := hand[p]
	if step > 0 && allowed&(fullSuit<<uint(suit*ranks)) != 0 {
		allowed &= fullSuit << uint(suit*ranks)
	}
	cards, n := choices(p, allowed, everyone)
	for _, c := range cards[:n] {
		s, b, bp := suit, best, bestPlayer
		if step == 0 {
			s, b, bp = c/ranks, c, p
		} else if c/ranks == suit && c > best {
			b, bp = c, p
		}
		hand[p] &^= 1 << uint(c)
		var ok bool
		if step+1 < players {
			ok = play(leader, step+1, s, b, bp, everyone)
		} else {
			ok = bp != 0 && survive(bp)
		}
		hand[p] |= 1 << uint(c)
		if ok == (p == 0) {
			return ok
		}
	}
	return p != 0
}

// survive: can the first player take no trick from here, whatever the others do.
func survive(leader int) bool {
	if hand[0] == 0 {
		return true
	}
	k := key(leader)
	slot := (k * golden) >> (keyBits - cacheBits)
	if cache[slot]>>1 == k {
		return cache[slot]&1 == 1
	}
	result := play(leader, 0, 0, -1, -1, hand[0]|hand[1]|hand[2])
	cache[slot] = k << 1
	if result {
		cache[slot] |= 1
	}
	return result
}

func main() {
	for p := 0; p < players; p++ {
		for i := 0; i < handSize; i++ {
			var t string
			fmt.Scan(&t)
			s := strings.IndexByte("SCDH", t[len(t)-1])
			r := 0
			for rankNames[r] != t[:len(t)-1] {
				r++
			}
			hand[p] |= 1 << uint(s*ranks+r)
		}
	}
	var leader int
	fmt.Scan(&leader)
	if survive(leader - 1) {
		fmt.Println(";)")
	} else {
		fmt.Println(";(")
	}
}
