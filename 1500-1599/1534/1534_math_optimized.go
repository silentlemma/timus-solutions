package main

import (
	"io"
	"os"
)

const (
	decimal    = 10
	maxInput   = 64
	maxOutput  = 32
	fieldCount = 3
)

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func scores(scored, conceded, matches int64) (int64, int64) {
	margin := scored - conceded
	var best, worst int64
	switch {
	case margin > 0:
		best, worst = matches+2*min(margin, matches), matches+2
	case margin == 0:
		best, worst = matches, matches
	default:
		best, worst = matches-1, matches-min(-margin, matches)
	}
	// A mixed schedule needs at least one win and one loss.
	if scored > 0 && conceded > 0 && matches > 1 {
		best = max(best, matches-1+2*min(scored, matches-1))
		worst = min(worst, matches+2-min(conceded, matches-1))
	}
	return best, worst
}

func main() {
	var input [maxInput]byte
	size, _ := io.ReadFull(os.Stdin, input[:])
	var fields [fieldCount]int64
	pos := 0
	for i := range fields {
		for pos < size && (input[pos] < '0' || input[pos] > '9') {
			pos++
		}
		for pos < size && input[pos] >= '0' && input[pos] <= '9' {
			fields[i] = fields[i]*decimal + int64(input[pos]-'0')
			pos++
		}
	}
	best, worst := scores(fields[0], fields[1], fields[2])
	var output [maxOutput]byte
	end := len(output) - 1
	output[end] = '\n'
	end = writeDecimal(output[:], end, worst) - 1
	output[end] = ' '
	begin := writeDecimal(output[:], end, best)
	os.Stdout.Write(output[begin:])
}

// Write the digits backwards into the space before end.
func writeDecimal(output []byte, end int, number int64) int {
	for {
		end--
		output[end] = '0' + byte(number%decimal)
		number /= decimal
		if number == 0 {
			return end
		}
	}
}
