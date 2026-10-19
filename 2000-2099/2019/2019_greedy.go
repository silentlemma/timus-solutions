package main

import (
	"bufio"
	"fmt"
	"os"
)

const caseBit = 32

type endpoint struct {
	letter byte
	id     int
}

func solve(n int, word string) []int {
	answer := make([]int, n)
	pending := make([]endpoint, 0, len(word))
	upper, lower := 0, 0
	for i := 0; i < len(word); i++ {
		code := word[i]
		isUpper := code >= 'A' && code <= 'Z'
		index := lower
		if isUpper {
			index = upper
			upper++
		} else {
			lower++
		}
		if len(pending) > 0 && pending[len(pending)-1].letter^code == caseBit {
			previous := pending[len(pending)-1].id
			pending = pending[:len(pending)-1]
			if isUpper {
				answer[index] = previous
			} else {
				answer[previous] = index
			}
		} else {
			pending = append(pending, endpoint{code, index})
		}
	}
	if len(pending) > 0 {
		return nil
	}
	return answer
}

func run(in *bufio.Reader, out *bufio.Writer) {
	var n int
	var word string
	fmt.Fscan(in, &n, &word)
	answer := solve(n, word)
	if answer == nil {
		fmt.Fprintln(out, "Impossible")
		return
	}
	for i, target := range answer {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, target+1)
	}
	fmt.Fprintln(out)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	run(in, out)
}
