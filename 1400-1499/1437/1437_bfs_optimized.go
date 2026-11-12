package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

const (
	cans      = 3
	byteBits  = 8
	values    = 1 << byteBits
	faceSize  = values * values
	faceCount = 2 * cans
	wordBits  = 64
)

var capacity [cans]int
var seen [faceCount * faceSize / wordBits]uint64
var states [faceCount * faceSize]uint32
var volumes [cans*(values-1) + 1]bool

func mark(v [cans]int) bool {
	for i := 0; i < cans; i++ {
		if v[i] != 0 && v[i] != capacity[i] {
			continue
		}
		face := 2 * i
		if v[i] != 0 {
			face++
		}
		key := face*faceSize + v[(i+1)%cans]*values + v[(i+2)%cans]
		bit := uint64(1) << uint(key%wordBits)
		if seen[key/wordBits]&bit != 0 {
			return false
		}
		seen[key/wordBits] |= bit
		return true
	}
	return false
}

func main() {
	input, _ := ioutil.ReadAll(os.Stdin)
	at := 0
	for i := range capacity {
		for at < len(input) && input[at] <= ' ' {
			at++
		}
		for at < len(input) && input[at] >= '0' && input[at] <= '9' {
			capacity[i] = capacity[i]*10 + int(input[at]-'0')
			at++
		}
	}
	mark([cans]int{})
	tail, answer := 1, 0
	for head := 0; head < tail; head++ {
		code := states[head]
		v := [cans]int{
			int(code >> (2 * byteBits)),
			int(code >> byteBits & (values - 1)),
			int(code & (values - 1)),
		}
		for mask := 1; mask < 1<<cans; mask++ {
			sum := 0
			for i := 0; i < cans; i++ {
				if mask>>uint(i)&1 != 0 {
					sum += v[i]
				}
			}
			if sum > 0 && !volumes[sum] {
				volumes[sum] = true
				answer++
			}
		}
		for i := 0; i < cans; i++ {
			for j := -1; j < cans; j++ {
				if i == j {
					continue
				}
				w := v
				if j < 0 {
					w[i] = capacity[i]
				} else {
					poured := v[i]
					if capacity[j]-v[j] < poured {
						poured = capacity[j] - v[j]
					}
					w[i] -= poured
					w[j] += poured
				}
				if mark(w) {
					states[tail] = uint32(w[0])<<(2*byteBits) | uint32(w[1])<<byteBits | uint32(w[2])
					tail++
				}
			}
		}
	}
	output := strconv.AppendInt(nil, int64(answer), 10)
	os.Stdout.Write(append(output, '\n'))
}
