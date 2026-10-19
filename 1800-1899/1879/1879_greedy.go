package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const letters = 100000

func main() {
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	scanner.Split(bufio.ScanWords)
	next := func() int {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return v
	}
	readCounts := func() (int64, []int64) {
		length := next()
		count := make([]int64, letters+1)
		for i := 0; i < length; i++ {
			count[next()]++
		}
		return int64(length), count
	}
	n, a := readCounts()
	m, b := readCounts()
	// every position of t meets every position of the cyclic s exactly once,
	// so the distance is n m minus the number of equal pairs
	p, q := a[0], b[0]
	a[0], b[0] = 0, 0
	var equal, same, maxA, maxB int64
	for c := 1; c <= letters; c++ {
		equal += a[c] * b[c]
		if g := p*b[c] + q*a[c]; g > same {
			same = g
		}
		if a[c] > maxA {
			maxA = a[c]
		}
		if b[c] > maxB {
			maxB = b[c]
		}
	}
	// the gain is linear in the letters chosen for the question marks of one
	// string, so all of them take one letter: the same letter for both
	// strings, or the best letter for each
	same += p * q
	best := p*maxB + q*maxA
	if same > best {
		best = same
	}
	fmt.Println(n*m - equal - best)
}
