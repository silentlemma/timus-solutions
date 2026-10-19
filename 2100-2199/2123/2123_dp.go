package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime/debug"
)

const memoryThreshold = 1 << 16

// Each processed type trades one mass bit for one multiplicity bit.
const initialMassBits = 62

func lowerBound(values []uint64, target, mask uint64) int {
	left, right := 0, len(values)
	for left < right {
		middle := left + (right-left)/2
		if (values[middle] & mask) < target {
			left = middle + 1
		} else {
			right = middle
		}
	}
	return left
}

func merge(current []uint64, mass, remaining uint64, massBits uint, next []uint64) (int, uint64) {
	mask := uint64(1)<<massBits - 1
	baseEnd := lowerBound(current, remaining+1, mask)
	reverseStart := lowerBound(current, mass-remaining, mask)
	forward := lowerBound(current, mass+1, mask)
	reverse := forward - 1
	base := 0
	nextSize := 0
	var answer uint64
	write := next != nil
	sentinel := mass + remaining + 1
	// Folding negative residuals gives three sorted streams.
	for base < baseEnd || reverse >= reverseStart || forward < len(current) {
		key := sentinel
		if base < baseEnd {
			key = (current[base] & mask)
		}
		if reverse >= reverseStart && mass-(current[reverse]&mask) < key {
			key = mass - (current[reverse] & mask)
		}
		if forward < len(current) && (current[forward]&mask)-mass < key {
			key = (current[forward] & mask) - mass
		}
		var count uint64
		if base < baseEnd && (current[base]&mask) == key {
			if write {
				count += (current[base] >> massBits)
			}
			base++
		}
		if reverse >= reverseStart && mass-(current[reverse]&mask) == key {
			if write {
				count += (current[reverse] >> massBits)
			}
			reverse--
		}
		if forward < len(current) && (current[forward]&mask)-mass == key {
			if write {
				count += (current[forward] >> massBits)
			}
			forward++
		}
		if key == 0 {
			answer += count
		} else {
			if write {
				next[nextSize] = count<<(massBits-1) | key
			}
			nextSize++
		}
	}
	return nextSize, answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var size int
	var target uint64
	fmt.Fscan(input, &size, &target)
	weights := make([]uint64, size)
	var remaining uint64
	for index := range weights {
		fmt.Fscan(input, &weights[index])
		remaining += weights[index]
	}
	if target < remaining {
		target = remaining - target
	} else {
		target -= remaining
	}
	if target > remaining {
		fmt.Println(0)
		return
	}
	if target == 0 {
		fmt.Println(1)
		return
	}

	massBits := uint(initialMassBits)
	current := []uint64{uint64(1)<<massBits | target}
	var answer uint64
	for index := size - 1; index >= 0; index-- {
		mass := weights[index]
		remaining -= mass
		// Count first so the next frontier needs no spare capacity.
		nextSize, _ := merge(current, mass, remaining, massBits, nil)
		next := make([]uint64, nextSize)
		_, completed := merge(current, mass, remaining, massBits, next)
		answer += completed
		current = next
		massBits--
		if nextSize >= memoryThreshold {
			debug.FreeOSMemory()
		}
		if len(current) == 0 {
			break
		}
	}
	fmt.Println(answer)
}
