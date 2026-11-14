package main

import (
	"os"
	"strconv"
)

const (
	maxText  = 4000
	maxWidth = 1000
	maxField = 7 // six decimal digits and a separator
	inputPad = 32
)

var (
	input    [maxText + inputPad]byte
	repeated [maxText + 2*maxWidth]byte
	common   [maxWidth]uint16
	best     [maxText + 2*maxWidth]uint16
	answer   [maxText]int
	output   [maxText * maxField]byte
)

func count(text []byte, width int) {
	size := len(text)
	lastStart := size + width - 2
	tape := repeated[:lastStart+width]
	for i := 0; i < len(tape); i += size {
		copy(tape[i:], text)
	}
	for start := lastStart; start >= 0; start-- {
		window := tape[start : start+width]
		prefix := best[start : start+width]
		total := width
		for distance, letter := range window[1:] {
			distance++
			shared := uint16(0)
			if letter == window[0] {
				shared = common[distance] + 1
				if shared > prefix[distance] {
					prefix[distance] = shared
				}
			}
			common[distance] = shared
			// Each start contributes only lengths without an earlier match.
			if fresh := width - distance - int(prefix[distance]); fresh > 0 {
				total += fresh
			}
		}
		if start < size {
			answer[start] = total
		}
	}
}

func main() {
	size := 0
	for size < len(input) {
		n, err := os.Stdin.Read(input[size:])
		size += n
		if err != nil || n == 0 {
			break
		}
	}
	i, width := 0, 0
	for i < size && input[i] <= ' ' {
		i++
	}
	for i < size && input[i] >= '0' && input[i] <= '9' {
		width = width*10 + int(input[i]-'0')
		i++
	}
	for i < size && input[i] <= ' ' {
		i++
	}
	j := i
	for j < size && input[j] > ' ' {
		j++
	}
	text := input[i:j]
	fixed := true
	for _, letter := range text[1:] {
		fixed = fixed && letter == text[0]
	}
	if width == 1 || fixed {
		for i := range text {
			answer[i] = width
		}
	} else {
		count(text, width)
	}
	out := output[:0]
	for _, value := range answer[:len(text)] {
		out = strconv.AppendInt(out, int64(value), 10)
		out = append(out, ' ')
	}
	out[len(out)-1] = '\n'
	os.Stdout.Write(out)
}
