package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

// Seven bits hold a start offset in a command of up to 100 letters.
const offsetBits = 7
const offsetMask = 1<<offsetBits - 1

type suffixes struct {
	words     []string
	positions []uint32
}

func (s suffixes) text(position uint32) string {
	return s.words[position>>offsetBits][position&offsetMask:]
}

func (s suffixes) Len() int           { return len(s.positions) }
func (s suffixes) Less(i, j int) bool { return s.text(s.positions[i]) < s.text(s.positions[j]) }
func (s suffixes) Swap(i, j int) {
	s.positions[i], s.positions[j] = s.positions[j], s.positions[i]
}

func prefix(a, b string) uint8 {
	i := 0
	for i < len(a) && i < len(b) && a[i] == b[i] {
		i++
	}
	return uint8(i)
}

func shortestKeys(words []string, letters int) []string {
	positions := make([]uint32, 0, letters)
	for owner, word := range words {
		for start := range word {
			positions = append(positions, uint32(owner<<offsetBits|start))
		}
	}
	sorted := suffixes{words, positions}
	sort.Sort(sorted)
	adjacent, left := make([]uint8, letters), make([]uint8, letters)
	// Keep the minimum adjacent LCP since the nearest suffix of another command.
	var shared uint8
	for i := 1; i < letters; i++ {
		a, b := positions[i-1], positions[i]
		adjacent[i] = prefix(sorted.text(a), sorted.text(b))
		if a>>offsetBits != b>>offsetBits || adjacent[i] < shared {
			shared = adjacent[i]
		}
		left[i] = shared
	}
	best := append([]string(nil), words...)
	shared = 0
	for i := letters - 1; i >= 0; i-- {
		position := positions[i]
		owner := position >> offsetBits
		if i+1 < letters && (owner != positions[i+1]>>offsetBits || adjacent[i+1] < shared) {
			shared = adjacent[i+1]
		}
		longest := shared
		if left[i] > longest {
			longest = left[i]
		}
		need := int(longest) + 1
		suffix := sorted.text(position)
		if need <= len(suffix) && need < len(best[owner]) {
			best[owner] = suffix[:need]
		}
	}
	return best
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	input.Scan()
	count, _ := strconv.Atoi(input.Text())
	words := make([]string, count)
	letters := 0
	for i := range words {
		input.Scan()
		words[i] = input.Text()
		letters += len(words[i])
	}
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	for _, key := range shortestKeys(words, letters) {
		output.WriteString(key)
		output.WriteByte('\n')
	}
}
