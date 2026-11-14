package main

import (
	"bufio"
	"math/bits"
	"os"
	"sort"
	"strconv"
)

const (
	limbLimit      = 1000000
	binaryBits     = 60
	binaryBase     = uint64(1) << binaryBits
	outputDigits   = 6
	octalDigitBits = 3
)

func binaryCosts(radix int, costs []int) {
	digitBits := bits.TrailingZeros(uint(radix))
	var mask uint64
	for i := 0; i < binaryBits; i += digitBits {
		mask |= uint64(1) << uint(i)
	}
	a, b := []uint64{1}, []uint64{1}
	for i := 2; i < len(costs); i++ {
		if len(a) < len(b) {
			a = append(a, 0)
		}
		var carry uint64
		sum := 0
		for j, other := range b {
			value := a[j] + other + carry
			carry = value >> binaryBits
			value &= binaryBase - 1
			a[j] = value
			sum += bits.OnesCount64(value & mask)
			if digitBits >= 2 {
				sum += 2 * bits.OnesCount64((value>>1)&mask)
			}
			if digitBits == octalDigitBits {
				sum += (1 << 2) * bits.OnesCount64((value>>2)&mask)
			}
		}
		if carry != 0 {
			a = append(a, 1)
		}
		costs[i] = sum + int(carry)
		a, b = b, a
	}
}

func tableCosts(radix int, costs []int) {
	base := 1
	for base <= limbLimit/radix {
		base *= radix
	}
	// Even twenty digits of value nine fit in a single byte.
	sums := make([]uint8, base)
	for i := 1; i < base; i++ {
		sums[i] = sums[i/radix] + uint8(i%radix)
	}
	a, b := []int{1}, []int{1}
	for i := 2; i < len(costs); i++ {
		if len(a) < len(b) {
			a = append(a, 0)
		}
		sum, carry := 0, 0
		for j, other := range b {
			value := a[j] + other + carry
			carry = 0
			if value >= base {
				value -= base
				carry = 1
			}
			a[j] = value
			sum += int(sums[value])
		}
		if carry != 0 {
			a = append(a, 1)
		}
		costs[i] = sum + carry
		a, b = b, a
	}
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	input.Scan()
	radix, _ := strconv.Atoi(input.Text())
	input.Scan()
	count, _ := strconv.Atoi(input.Text())
	costs := make([]int, count)
	costs[0], costs[1] = 1, 1
	if radix&(radix-1) == 0 {
		binaryCosts(radix, costs)
	} else {
		tableCosts(radix, costs)
	}
	// One integer stores the cost as the primary key and the index as the tie breaker.
	for i, cost := range costs {
		costs[i] = cost*count + i
	}
	sort.Ints(costs)
	out := bufio.NewWriter(os.Stdout)
	var digits [outputDigits]byte
	for i, key := range costs {
		if i != 0 {
			out.WriteByte(' ')
		}
		out.Write(strconv.AppendInt(digits[:0], int64(key%count+1), 10))
	}
	out.WriteByte('\n')
	out.Flush()
}
