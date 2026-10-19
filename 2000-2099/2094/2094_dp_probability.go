package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const (
	percent     = 100
	outputScale = int64(1000000000)
	half        = 0.5
	minDecimals = 3
)

func main() {
	input := bufio.NewReader(os.Stdin)
	var seatCount, vacancyPercent int
	var seats string
	fmt.Fscan(input, &seatCount, &vacancyPercent, &seats)
	left, right, occupiedLeft := 0, 0, 0
	beforeOwnSeat := true
	for _, seat := range seats {
		if seat == '2' {
			beforeOwnSeat = false
		} else if seat == '0' {
			if beforeOwnSeat {
				left++
			} else {
				right++
			}
		} else if beforeOwnSeat {
			occupiedLeft++
		}
	}

	empty := left + right
	step := make([]float64, empty+1)
	expected := make([]float64, empty+1)
	arrival, remaining := 0.0, 0.0
	// Observed arrivals update the distribution of the final audience size.
	for count := 1; count <= empty; count++ {
		weight := float64(count * (percent - vacancyPercent))
		arrival = weight / (weight + float64((empty-count+1)*vacancyPercent)*(1-arrival))
		remaining = arrival * (1 + remaining)
		step[count] = arrival / float64(count)
		expected[count] = remaining / float64(count)
	}

	best := make([]float64, right+1)
	// The current cell compares sitting now with waiting for the next arrival.
	for l := 1; l <= left; l++ {
		for r := 1; r <= right; r++ {
			count := l + r
			stop := float64(r) * expected[count]
			wait := step[count] * (float64(l)*(1+best[r]) + float64(r)*best[r-1])
			if stop < wait {
				best[r] = stop
			} else {
				best[r] = wait
			}
		}
	}

	answer := float64(occupiedLeft) + best[right]
	rounded := int64(math.Floor(answer*float64(outputScale) + half))
	fraction := strconv.FormatInt(rounded%outputScale+outputScale, 10)[1:]
	for len(fraction) > minDecimals && fraction[len(fraction)-1] == '0' {
		fraction = fraction[:len(fraction)-1]
	}
	fmt.Printf("%d.%s\n", rounded/outputScale, fraction)
}
