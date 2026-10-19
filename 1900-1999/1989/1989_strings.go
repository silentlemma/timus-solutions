package main

import (
	"bufio"
	"bytes"
	"io/ioutil"
	"os"
)

type reader struct {
	data     []byte
	position int
}

func (r *reader) token() []byte {
	for r.position < len(r.data) && r.data[r.position] <= ' ' {
		r.position++
	}
	begin := r.position
	for r.position < len(r.data) && r.data[r.position] > ' ' {
		r.position++
	}
	return r.data[begin:r.position]
}
func (r *reader) number() int {
	value := 0
	for _, digit := range r.token() {
		value = value*10 + int(digit-'0')
	}
	return value
}
func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	r := reader{data: data}
	word := append([]byte(nil), r.token()...)
	size := len(word)
	reverse := make([]byte, size)
	for i, value := range word {
		reverse[size-1-i] = value
	}
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	operations := r.number()
	for ; operations > 0; operations-- {
		operation := r.token()
		left := r.number() - 1
		if operation[0] == 'c' {
			value := r.token()[0]
			word[left] = value
			reverse[size-1-left] = value
		} else {
			end := r.number()
			half := (end - left) / 2
			if bytes.Equal(word[left:left+half], reverse[size-end:size-end+half]) {
				output.WriteString("Yes\n")
			} else {
				output.WriteString("No\n")
			}
		}
	}
}
