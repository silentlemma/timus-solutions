package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

// FNV-1a of the whole input seeds splitmix64; the arrangements are never
// decoded, they only make the seed differ between tests
const (
	fnvOffset uint64 = 0xcbf29ce484222325
	fnvPrime  uint64 = 0x100000001b3
	golden    uint64 = 0x9e3779b97f4a7c15
	mixA      uint64 = 0xbf58476d1ce4e5b9
	mixB      uint64 = 0x94d049bb133111eb
	shiftA           = 30
	shiftB           = 27
	shiftC           = 31
)

var state uint64

func nextRandom() uint64 {
	state += golden
	z := state
	z = (z ^ (z >> shiftA)) * mixA
	z = (z ^ (z >> shiftB)) * mixB
	return z ^ (z >> shiftC)
}

func main() {
	input, _ := ioutil.ReadAll(os.Stdin)
	state = fnvOffset
	for _, c := range input {
		state = (state ^ uint64(c)) * fnvPrime
	}
	games, _ := strconv.Atoi(strings.Fields(string(input))[0])
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for game := 0; game < games; game++ {
		n := game + 2
		// a bubble sort network: every white ball ends left of every black one
		for end := n - 1; end >= 1; end-- {
			for i := 1; i <= end; i++ {
				out.WriteString("? " + strconv.Itoa(i) + " " + strconv.Itoa(i+1) + "\n")
			}
		}
		j := 1 + int(nextRandom()%uint64(n-1))
		out.WriteString("! " + strconv.Itoa(j) + " " + strconv.Itoa(j+1) + "\n")
	}
}
