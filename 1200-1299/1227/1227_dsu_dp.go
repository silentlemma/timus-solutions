package main

import "os"

const (
	maxCities = 100
	inputSize = 4096
	decimal   = 10
)

type road struct {
	length int
	to     uint8
	next   uint8
}

var input [inputSize]byte
var cursor, available int
var sets [maxCities + 1]uint8
var head [maxCities + 1]uint8
var roads [2 * maxCities]road
var roadIndex uint8
var visited [maxCities + 1]bool
var diameter int

func nextByte() byte {
	if cursor == available {
		available, _ = os.Stdin.Read(input[:])
		cursor = 0
		if available == 0 {
			return 0
		}
	}
	ch := input[cursor]
	cursor++
	return ch
}

func nextInt() int {
	ch := nextByte()
	for ch != 0 && ch <= ' ' {
		ch = nextByte()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = value*decimal + int(ch-'0')
		ch = nextByte()
	}
	return value
}

func root(city uint8) uint8 {
	for sets[city] != city {
		sets[city] = sets[sets[city]]
		city = sets[city]
	}
	return city
}

func addRoad(from, to uint8, length int) {
	roadIndex++
	roads[roadIndex] = road{length: length, to: to, next: head[from]}
	head[from] = roadIndex
}

func depth(city, parent uint8) int {
	visited[city] = true
	longest := 0
	for index := head[city]; index != 0; index = roads[index].next {
		edge := roads[index]
		if edge.to == parent {
			continue
		}
		branch := edge.length + depth(edge.to, city)
		if longest+branch > diameter {
			diameter = longest + branch
		}
		if branch > longest {
			longest = branch
		}
	}
	return longest
}

func possible(cities uint8, count, target int) bool {
	if target == 0 {
		return true
	}
	for city := uint8(1); city <= cities; city++ {
		sets[city] = city
	}
	for i := 0; i < count; i++ {
		left, right := uint8(nextInt()), uint8(nextInt())
		length := nextInt()
		a, b := root(left), root(right)
		if a == b {
			return true
		}
		sets[a] = b
		// The forest has at most maxCities - 1 roads before the first cycle.
		addRoad(left, right, length)
		addRoad(right, left, length)
	}
	for city := uint8(1); city <= cities; city++ {
		if !visited[city] {
			depth(city, 0)
			if diameter >= target {
				return true
			}
		}
	}
	return false
}

func main() {
	cities, count, target := uint8(nextInt()), nextInt(), nextInt()
	if possible(cities, count, target) {
		os.Stdout.WriteString("YES\n")
	} else {
		os.Stdout.WriteString("NO\n")
	}
}
