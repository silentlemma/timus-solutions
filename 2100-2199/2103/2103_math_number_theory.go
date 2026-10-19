package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	three = int64(3)
	five  = int64(5)
	six   = int64(6)
	seven = int64(7)
	eight = int64(8)
	nine  = int64(9)
)

type result struct {
	cost  int64
	route []int64
}

func makeResult(cost int64, points ...int64) result {
	answer := result{cost: cost}
	for _, point := range points {
		if len(answer.route) == 0 || answer.route[len(answer.route)-1] != point {
			answer.route = append(answer.route, point)
		}
	}
	return answer
}

func solve(source, target int64) result {
	if target <= source {
		return makeResult(source-target, source, target)
	}
	if target%source == 0 {
		return makeResult(0, source, target)
	}

	// A unit-cost route has one adjacent step between two chains of free jumps.
	for divisor := int64(1); divisor*divisor <= target; divisor++ {
		if target%divisor != 0 {
			continue
		}
		for _, point := range []int64{divisor, target / divisor} {
			for _, adjacent := range []int64{point - 1, point + 1} {
				if adjacent >= source && adjacent%source == 0 {
					return makeResult(1, source, adjacent, point, target)
				}
			}
		}
	}

	if source <= five {
		lower := target / source * source
		nearest := lower
		if target-lower > lower+source-target {
			nearest += source
		}
		return makeResult(2, source, nearest, target)
	}

	remaining := target
	for _, factor := range []int64{2, three} {
		for remaining%factor == 0 {
			remaining /= factor
		}
	}
	// This divisor is adjacent to a multiple of six.
	if remaining > 1 {
		adjacent := remaining + 1
		if remaining%six == 1 {
			adjacent = remaining - 1
		}
		return makeResult(2, source, six, adjacent, remaining, target)
	}
	if target%six == 0 {
		return makeResult(2, source, six, target)
	}
	if target%eight == 0 {
		return makeResult(2, source, eight, target)
	}
	if source == seven {
		return makeResult(2, source, nine, target)
	}
	return makeResult(2, source, five, 10, nine, target)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var source, target int64
	if _, err := fmt.Fscan(in, &source, &target); err != nil {
		return
	}
	answer := solve(source, target)
	fmt.Fprintln(out, answer.cost)
	fmt.Fprintln(out, len(answer.route))
	for index, point := range answer.route {
		if index != 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, point)
	}
	fmt.Fprintln(out)
}
