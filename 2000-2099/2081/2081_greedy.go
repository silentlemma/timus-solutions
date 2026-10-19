package main

import (
	"bufio"
	"fmt"
	"os"
)

var digits = []string{"._.|.||_|", ".....|..|", "._.._||_.", "._.._|._|", "...|_|..|",
	"._.|_.._|", "._.|_.|_|", "._...|..|", "._.|_||_|", "._.|_|._|"}

var columns = []int{0, 4, 10, 14} // where the four digits start

const (
	width   = 3
	seconds = 60 // MM:SS runs from 00:00 to 59:59
)

// fits tells whether every lit segment belongs to the digit
func fits(shown string, digit int) bool {
	for i := 0; i < len(shown); i++ {
		if shown[i] != '.' && shown[i] != digits[digit][i] {
			return false
		}
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	previous := seconds * seconds
	for r := 0; r < n; r++ {
		rows := make([]string, width)
		for i := range rows {
			fmt.Fscan(in, &rows[i])
		}
		ok := make([][10]bool, len(columns))
		for k, c := range columns {
			cell := ""
			for _, row := range rows {
				cell += row[c : c+width]
			}
			for d := 0; d < 10; d++ {
				ok[k][d] = fits(cell, d)
			}
		}
		// the largest time that fits and stays below the previous one leaves the
		// most room for the rest, so it never spoils a solution
		value := previous - 1
		for {
			m, s := value/seconds, value%seconds
			all := true
			for k, d := range []int{m / 10, m % 10, s / 10, s % 10} {
				all = all && ok[k][d]
			}
			if all {
				fmt.Fprintf(out, "%02d:%02d\n", m, s)
				break
			}
			value--
		}
		previous = value
	}
}
