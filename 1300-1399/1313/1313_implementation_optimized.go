package main

import (
	"bytes"
	"io/ioutil"
	"os"
	"strconv"
)

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	words := bytes.Fields(data)
	n, _ := strconv.Atoi(string(words[0]))
	values := words[1:]
	// diagonal s holds the cells with row + column = s; each is read from
	// its lowest row up
	out := make([]byte, 0, len(data))
	for sum := 0; sum < 2*n-1; sum++ {
		low, high := sum-n+1, sum
		if low < 0 {
			low = 0
		}
		if high > n-1 {
			high = n - 1
		}
		for row := high; row >= low; row-- {
			out = append(out, values[row*n+sum-row]...)
			out = append(out, ' ')
		}
	}
	out[len(out)-1] = '\n'
	os.Stdout.Write(out)
}
