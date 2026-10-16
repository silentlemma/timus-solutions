package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	n, h, d int
	lefts   []int
)

// spot is the place of a left end on the line from start, or -1 if none
func spot(value, start int) int {
	diff := value - start
	if diff%d != 0 {
		return -1
	}
	step := diff / d
	if step < 0 || step >= n {
		return -1
	}
	return step
}

// choices gives the places of strip k unturned and turned, -1 for none
func choices(k, start int) (int, int) {
	var a, b int
	if d != 0 {
		a, b = spot(lefts[k], start), spot(h-d-lefts[k], start)
	} else {
		// with a flat line every strip keeps its own place in the order
		a, b = -1, -1
		if lefts[k] == start {
			a = k
		}
		if h-lefts[k] == start {
			b = k
		}
	}
	if a == b {
		b = -1
	}
	return a, b
}

// arrange gives the strips in order, signed when turned over, if their left
// ends can be start, start + d, ..., start + (n - 1) d, and nil otherwise
func arrange(start int) []int {
	place := make([]int, n)
	var flexible []int
	for k := 0; k < n; k++ {
		a, b := choices(k, start)
		if a < 0 && b < 0 {
			return nil
		}
		if a >= 0 && b >= 0 {
			flexible = append(flexible, k)
			continue
		}
		step, sign := a, 1
		if a < 0 {
			step, sign = b, -1
		}
		if place[step] != 0 {
			return nil
		}
		place[step] = sign * (k + 1)
	}
	// a strip that fits two places pairs place i with place K - i, so only
	// strips of the same pair compete once the strips with one choice are in
	for _, k := range flexible {
		a, b := choices(k, start)
		switch {
		case place[a] == 0:
			place[a] = k + 1
		case place[b] == 0:
			place[b] = -(k + 1)
		default:
			return nil
		}
	}
	return place
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	if _, err := fmt.Fscan(reader, &h, &n); err != nil {
		return
	}
	lefts = make([]int, n)
	rights := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &lefts[i], &rights[i])
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	// turning a strip over keeps its slope, so all slopes must be equal; the
	// left end x of a strip turns into h - d - x
	d = rights[0] - lefts[0]
	for i := 0; i < n; i++ {
		if rights[i]-lefts[i] != d {
			fmt.Fprintln(writer, 0)
			return
		}
	}
	starts := []int{lefts[0], h - lefts[0]}
	if d != 0 {
		low, high := h, 0
		for _, x := range lefts {
			for _, v := range []int{x, h - d - x} {
				if v < low {
					low = v
				}
				if v > high {
					high = v
				}
			}
		}
		// the strip with the extreme end either starts the line or, turned,
		// ends it
		first, last := low, high
		if d < 0 {
			first, last = high, low
		}
		starts = []int{first, last - (n-1)*d}
	}
	for _, start := range starts {
		if place := arrange(start); place != nil {
			for i, v := range place {
				if i > 0 {
					writer.WriteByte(' ')
				}
				writer.WriteString(strconv.Itoa(v))
			}
			writer.WriteByte('\n')
			return
		}
	}
	fmt.Fprintln(writer, 0)
}
