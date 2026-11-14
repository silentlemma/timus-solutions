package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const scale = 1000

func tokenStart(input *bufio.Reader) int {
	for {
		c, err := input.ReadByte()
		if err != nil {
			return -1
		}
		if c > ' ' {
			return int(c)
		}
	}
}

func count(input *bufio.Reader) int {
	first := tokenStart(input)
	value := 0
	if first != '+' {
		value = first - '0'
	}
	for {
		c, err := input.ReadByte()
		if err != nil || c <= ' ' {
			return value
		}
		value = value*10 + int(c-'0')
	}
}

func residue(input *bufio.Reader) int {
	first := tokenStart(input)
	negative := first == '-'
	for first > ' ' && first != '.' {
		c, err := input.ReadByte()
		if err != nil {
			return 0
		}
		first = int(c)
	}
	if first != '.' {
		return 0
	}
	value, place := 0, scale/10
	for {
		c, err := input.ReadByte()
		if err != nil || c <= ' ' {
			break
		}
		value += int(c-'0') * place
		place /= 10
	}
	if negative && value != 0 {
		return scale - value
	}
	return value
}

type keys []uint32

func (k keys) Len() int           { return len(k) }
func (k keys) Less(i, j int) bool { return k[i] < k[j] }
func (k keys) Swap(i, j int)      { k[i], k[j] = k[j], k[i] }

func norm(key uint32) int {
	x, y := int(key)/scale, int(key)%scale
	if scale-x < x {
		x = scale - x
	}
	if scale-y < y {
		y = scale - y
	}
	return x*x + y*y
}

func main() {
	input := bufio.NewReader(os.Stdin)
	n := count(input)
	groups := make(keys, n)
	for i := range groups {
		x, y := residue(input), residue(input)
		groups[i] = uint32(x*scale + y)
	}
	sort.Sort(groups)
	bestCount, bestNorm := 0, 0
	for first := 0; first < n; {
		end := first + 1
		for end < n && groups[first] == groups[end] {
			end++
		}
		frequency := end - first
		if frequency >= bestCount {
			distance := norm(groups[first])
			if frequency > bestCount || distance < bestNorm {
				bestCount, bestNorm = frequency, distance
			}
		}
		first = end
	}
	fmt.Printf("%d %.9f\n", bestCount, math.Sqrt(float64(bestNorm))/scale)
}
