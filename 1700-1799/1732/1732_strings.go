package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// a line holds up to 100000 characters
const bufferSize = 1 << 17

func prefixFunction(t string) []int {
	p := make([]int, len(t))
	k := 0
	for i := 1; i < len(t); i++ {
		for k > 0 && t[i] != t[k] {
			k = p[k-1]
		}
		if t[i] == t[k] {
			k++
		}
		p[i] = k
	}
	return p
}

// the first occurrence of t in s[from:to], or -1
func find(s string, from, to int, t string, p []int) int {
	k := 0
	for i := from; i < to; i++ {
		for k > 0 && s[i] != t[k] {
			k = p[k-1]
		}
		if s[i] == t[k] {
			k++
			if k == len(t) {
				return i - k + 1
			}
		}
	}
	return -1
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	source, _ := in.ReadString('\n')
	line, _ := in.ReadString('\n')
	source = strings.TrimRight(source, "\r\n")
	target := strings.Split(strings.TrimRight(line, "\r\n"), " ")
	keep := make([]bool, len(source))
	j := 0
	p := prefixFunction(target[0])
	// each wanted word goes to its earliest place in the current word, at
	// least one erased letter after the previous one there; if it does not
	// fit, the next word of the source is tried
	for begin := 0; begin < len(source) && j < len(target); {
		end := strings.IndexByte(source[begin:], ' ')
		if end < 0 {
			end = len(source)
		} else {
			end += begin
		}
		for pos := begin; j < len(target) && end-pos >= len(target[j]); {
			at := find(source, pos, end, target[j], p)
			if at < 0 {
				break
			}
			for i := at; i < at+len(target[j]); i++ {
				keep[i] = true
			}
			pos = at + len(target[j]) + 1
			j++
			if j < len(target) {
				p = prefixFunction(target[j])
			}
		}
		begin = end + 1
	}
	if j < len(target) {
		fmt.Println("I HAVE FAILED!!!")
		return
	}
	out := []byte(source)
	for i := range out {
		if out[i] != ' ' && !keep[i] {
			out[i] = '_'
		}
	}
	fmt.Println(string(out))
}
