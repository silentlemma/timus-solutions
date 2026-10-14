package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	cars, where, run := make([]int, n), make([]int, n+1), make([]int, n+1)
	for i := range cars {
		fmt.Fscan(in, &cars[i])
		where[cars[i]] = i
	}
	// cut 1..n into the fewest runs of numbers that already stand in order, and
	// a new run starts where car v + 1 stands before car v
	for car := 2; car <= n; car++ {
		run[car] = run[car-1]
		if where[car] < where[car-1] {
			run[car]++
		}
	}
	passes := 0
	for 1<<passes <= run[n] {
		passes++
	}
	fmt.Fprintln(out, passes)
	for bit := 0; ; bit++ {
		for i, car := range cars {
			if i > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(car))
		}
		out.WriteByte('\n')
		if bit == passes {
			break
		}
		// pass b sends the cars whose run number has bit b set to the right, and
		// like a radix sort from the low bit up, the passes leave the runs in order
		next := make([]int, 0, n)
		for side := 0; side < 2; side++ {
			for _, car := range cars {
				if run[car]>>bit&1 == side {
					next = append(next, car)
				}
			}
		}
		cars = next
	}
}
