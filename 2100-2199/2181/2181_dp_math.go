package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const modulus int64 = 1000000007

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

func countPaths(n, m int, down, right []bool, sourceRow, sourceColumn int) (int64, int64) {
	dp := make([]int64, m)
	var upper, lower int64
	for row := 0; row < n; row++ {
		for column := 0; column < m; column++ {
			index := row*m + column
			var value int64
			if row == sourceRow && column == sourceColumn {
				value = 1
			} else {
				if row > 0 && !down[index-m] {
					value = dp[column]
				}
				if column > 0 && !right[index-1] {
					value += dp[column-1]
				}
				if value >= modulus {
					value -= modulus
				}
			}
			dp[column] = value
			if row == n-2 && column == m-1 {
				upper = value
			}
			if row == n-1 && column == m-2 {
				lower = value
			}
		}
	}
	return upper, lower
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := scanner{data: data}
	n, m, missing := input.nextInt(), input.nextInt(), input.nextInt()
	down := make([]bool, n*m)
	right := make([]bool, n*m)
	for edge := 0; edge < missing; edge++ {
		a, b, c, d := input.nextInt(), input.nextInt(), input.nextInt(), input.nextInt()
		if a == c {
			if b > d {
				b = d
			}
			right[(a-1)*m+b-1] = true
		} else {
			if a > c {
				a = c
			}
			down[(a-1)*m+b-1] = true
		}
	}
	if right[0] || down[0] || down[(n-2)*m+m-1] || right[(n-1)*m+m-2] {
		fmt.Println(0)
		return
	}

	upperUpper, upperLower := countPaths(n, m, down, right, 0, 1)
	lowerUpper, lowerLower := countPaths(n, m, down, right, 1, 0)
	// Swapping tails cancels every pair that shares an internal vertex.
	answer := (upperUpper*lowerLower - upperLower*lowerUpper) % modulus
	answer = (answer + modulus) % modulus
	fmt.Println(answer * 2 % modulus)
}
