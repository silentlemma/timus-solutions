package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
)

const nine = 9
const base = 10
const bits = 64

func main() {
	// the whole input at once: 200 000 numbers are slow to read token by token
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	pos := 0
	next := func() string {
		for pos < len(data) && (data[pos] < '0' || data[pos] > '9') {
			pos++
		}
		start := pos
		for pos < len(data) && data[pos] >= '0' && data[pos] <= '9' {
			pos++
		}
		return string(data[start:pos])
	}
	n, _ := strconv.Atoi(next())
	records := make([]string, n)
	var total int64
	for i := range records {
		records[i] = next()
		v, _ := strconv.ParseInt(records[i], base, bits)
		total += v
	}
	report, _ := strconv.ParseInt(next(), base, bits)
	diff := report - total
	if diff == 0 {
		fmt.Println("Input has no error.")
		return
	}
	// swapping digits a (at 10^(i+1)) and b (at 10^i) adds 9 * (b - a) * 10^i
	if diff%nine == 0 {
		step, place := diff/nine, 0
		for step%base == 0 {
			step /= base
			place++
		}
		if step > -base && step < base {
			for number, digits := range records {
				hi := len(digits) - 2 - place // index of the digit at 10^(i+1)
				if hi < 0 || int64(digits[hi+1])-int64(digits[hi]) != step {
					continue
				}
				if hi == 0 && digits[1] == '0' {
					continue // the swap would make a leading zero
				}
				b := []byte(digits)
				b[hi], b[hi+1] = b[hi+1], b[hi]
				fmt.Printf("Error in record #%d. Correct number is: %s.\n", number+1, b)
				return
			}
		}
	}
	fmt.Println("Unrecoverable error.")
}
