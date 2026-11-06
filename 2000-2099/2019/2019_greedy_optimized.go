package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	caseBit   = 'a' ^ 'A'
	fieldSize = 8
	decimal   = 10
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	pairs, _ := strconv.Atoi(input.Text())
	if !input.Scan() {
		return
	}
	word := input.Bytes()
	// Reuse the part of the input already read as the stack of letters.
	letters := word[:0]
	ids := make([]uint16, 0, len(word))
	answer := make([]uint16, pairs+1)
	var upper, lower uint16
	for _, ch := range word {
		capital := ch >= 'A' && ch <= 'Z'
		var id uint16
		if capital {
			upper++
			id = upper
		} else {
			lower++
			id = lower
		}
		last := len(letters) - 1
		if last >= 0 && letters[last]^ch == caseBit {
			previous := ids[last]
			letters, ids = letters[:last], ids[:last]
			if capital {
				answer[id] = previous
			} else {
				answer[previous] = id
			}
		} else {
			letters = append(letters, ch)
			ids = append(ids, id)
		}
	}
	if len(letters) != 0 {
		os.Stdout.WriteString("Impossible\n")
		return
	}
	output := bufio.NewWriter(os.Stdout)
	var storage [fieldSize]byte
	for i, index := range answer[1:] {
		if i > 0 {
			output.WriteByte(' ')
		}
		output.Write(strconv.AppendUint(storage[:0], uint64(index), decimal))
	}
	output.WriteByte('\n')
	output.Flush()
}
