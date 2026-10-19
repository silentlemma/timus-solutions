package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	maxMinutes  = 300
	maxDivisor  = maxMinutes + 1
	wheelPrimes = 6
	usedBits    = 6
)

type wheel struct {
	period int
	prefix []int
}

type counter struct {
	primes      []int
	primeCounts []int
	wheels      []wheel
	memo        map[int64]int
	base        int
}

func newCounter() *counter {
	limit := maxDivisor * maxDivisor
	composite := make([]bool, limit+1)
	composite[0], composite[1] = true, true
	for divisor := 2; divisor*divisor <= limit; divisor++ {
		if !composite[divisor] {
			for number := divisor * divisor; number <= limit; number += divisor {
				composite[number] = true
			}
		}
	}
	c := &counter{primeCounts: make([]int, limit+1)}
	for number := 1; number <= limit; number++ {
		c.primeCounts[number] = c.primeCounts[number-1]
		if !composite[number] {
			c.primeCounts[number]++
			if number <= maxDivisor {
				c.primes = append(c.primes, number)
			}
		}
	}
	c.wheels = append(c.wheels, wheel{1, []int{0, 1}})
	period := 1
	for used := 1; used <= wheelPrimes; used++ {
		period *= c.primes[used-1]
		blocked := make([]bool, period+1)
		for _, divisor := range c.primes[:used] {
			for number := divisor; number <= period; number += divisor {
				blocked[number] = true
			}
		}
		prefix := make([]int, period+1)
		for number := 1; number <= period; number++ {
			prefix[number] = prefix[number-1]
			if !blocked[number] {
				prefix[number]++
			}
		}
		c.wheels = append(c.wheels, wheel{period, prefix})
	}
	return c
}

func (c *counter) phi(value, remaining int) int {
	if remaining == c.base {
		w := c.wheels[c.base]
		return value/w.period*w.prefix[w.period] + w.prefix[value%w.period]
	}
	if value == 0 {
		return 0
	}
	last := c.primes[remaining-1]
	if value < last {
		return 1
	}
	if value < last*last {
		return 1 + c.primeCounts[value] - remaining
	}
	key := int64(value)<<usedBits | int64(remaining)
	if cached, found := c.memo[key]; found {
		return cached
	}
	result := c.phi(value, remaining-1) - c.phi(value/last, remaining-1)
	c.memo[key] = result
	return result
}

func (c *counter) countYears(start, duration, minutes int) int {
	limit := minutes + 1
	used := c.primeCounts[limit]
	c.base = used
	if c.base > wheelPrimes {
		c.base = wheelPrimes
	}
	c.memo = make(map[int64]int)
	finish := start + duration
	result := c.phi(finish, used) - c.phi(start, used)
	lower := start
	if lower > limit {
		lower = limit
	}
	upper := finish
	if upper > limit {
		upper = limit
	}
	return result + c.primeCounts[upper] - c.primeCounts[lower]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var start, duration, minutes int
	fmt.Fscan(in, &start, &duration, &minutes)
	c := newCounter()
	fmt.Fprintln(out, c.countYears(start, duration, minutes))
}
