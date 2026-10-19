package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const wordBits = 64

type input struct {
	data []byte
	pos  int
}

func (in *input) next() []byte {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	start := in.pos
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		in.pos++
	}
	return in.data[start:in.pos]
}

func (in *input) integer() int {
	value := 0
	for _, digit := range in.next() {
		value = value*10 + int(digit-'0')
	}
	return value
}

func readSet(in *input, masks []uint64, offset int) {
	for bit, digit := range in.next() {
		if digit == '1' {
			masks[offset+bit/wordBits] |= uint64(1) << uint(bit%wordBits)
		}
	}
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n, m := in.integer(), in.integer()
	words := (n + wordBits - 1) / wordBits
	required := make([]uint64, m*words)
	added := make([]uint64, m*words)
	owned := make([]uint64, words)
	for rule := 0; rule < m; rule++ {
		readSet(&in, required, rule*words)
		readSet(&in, added, rule*words)
	}
	readSet(&in, owned, 0)

	fired := make([]bool, m)
	changed := true
	for changed {
		changed = false
		for rule := 0; rule < m; rule++ {
			if fired[rule] {
				continue
			}
			offset := rule * words
			ready := true
			for word := 0; word < words; word++ {
				if required[offset+word] & ^owned[word] != 0 {
					ready = false
					break
				}
			}
			if !ready {
				continue
			}
			fired[rule] = true
			for word := 0; word < words; word++ {
				merged := owned[word] | added[offset+word]
				changed = changed || merged != owned[word]
				owned[word] = merged
			}
		}
	}

	answer := make([]byte, n)
	for bit := range answer {
		answer[bit] = '0'
		if owned[bit/wordBits]>>uint(bit%wordBits)&1 != 0 {
			answer[bit] = '1'
		}
	}
	fmt.Println(string(answer))
}
