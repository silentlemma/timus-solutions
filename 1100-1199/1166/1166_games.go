package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strings"
)

// skips are the cards after which the second player loses the turn: 6, 7,
// ace, king of spades; the face-up card before the first move gets the next
// index
var skips []string

type top struct {
	value, suit, announced byte // announced is 0 unless it is a queen
	index                  int
}

func covers(card string, t top) bool {
	if t.announced != 0 {
		return card[1] == t.announced
	}
	return card[1] == t.suit || card[0] == t.value
}

var real []string
var last string
var jokers int
var failed []bool

func topOf(k int) top {
	return top{skips[k][0], skips[k][1], 0, k}
}

// finish lays the cards still left after t, or reports false; every card
// but the last must make the opponent skip, and the last may be anything
func finish(mask, used int, t top, out *[]string) bool {
	rest := len(real) - bits.OnesCount(uint(mask)) + jokers - used
	if last != "" {
		rest++
	}
	if rest == 1 {
		if last != "" {
			if !covers(last, t) {
				return false
			}
			if last[0] == 'Q' {
				*out = append(*out, last+last[1:2])
			} else {
				*out = append(*out, last)
			}
			return true
		}
		if used < jokers {
			suit := t.suit
			if t.announced != 0 {
				suit = t.announced
			}
			*out = append(*out, "*2"+string(suit))
			return true
		}
		for k := range real {
			if mask>>k&1 == 0 {
				if !covers(real[k], t) {
					return false
				}
				*out = append(*out, real[k])
				return true
			}
		}
	}
	key := (mask*(jokers+1)+used)*(len(skips)+1) + t.index
	if failed[key] {
		return false
	}
	for k := range real {
		if mask>>k&1 == 0 && covers(real[k], t) {
			s := 0
			for skips[s] != real[k] {
				s++
			}
			*out = append(*out, real[k])
			if finish(mask|1<<k, used, topOf(s), out) {
				return true
			}
			*out = (*out)[:len(*out)-1]
		}
	}
	if used < jokers {
		for s := range skips {
			if covers(skips[s], t) {
				*out = append(*out, "*"+skips[s])
				if finish(mask, used+1, topOf(s), out) {
					return true
				}
				*out = (*out)[:len(*out)-1]
			}
		}
	}
	failed[key] = true
	return false
}

func main() {
	for _, v := range "67A" {
		for _, s := range "SCDH" {
			skips = append(skips, string(v)+string(s))
		}
	}
	skips = append(skips, "KS")
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')
	var faceUp string
	fmt.Fscan(in, &faceUp)
	faceUp = strings.TrimLeft(faceUp, "*")
	t := top{faceUp[0], faceUp[1], 0, len(skips)}
	if faceUp[0] == 'Q' {
		t.announced = faceUp[2]
	}
	others := 0
	for _, word := range strings.Fields(line) {
		isSkip := false
		for _, s := range skips {
			isSkip = isSkip || s == word
		}
		if word == "*" {
			jokers++
		} else if isSkip {
			real = append(real, word)
		} else {
			last = word
			others++
		}
	}
	if others > 1 {
		fmt.Println("NO")
		return
	}
	failed = make([]bool, (1<<len(real))*(jokers+1)*(len(skips)+1))
	var order []string
	if !finish(0, 0, t, &order) {
		fmt.Println("NO")
		return
	}
	fmt.Println("YES")
	fmt.Println(strings.Join(order, " "))
}
