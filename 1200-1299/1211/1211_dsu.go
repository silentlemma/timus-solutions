package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	maxChildren = 25000
	bufferSize  = 4096
)

func nextInt(input *bufio.Scanner) int16 {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return int16(value)
}

func root(sets []int16, child int16) int16 {
	for sets[child] > 0 {
		parent := sets[child]
		if sets[parent] > 0 {
			sets[child] = sets[parent]
		}
		child = sets[child]
	}
	return child
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	var storage [maxChildren + 1]int16
	sets := storage[:]
	output := bufio.NewWriter(os.Stdout)
	for tests := nextInt(input); tests > 0; tests-- {
		size := nextInt(input)
		for child := int16(1); child <= size; child++ {
			sets[child] = -1
		}
		confessions := 0
		consistent := true
		for child := int16(1); child <= size; child++ {
			named := nextInt(input)
			if named == 0 {
				confessions++
			} else if consistent {
				a, b := root(sets, child), root(sets, named)
				if a == b {
					consistent = false
					continue
				}
				if sets[a] > sets[b] {
					a, b = b, a
				}
				sets[a] += sets[b]
				sets[b] = a
			}
		}
		if consistent && confessions == 1 {
			output.WriteString("YES\n")
		} else {
			output.WriteString("NO\n")
		}
	}
	output.Flush()
}
