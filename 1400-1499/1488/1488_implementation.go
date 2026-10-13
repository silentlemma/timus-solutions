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
	three     = 3
	cards     = 8 // three of Sasha's, three of Dima's, two in the sleeve
	hand      = 3
	sleeve    = 6
	firstFace = 11 // J, Q, K, A rank from 11 to 14
	faces     = "JQKA"
	keyLength = 4 // the combination and up to three ranks
)

type key [keyLength]int

// combinations from the lowest: high card, pair, flush, straight,
// three of a kind, straight flush, three threes
const (
	high = iota
	pair
	flush
	straight
	triple
	straightFlush
	threeThrees
)

func rankOf(card string) int {
	name := card[:len(card)-1]
	if len(name) == 1 && strings.Contains(faces, name) {
		return firstFace + strings.Index(faces, name)
	}
	r, _ := strconv.Atoi(name)
	return r
}

// value is a key that orders hands from the weakest to the strongest
func value(h []string) key {
	r := []int{rankOf(h[0]), rankOf(h[1]), rankOf(h[2])}
	sort.Sort(sort.Reverse(sort.IntSlice(r)))
	isFlush := h[0][len(h[0])-1] == h[1][len(h[1])-1] && h[1][len(h[1])-1] == h[2][len(h[2])-1]
	isStraight := r[0] == r[1]+1 && r[1] == r[2]+1
	switch {
	case r[0] == three && r[2] == three:
		return key{threeThrees}
	case isStraight && isFlush:
		return key{straightFlush, r[0], r[1], r[2]}
	case r[0] == r[2]:
		return key{triple, r[0], r[1], r[2]}
	case isStraight:
		return key{straight, r[0], r[1], r[2]}
	case isFlush:
		return key{flush, r[0], r[1], r[2]}
	case r[0] == r[1]:
		return key{pair, r[0], r[2]}
	case r[1] == r[2]:
		return key{pair, r[1], r[0]}
	}
	return key{high, r[0], r[1], r[2]}
}

func compare(a, b key) int {
	for i := range a {
		if a[i] != b[i] {
			if a[i] < b[i] {
				return -1
			}
			return 1
		}
	}
	return 0
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for {
		card := make([]string, cards)
		if _, err := fmt.Fscan(reader, &card[0]); err != nil {
			return
		}
		for i := 1; i < cards; i++ {
			fmt.Fscan(reader, &card[i])
		}
		sasha, dima := card[:hand], card[hand:sleeve]
		var usable []string
		for _, c := range card[sleeve:] {
			if c != sasha[0] && c != sasha[1] && c != sasha[2] {
				usable = append(usable, c)
			}
		}
		// Dima's hands: as dealt, one card swapped, or two swapped for both
		hands := [][]string{dima}
		for _, c := range usable {
			for i := 0; i < hand; i++ {
				h := append([]string(nil), dima...)
				h[i] = c
				hands = append(hands, h)
			}
		}
		if len(usable) == 2 {
			for keep := 0; keep < hand; keep++ {
				hands = append(hands, []string{dima[keep], usable[0], usable[1]})
			}
		}
		target := value(sasha)
		win, draw := false, false
		for _, h := range hands {
			if h[0] == h[1] || h[1] == h[2] || h[0] == h[2] {
				continue
			}
			c := compare(value(h), target)
			win = win || c > 0
			draw = draw || c == 0
		}
		switch {
		case win:
			fmt.Fprintln(writer, "Dima")
		case draw:
			fmt.Fprintln(writer, "Artyom")
		default:
			fmt.Fprintln(writer, "Sasha")
		}
	}
}
