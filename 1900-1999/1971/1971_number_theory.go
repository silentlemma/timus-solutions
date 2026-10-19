package main

import (
	"bufio"
	"fmt"
	"os"
)

const factorLimit = 100
const lowFPS = 10
const highFPS = 60

type factor struct{ prime, exponent int }

func factorTable() ([]int, [factorLimit + 1][]factor) {
	primes := []int{}
	var factors [factorLimit + 1][]factor
	for value := 2; value <= factorLimit; value++ {
		remaining := value
		for _, prime := range primes {
			exponent := 0
			for remaining%prime == 0 {
				remaining /= prime
				exponent++
			}
			if exponent != 0 {
				factors[value] = append(factors[value], factor{prime, exponent})
			}
		}
		if remaining > 1 {
			factors[value] = append(factors[value], factor{remaining, 1})
			if remaining == value {
				primes = append(primes, value)
			}
		}
	}
	return primes, factors
}

func classify(width, height, power int, counts *[factorLimit + 1]int, primes []int) string {
	area := width * height
	limit := power / (lowFPS * area)
	if limit == 0 {
		return "Slideshow"
	}
	product := 1
	for _, prime := range primes {
		for step := 0; step < counts[prime]; step++ {
			if product > limit/prime {
				return "Slideshow"
			}
			product *= prime
		}
	}
	if product <= power/(highFPS*area) {
		return "Perfect"
	}
	return "So-so"
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	primes, factors := factorTable()
	var counts [factorLimit + 1]int
	var n int
	fmt.Fscan(in, &n)
	options := make(map[string]int, n)
	for i := 0; i < n; i++ {
		var name string
		var value int
		fmt.Fscan(in, &name, &value)
		options[name] = value
		for _, part := range factors[value] {
			counts[part.prime] += part.exponent
		}
	}
	var width, height, power, changes int
	fmt.Fscan(in, &width, &height, &power, &changes)
	fmt.Fprintln(out, classify(width, height, power, &counts, primes))
	for i := 0; i < changes; i++ {
		var command string
		fmt.Fscan(in, &command)
		if command == "Resolution" {
			fmt.Fscan(in, &width, &height)
		} else {
			var name string
			fmt.Fscan(in, &name)
			change := -1
			if command == "On" {
				change = 1
			}
			for _, part := range factors[options[name]] {
				counts[part.prime] += change * part.exponent
			}
		}
		fmt.Fprintln(out, classify(width, height, power, &counts, primes))
	}
}
