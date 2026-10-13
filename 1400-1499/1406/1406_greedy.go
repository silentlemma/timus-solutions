package main

import "fmt"

const digit = 9 // the largest digit

func main() {
	var line string
	fmt.Scan(&line)
	s := []byte(line)
	after := 0 // the sum of the digits after position i
	// the rightmost digit that can grow by one while the digits after it give
	// one back; the smallest such change gives the next number
	for i := len(s) - 1; i >= 0; i-- {
		d := int(s[i] - '0')
		if d < digit && after > 0 {
			s[i]++
			rest := after - 1
			// the smallest tail with this sum: the digits pushed to the right
			for j := len(s) - 1; j > i; j-- {
				put := rest
				if put > digit {
					put = digit
				}
				s[j] = byte('0' + put)
				rest -= put
			}
			fmt.Println(string(s))
			return
		}
		after += d
	}
	fmt.Println(-1)
}
