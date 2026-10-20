package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

const maxAnswer int64 = 1000000000000

type input struct {
	data []byte
	pos  int
}

func (in *input) nextInt() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	var value int64
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int64(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n := int(in.nextInt())
	negative := make([]int64, 0, n)
	answer := int64(1)
	possible := true
	output := make([]byte, 0)
	for i := 0; i < n; i++ {
		divisor := in.nextInt()
		affirmative := in.nextInt()
		if possible {
			if affirmative == 0 {
				if answer%divisor == 0 {
					possible = false
				} else {
					negative = append(negative, divisor)
				}
			} else {
				factor := divisor / gcd(answer, divisor)
				if answer > maxAnswer/factor {
					possible = false
				} else if factor != 1 {
					answer *= factor
					// Every change at least doubles the least common multiple.
					for _, forbidden := range negative {
						if answer%forbidden == 0 {
							possible = false
							break
						}
					}
				}
			}
		}
		if possible {
			output = strconv.AppendInt(output, answer, 10)
		} else {
			output = append(output, '-', '1')
		}
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
