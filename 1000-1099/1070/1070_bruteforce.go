package main

import (
	"fmt"
	"strconv"
	"strings"
)

const (
	hour     = 60
	day      = 24 * hour
	longest  = 6 * hour
	spread   = 10
	maxShift = 5
)

func clockMinutes() int {
	var s string
	fmt.Scan(&s)
	parts := strings.SplitN(s, ".", 2)
	h, _ := strconv.Atoi(parts[0])
	m, _ := strconv.Atoi(parts[1])
	return h*hour + m
}

func around(t int) int {
	return (t%day + day) % day
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	out1, in1 := clockMinutes(), clockMinutes()
	out2, in2 := clockMinutes(), clockMinutes()
	// when the second airport is k hours ahead, the real durations are the clock
	// differences minus and plus k hours, taken around the day
	for k := -maxShift; k <= maxShift; k++ {
		t1 := around(in1 - out1 - k*hour)
		t2 := around(in2 - out2 + k*hour)
		if t1 <= longest && t2 <= longest && abs(t1-t2) <= spread {
			fmt.Println(abs(k))
			return
		}
	}
}
