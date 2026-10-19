package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

type input struct {
	data []byte
	at   int
}

func (in *input) number() int {
	for in.at < len(in.data) && in.data[in.at] <= ' ' {
		in.at++
	}
	value := 0
	for in.at < len(in.data) && in.data[in.at] > ' ' {
		value = value*10 + int(in.data[in.at]-'0')
		in.at++
	}
	return value
}

func arrange(values []int, capacity int) (int, []int) {
	sort.Ints(values)
	queue := make([]int, 0, len(values))
	left, right, trips := 0, len(values)-1, 0
	for left < right {
		if values[left]+values[right] > capacity {
			// The largest value cannot share a trip with any remaining value.
			queue = append(queue, values[left], values[right])
			left++
			right--
			trips += 2
		} else {
			queue = append(queue, values[left], values[left+1])
			left += 2
			trips++
		}
	}
	if left == right {
		queue = append(queue, values[left])
		trips++
	}
	return trips, queue
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n, capacity := in.number(), in.number()
	values := make([]int, n)
	for i := range values {
		values[i] = in.number()
	}
	trips, queue := arrange(values, capacity)
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, trips)
	for i, value := range queue {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, value)
	}
	fmt.Fprintln(out)
	out.Flush()
}
