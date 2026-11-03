package main

import (
	"bufio"
	"fmt"
	"os"
)

const longest, top = 100, 9
const maxSum, none = longest * top, longest + 1

var low, high [maxSum + 1]int
var offset [maxSum + 2]int
var fewest []byte

func lookup(total, squares int) int {
	if total < 0 || total > maxSum || squares < total || (squares-total)%2 != 0 {
		return none
	}
	b := (squares - total) / 2
	if b < low[total] || b > high[total] {
		return none
	}
	return int(fewest[offset[total]+b-low[total]])
}

func main() {
	for total := 0; total <= maxSum; total++ {
		// Compress parity into b=(squareSum-total)/2. Balance 100 slots for
		// its minimum and pack nines for its maximum, bounding each row.
		q, r := total/longest, total%longest
		least := (longest-r)*q*q + r*(q+1)*(q+1)
		q, r = total/top, total%top
		greatest := q*top*top + r*r
		low[total], high[total] = (least-total)/2, (greatest-total)/2
		offset[total+1] = offset[total] + high[total] - low[total] + 1
	}
	fewest = make([]byte, offset[maxSum+1])
	for i := range fewest {
		fewest[i] = none
	}
	fewest[0] = 0
	for total := 1; total <= maxSum; total++ {
		destination := offset[total] - low[total]
		for digit := 1; digit <= top && digit <= total; digit++ {
			previous, delta := total-digit, digit*(digit-1)/2
			first, last := low[total], high[total]
			if low[previous]+delta > first {
				first = low[previous] + delta
			}
			if high[previous]+delta < last {
				last = high[previous] + delta
			}
			shift := offset[previous] - low[previous] - delta - destination
			for position := destination + first; position <= destination+last; position++ {
				value := fewest[position+shift] + 1
				if value < fewest[position] {
					fewest[position] = value
				}
			}
		}
	}
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var tests int
	fmt.Fscan(in, &tests)
	for ; tests > 0; tests-- {
		var total, squares int
		fmt.Fscan(in, &total, &squares)
		size := lookup(total, squares)
		if size == none {
			fmt.Fprintln(out, "No solution")
			continue
		}
		digits := make([]byte, 0, size)
		digit := 1
		for left := size - 1; left >= 0; left-- {
			for lookup(total-digit, squares-digit*digit) != left {
				digit++
			}
			digits = append(digits, byte('0'+digit))
			total -= digit
			squares -= digit * digit
		}
		fmt.Fprintln(out, string(digits))
	}
}
