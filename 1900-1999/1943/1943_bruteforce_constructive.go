package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const localLimit = 5

func wins(first, second []int) bool {
	first = append([]int(nil), first...)
	second = append([]int(nil), second...)
	firstHead, secondHead := 0, 0
	seen := make(map[string]struct{})
	for firstHead < len(first) && secondHead < len(second) {
		state := fmt.Sprint(first[firstHead:], second[secondHead:])
		if _, found := seen[state]; found {
			return false
		}
		seen[state] = struct{}{}
		x, y := first[firstHead], second[secondHead]
		firstHead++
		secondHead++
		if x > y {
			first = append(first, y, x)
		} else if y > x {
			second = append(second, x, y)
		}
	}
	return firstHead < len(first)
}

func nextPermutation(values []int) bool {
	pivot := len(values) - 2
	for pivot >= 0 && values[pivot] >= values[pivot+1] {
		pivot--
	}
	if pivot < 0 {
		return false
	}
	successor := len(values) - 1
	for values[successor] <= values[pivot] {
		successor--
	}
	values[pivot], values[successor] = values[successor], values[pivot]
	for left, right := pivot+1, len(values)-1; left < right; left, right = left+1, right-1 {
		values[left], values[right] = values[right], values[left]
	}
	return true
}

func construct(opponent []int) []int {
	size := len(opponent)
	if size > localLimit {
		size = localLimit
	}
	candidate := append([]int(nil), opponent[:size]...)
	sort.Ints(candidate)
	for {
		if wins(candidate, opponent[:size]) {
			answer := append([]int(nil), opponent...)
			copy(answer, candidate)
			return answer
		}
		if !nextPermutation(candidate) {
			return nil
		}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var size int
	fmt.Fscan(in, &size)
	opponent := make([]int, size)
	for index := range opponent {
		fmt.Fscan(in, &opponent[index])
	}
	answer := construct(opponent)
	if answer == nil {
		fmt.Fprintln(out, "NO")
		return
	}
	fmt.Fprintln(out, "YES")
	for index, card := range answer {
		if index != 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, card)
	}
	fmt.Fprintln(out)
}
