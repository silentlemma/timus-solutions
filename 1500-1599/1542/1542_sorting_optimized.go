package main

import (
	"bufio"
	"bytes"
	"os"
	"sort"
	"strconv"
)

const (
	maxWordLength = 15
	suggestions   = 10
)

type entry struct {
	frequency int32
	word      [maxWordLength]byte
	length    uint8
}

type matches struct {
	indices [suggestions]uint32
	count   int
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	number := func() int {
		input.Scan()
		value, _ := strconv.Atoi(input.Text())
		return value
	}
	words := make([]entry, number())
	for i := range words {
		input.Scan()
		words[i].length = uint8(copy(words[i].word[:], input.Bytes()))
		words[i].frequency = int32(number())
	}
	sort.Slice(words, func(i, j int) bool {
		a, b := &words[i], &words[j]
		if a.frequency != b.frequency {
			return a.frequency > b.frequency
		}
		return bytes.Compare(a.word[:], b.word[:]) < 0
	})

	queryIDs := make([]int, number())
	lookup := make(map[string]int)
	answers := []matches{{}}
	var requested [maxWordLength + 1]bool
	for i := range queryIDs {
		input.Scan()
		prefix := input.Bytes()
		if len(prefix) > maxWordLength {
			continue
		}
		requested[len(prefix)] = true
		id := lookup[string(prefix)]
		if id == 0 {
			id = len(answers)
			lookup[string(prefix)] = id
			answers = append(answers, matches{})
		}
		queryIDs[i] = id
	}
	var lengths []int
	for length := 1; length <= maxWordLength; length++ {
		if requested[length] {
			lengths = append(lengths, length)
		}
	}
	for i := range words {
		word := &words[i]
		for _, length := range lengths {
			if length > int(word.length) {
				break
			}
			if id := lookup[string(word.word[:length])]; id != 0 {
				answer := &answers[id]
				if answer.count < suggestions {
					answer.indices[answer.count] = uint32(i)
					answer.count++
				}
			}
		}
	}
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	for i, id := range queryIDs {
		if i > 0 {
			output.WriteByte('\n')
		}
		answer := &answers[id]
		for _, index := range answer.indices[:answer.count] {
			word := &words[index]
			output.Write(word.word[:word.length])
			output.WriteByte('\n')
		}
	}
}
