package main

import (
	"bufio"
	"os"
	"strconv"
)

const whole = 10000

func number(in *bufio.Scanner) int {
	in.Scan()
	value, _ := strconv.Atoi(in.Text())
	return value
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	n := number(in)
	low, high, unknown, ceiling := 0, 0, 0, whole
	for i := 0; i < n; i++ {
		in.Scan() // ingredient name
		if number(in) == 0 {
			unknown++
			continue
		}
		share := number(in)
		// The run can use the preceding share as its ceiling and this one as its floor.
		low += (unknown + 1) * share
		high += unknown*ceiling + share
		ceiling, unknown = share, 0
	}
	low += unknown
	high += unknown * ceiling
	if low <= whole && whole <= high {
		os.Stdout.WriteString("YES\n")
	} else {
		os.Stdout.WriteString("NO\n")
	}
}
