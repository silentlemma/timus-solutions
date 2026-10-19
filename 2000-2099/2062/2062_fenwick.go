package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

type Charges struct {
	size          int
	initial, tree []int64
	offsets       []int
	divisors      []uint16
}

func newCharges(initial []int64) *Charges {
	size := len(initial) - 1
	offsets := make([]int, size+2)
	for divisor := 1; divisor*divisor <= size; divisor++ {
		for multiple := divisor * divisor; multiple <= size; multiple += divisor {
			offsets[multiple+1]++
		}
	}
	for index := 1; index <= size+1; index++ {
		offsets[index] += offsets[index-1]
	}
	divisors := make([]uint16, offsets[size+1])
	cursor := append([]int(nil), offsets...)
	for divisor := 1; divisor*divisor <= size; divisor++ {
		for multiple := divisor * divisor; multiple <= size; multiple += divisor {
			divisors[cursor[multiple]] = uint16(divisor)
			cursor[multiple]++
		}
	}
	return &Charges{size, initial, make([]int64, size+1), offsets, divisors}
}

func (charges *Charges) irradiate(left, right int, power int64) {
	for index := left; index <= charges.size; index += index & -index {
		charges.tree[index] += power
	}
	for index := right + 1; index <= charges.size; index += index & -index {
		charges.tree[index] -= power
	}
}

func (charges *Charges) point(index int) int64 {
	var result int64
	for index > 0 {
		result += charges.tree[index]
		index &= index - 1
	}
	return result
}

func (charges *Charges) measure(index int) int64 {
	result := charges.initial[index]
	for at := charges.offsets[index]; at < charges.offsets[index+1]; at++ {
		divisor := int(charges.divisors[at])
		partner := index / divisor
		result += charges.point(divisor)
		if partner != divisor {
			result += charges.point(partner)
		}
	}
	return result
}

type Input struct {
	data []byte
	at   int
}

func (input *Input) next() int {
	for input.at < len(input.data) && input.data[input.at] <= ' ' {
		input.at++
	}
	value := 0
	for input.at < len(input.data) && input.data[input.at] >= '0' {
		value = value*10 + int(input.data[input.at]-'0')
		input.at++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := Input{data: data}
	size := input.next()
	initial := make([]int64, size+1)
	for index := 1; index <= size; index++ {
		initial[index] = int64(input.next())
	}
	charges := newCharges(initial)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	count := input.next()
	for ; count > 0; count-- {
		if input.next() == 1 {
			fmt.Fprintln(output, charges.measure(input.next()))
		} else {
			left, right, power := input.next(), input.next(), int64(input.next())
			charges.irradiate(left, right, power)
		}
	}
}
