package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxDigit = 9

func firstCheapest(input *bufio.Reader, count, width int) int {
	if width > count {
		return 0
	}
	window := make([]byte, width)
	slot, length, total := 0, 0, 0
	best, bestTotal := 0, maxDigit*width+1
	for position := 1; position <= count; {
		state, err := input.ReadByte()
		if err != nil {
			return best
		}
		if state == '*' {
			slot, length, total = 0, 0, 0
		} else if state >= '0' && state <= '9' {
			if length == width {
				total -= int(window[slot])
			} else {
				length++
			}
			digit := state - '0'
			window[slot] = digit
			total += int(digit)
			slot++
			if slot == width {
				slot = 0
			}
			if length == width && total < bestTotal {
				best, bestTotal = position-width+1, total
				if total == 0 {
					return best
				}
			}
		} else {
			continue
		}
		position++
	}
	return best
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count, width int
	if _, err := fmt.Fscan(input, &count, &width); err != nil {
		return
	}
	fmt.Println(firstCheapest(input, count, width))
}
