package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

type scanner struct {
	data []byte
	pos  int
}

func (s *scanner) nextInt() int {
	for s.pos < len(s.data) && s.data[s.pos] <= ' ' {
		s.pos++
	}
	value := 0
	for s.pos < len(s.data) && s.data[s.pos] >= '0' && s.data[s.pos] <= '9' {
		value = value*10 + int(s.data[s.pos]-'0')
		s.pos++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	if len(data) == 0 {
		return
	}
	in := scanner{data: data}
	suits, ranks, rows := in.nextInt(), in.nextInt(), in.nextInt()
	total := suits * ranks
	indegree := make([]int, total)
	left := make([]int, total)
	for card := 0; card < total; card++ {
		left[card] = -1
		if card%ranks != 0 {
			indegree[card] = 1
		}
	}
	for row := 0; row < rows; row++ {
		length := in.nextInt()
		previous := -1
		for column := 0; column < length; column++ {
			suit, rank := in.nextInt(), in.nextInt()
			card := (suit-1)*ranks + rank - 1
			left[card] = previous
			if previous != -1 {
				indegree[previous]++
			}
			previous = card
		}
	}

	queue := make([]int, 0, total)
	for card := 0; card < total; card++ {
		if indegree[card] == 0 {
			queue = append(queue, card)
		}
	}
	for head := 0; head < len(queue); head++ {
		card := queue[head]
		// Removing a card may unlock its suit successor and its left neighbor.
		if card%ranks+1 < ranks {
			next := card + 1
			indegree[next]--
			if indegree[next] == 0 {
				queue = append(queue, next)
			}
		}
		if left[card] != -1 {
			next := left[card]
			indegree[next]--
			if indegree[next] == 0 {
				queue = append(queue, next)
			}
		}
	}
	if len(queue) != total {
		os.Stdout.WriteString("NO\n")
		return
	}
	answer := make([]byte, 0, len(data)+len("YES\n"))
	answer = append(answer, "YES\n"...)
	for _, card := range queue {
		answer = strconv.AppendInt(answer, int64(card/ranks+1), 10)
		answer = append(answer, ' ')
		answer = strconv.AppendInt(answer, int64(card%ranks+1), 10)
		answer = append(answer, '\n')
	}
	os.Stdout.Write(answer)
}
