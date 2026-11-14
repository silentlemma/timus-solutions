package main

import (
	"bufio"
	"os"
)

const (
	maxFactor    = 100
	lowFPS       = 10
	highFPS      = 60
	decimal      = 10
	alphabetBase = 27
	minArea      = 320 * 200
	maxPower     = 1000000000
	capped       = maxPower/(lowFPS*minArea) + 1
)

func number(input *bufio.Scanner) int {
	input.Scan()
	value := 0
	for _, c := range input.Bytes() {
		value = value*decimal + int(c-'0')
	}
	return value
}

func name(input *bufio.Scanner) uint64 {
	input.Scan()
	var key uint64
	for _, c := range input.Bytes() {
		key = key*alphabetBase + uint64(c-'a'+1)
	}
	return key
}

type effects struct {
	count   [maxFactor + 1]int
	active  int
	product int
}

func (s *effects) multiply(factor int) {
	s.product *= factor
	if s.product >= capped {
		s.product = capped
	}
}

func (s *effects) restore() {
	// Even the weakest eleven effects force a slideshow at minimum resolution.
	const maxExactEffects = 10
	if s.active > maxExactEffects {
		s.product = capped
		return
	}
	s.product = 1
	for factor, count := range s.count {
		for i := 0; i < count; i++ {
			s.multiply(factor)
			if s.product == capped {
				return
			}
		}
	}
}

func (s *effects) add(factor int) {
	s.active++
	s.count[factor]++
	s.multiply(factor)
}

func (s *effects) remove(factor int) {
	s.active--
	s.count[factor]--
	if s.product == capped {
		s.restore()
	} else {
		s.product /= factor
	}
}

func (s *effects) status(area, power int) string {
	if s.product > power/(lowFPS*area) {
		return "Slideshow\n"
	}
	if s.product <= power/(highFPS*area) {
		return "Perfect\n"
	}
	return "So-so\n"
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	n := number(input)
	options := make(map[uint64]uint8, n)
	state := effects{product: 1}
	for i := 0; i < n; i++ {
		key, factor := name(input), number(input)
		options[key] = uint8(factor)
		state.add(factor)
	}
	area := number(input) * number(input)
	power, changes := number(input), number(input)
	output := bufio.NewWriter(os.Stdout)
	output.WriteString(state.status(area, power))
	for i := 0; i < changes; i++ {
		input.Scan()
		switch input.Bytes()[0] {
		case 'R':
			area = number(input) * number(input)
		case 'O':
			on := input.Bytes()[1] == 'n'
			factor := int(options[name(input)])
			if on {
				state.add(factor)
			} else {
				state.remove(factor)
			}
		}
		output.WriteString(state.status(area, power))
	}
	output.Flush()
}
