package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
)

const upperCount = 26

type node struct {
	next     [2]int
	fail     int
	terminal bool
}

func symbolIndex(letter byte) int {
	if letter <= 'Z' {
		return int(letter - 'A')
	}
	return int(letter-'a') + upperCount
}

func solve(fields [][]byte) int {
	k, _ := strconv.Atoi(string(fields[0]))
	message := fields[1]
	codes := fields[2 : k+2]
	singletons, good := 0, byte('0')
	capacity := 1
	for _, code := range codes {
		capacity += len(code)
		if len(code) == 1 {
			singletons++
			good = code[0]
		}
	}
	if singletons == 0 {
		answer := 0
		for _, letter := range message {
			answer += len(codes[symbolIndex(letter)])
		}
		return answer
	}
	if singletons == 2 {
		return -1
	}

	bad := byte('0' + '1' - good)
	weights := make([]int, k)
	reversed := make([][]byte, k)
	nodes := make([]node, 1, capacity)
	for symbol, code := range codes {
		reversed[symbol] = make([]byte, len(code))
		state := 0
		for position := len(code) - 1; position >= 0; position-- {
			bit := code[position]
			reversed[symbol][len(code)-1-position] = bit
			if bit == bad {
				weights[symbol]++
			}
			edge := int(bit - '0')
			if nodes[state].next[edge] == 0 {
				nodes[state].next[edge] = len(nodes)
				nodes = append(nodes, node{})
			}
			state = nodes[state].next[edge]
		}
		nodes[state].terminal = true
	}
	totalBad := 0
	for _, letter := range message {
		totalBad += weights[symbolIndex(letter)]
	}
	if totalBad == 0 {
		return -1
	}

	queue := make([]int, 0, len(nodes))
	for bit := 0; bit < 2; bit++ {
		if nodes[0].next[bit] != 0 {
			queue = append(queue, nodes[0].next[bit])
		}
	}
	for head := 0; head < len(queue); head++ {
		state := queue[head]
		fallback := nodes[state].fail
		nodes[state].terminal = nodes[state].terminal || nodes[fallback].terminal
		for bit := 0; bit < 2; bit++ {
			child := nodes[state].next[bit]
			if child == 0 {
				nodes[state].next[bit] = nodes[fallback].next[bit]
			} else {
				nodes[child].fail = nodes[fallback].next[bit]
				queue = append(queue, child)
			}
		}
	}

	// Cache complete codeword transitions instead of expanding the message.
	cache := make([]int, len(nodes)*k)
	state, tailBad := 0, 0
	for position := len(message) - 1; position >= 0; position-- {
		symbol := symbolIndex(message[position])
		key := state*k + symbol
		edge := cache[key]
		if edge == 0 {
			next, consumed := state, 0
			for _, bit := range reversed[symbol] {
				if bit == bad {
					consumed++
				}
				next = nodes[next].next[int(bit-'0')]
				if !nodes[next].terminal {
					edge = -consumed
					break
				}
			}
			if edge == 0 {
				edge = next + 1
			}
			cache[key] = edge
		}
		if edge < 0 {
			return totalBad - tailBad + edge + 1
		}
		state = edge - 1
		tailBad += weights[symbol]
	}
	return -1
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	fmt.Println(solve(bytes.Fields(data)))
}
