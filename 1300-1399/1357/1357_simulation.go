package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	specificHeat = 4190 // J/(kg K)
	portionGrams = 200
	cold         = 20 // degrees
	boiling      = 100
	power        = 400 // W

	// heating one portion takes C m dT / P seconds; with m in grams this is
	// exactly the number of milliseconds, 167 600
	portionMs = specificHeat * portionGrams * (boiling - cold) / power
	capacity  = 5 // portions in a full teakettle
	ms        = 1000
	minute    = 60
	hour      = minute * minute
	day       = 24 * hour
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	wake := make([]int64, n)
	ready := make([]int64, n)
	for i := range wake {
		var h, m, s int64
		var t string
		fmt.Fscan(in, &t)
		fmt.Sscanf(t, "%d:%d:%d", &h, &m, &s)
		wake[i] = (h*hour + m*minute + s) * ms
	}
	var kettle, waiting []int
	var boil int64 // the moment the water in the kettle boils, in milliseconds
	i := 0
	for i < n || len(kettle) > 0 {
		// water that boils exactly when someone wakes up is poured out first
		if len(kettle) > 0 && (i == n || wake[i] >= boil) {
			for _, j := range kettle {
				ready[j] = boil
			}
			take := len(waiting)
			if take > capacity {
				take = capacity
			}
			kettle = append([]int(nil), waiting[:take]...)
			waiting = waiting[take:]
			boil += portionMs * int64(len(kettle))
			continue
		}
		if len(kettle) == 0 {
			kettle = []int{i}
			boil = wake[i] + portionMs
		} else if len(kettle) < capacity {
			// the heat still missing grows by one portion's worth
			kettle = append(kettle, i)
			boil += portionMs
		} else {
			waiting = append(waiting, i)
		}
		i++
	}
	for _, t := range ready {
		sec := (t + ms - 1) / ms % day // rounded up, past midnight from 00:00:00
		fmt.Fprintf(out, "%02d:%02d:%02d\n", sec/hour, sec/minute%minute, sec%minute)
	}
}
