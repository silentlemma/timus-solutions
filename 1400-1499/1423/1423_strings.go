package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
)

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	// characters from 33 to 255 may come, so split on bytes up to the space
	words := bytes.FieldsFunc(data, func(r rune) bool { return r <= ' ' })
	n, _ := strconv.Atoi(string(words[0]))
	s, t := words[1], words[2]
	// t is s turned left by k, that is right by n - k: find it in s + s with KMP
	fail := make([]int, n)
	for i, k := 1, 0; i < n; i++ {
		for k > 0 && t[i] != t[k] {
			k = fail[k-1]
		}
		if t[i] == t[k] {
			k++
		}
		fail[i] = k
	}
	for i, k := 0, 0; i+1 < 2*n; i++ {
		c := s[i%n]
		for k > 0 && c != t[k] {
			k = fail[k-1]
		}
		if c == t[k] {
			k++
		}
		if k == n {
			start := i - n + 1
			fmt.Println((n - start) % n)
			return
		}
	}
	fmt.Println(-1)
}
