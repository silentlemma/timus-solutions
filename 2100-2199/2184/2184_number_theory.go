package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

type fastInput struct {
	data     []byte
	position int
}

func (input *fastInput) nextUint64() uint64 {
	for input.position < len(input.data) && input.data[input.position] <= ' ' {
		input.position++
	}
	var value uint64
	for input.position < len(input.data) && input.data[input.position] > ' ' {
		value = value*10 + uint64(input.data[input.position]-'0')
		input.position++
	}
	return value
}

func gcd(left, right uint64) uint64 {
	for right != 0 {
		left, right = right, left%right
	}
	return left
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := fastInput{data: data}
	n := int(input.nextUint64())
	values := make([]uint64, n)
	var total uint64
	for index := range values {
		values[index] = input.nextUint64()
		total += values[index]
	}

	// The two exceptional chests change a prefix and a suffix gcd.
	marked := make([]bool, n)
	current := total
	for index, value := range values {
		next := gcd(current, value)
		if next != current {
			marked[index] = true
		}
		current = next
	}
	current = total
	for index := n; index > 0; {
		index--
		next := gcd(current, values[index])
		if next != current {
			marked[index] = true
		}
		current = next
	}

	fixed := total
	critical := make([]uint64, 0)
	for index, value := range values {
		if marked[index] {
			critical = append(critical, value)
		} else {
			fixed = gcd(fixed, value)
		}
	}

	count := len(critical)
	suffix := make([]uint64, count+1)
	suffix[count] = fixed
	for index := count; index > 0; {
		index--
		suffix[index] = gcd(critical[index], suffix[index+1])
	}
	answer := suffix[0]
	before := fixed
	for first := 0; first < count; first++ {
		running := before
		for second := first + 1; second < count; second++ {
			candidate := gcd(running, suffix[second+1])
			if candidate > answer {
				answer = candidate
			}
			running = gcd(running, critical[second])
		}
		before = gcd(before, critical[first])
	}

	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(output, answer)
	output.Flush()
}
