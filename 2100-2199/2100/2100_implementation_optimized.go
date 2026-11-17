package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	inputBufferSize = 256
	unlucky         = 13
	price           = 100
)

func readInt(in *bufio.Reader) int {
	c, err := in.ReadByte()
	for c <= ' ' && err == nil {
		c, err = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, inputBufferSize)
	n := readInt(in)
	people := n + 2
	for i := 0; i < n; i++ {
		c, _ := in.ReadByte()
		for c <= ' ' {
			c, _ = in.ReadByte()
		}
		for c > ' ' {
			if c == '+' {
				people++
			}
			c, _ = in.ReadByte()
		}
	}
	if people == unlucky {
		people++
	}
	os.Stdout.WriteString(strconv.Itoa(people*price) + "\n")
}
