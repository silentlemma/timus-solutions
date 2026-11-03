package main

import (
	"bufio"
	"io/ioutil"
	"os"
)

const limit = 100000
const letters = "abc"
const period = len(letters)
const blockRepeats = 1024
const blockSize = period * blockRepeats
const bufferSize = 4096

func main() {
	input, _ := ioutil.ReadAll(os.Stdin)
	n := 0
	for _, ch := range input {
		if ch >= '0' && ch <= '9' {
			n = n*10 + int(ch-'0')
		}
	}
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer out.Flush()
	if n == 1 {
		for first := 0; first < period; first++ {
			out.WriteByte(letters[first])
			out.WriteByte('\n')
		}
		return
	}
	if period*(period-1)*n > limit {
		out.WriteString("TOO LONG\n")
		return
	}
	var block [blockSize]byte
	for first := 0; first < period; first++ {
		for second := 0; second < period; second++ {
			if first == second {
				continue
			}
			third := 0
			for third == first || third == second {
				third++
			}
			pattern := [period]byte{letters[first], letters[second], letters[third]}
			for i := range block {
				block[i] = pattern[i%period]
			}
			for left := n; left > 0; {
				take := left
				if take > blockSize {
					take = blockSize
				}
				out.Write(block[:take])
				left -= take
			}
			out.WriteByte('\n')
		}
	}
}
