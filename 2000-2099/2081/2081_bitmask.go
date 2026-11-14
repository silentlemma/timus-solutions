package main

import (
	"bufio"
	"math/bits"
	"os"
	"strconv"
)

const (
	seconds      = 60
	width        = 3
	tensValues   = seconds / 10
	clockDigits  = 4
	lineWidth    = 6
	secondsUnits = clockDigits - 1
)

// Each bit indicates a lit cell in the corresponding 3-by-3 glyph.
var glyph = [10]int{490, 288, 242, 434, 312, 410, 474, 290, 506, 442}
var column = [clockDigits]int{0, 4, 10, 14}

func pairMask(tens, units int) uint64 {
	var unitMask uint64
	for digit, shape := range glyph {
		if units&shape == units {
			unitMask |= 1 << digit
		}
	}
	var mask uint64
	for digit, shape := range glyph[:tensValues] {
		if tens&shape == tens {
			mask |= unitMask << (10 * digit)
		}
	}
	return mask
}

func largestAtMost(mask uint64, bound int) int {
	return bits.Len64(mask&((uint64(1)<<(bound+1))-1)) - 1
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	input.Scan()
	count, _ := strconv.Atoi(input.Text())
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()

	bound := seconds*seconds - 1
	for reading := 0; reading < count; reading++ {
		var lit [clockDigits]int
		for row := 0; row < width; row++ {
			input.Scan()
			line := input.Bytes()
			for digit, start := range column {
				for cell := 0; cell < width; cell++ {
					if line[start+cell] != '.' {
						lit[digit] |= 1 << (row*width + cell)
					}
				}
			}
		}
		minutes := pairMask(lit[0], lit[1])
		secondMask := pairMask(lit[2], lit[secondsUnits])
		// Take the largest feasible time so every smaller time remains available.
		m, s := bound/seconds, bound%seconds
		bestSecond := largestAtMost(secondMask, s)
		if minutes&(uint64(1)<<m) == 0 || bestSecond < 0 {
			m = largestAtMost(minutes, m-1)
			bestSecond = bits.Len64(secondMask) - 1
		}
		result := [lineWidth]byte{byte(m/10) + '0', byte(m%10) + '0', ':',
			byte(bestSecond/10) + '0', byte(bestSecond%10) + '0', '\n'}
		output.Write(result[:])
		bound = m*seconds + bestSecond - 1
	}
}
