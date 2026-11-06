package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

const (
	outputSize = 16
	decimal    = 10
)

func simple(ch byte) bool {
	return ch == ' ' || ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z'
}

func main() {
	input := bufio.NewReader(os.Stdin)
	header, _ := input.ReadString('\n')
	fields := strings.Fields(header)
	shortLimit, _ := strconv.Atoi(fields[0])
	longLimit, _ := strconv.Atoi(fields[1])
	length, messages := 0, 0
	plain := true
	for {
		ch, err := input.ReadByte()
		if err != nil || ch == '\n' || ch == '\r' {
			break
		}
		letter := simple(ch)
		if length == longLimit || length >= shortLimit && (!plain || !letter) {
			messages++
			length, plain = 0, true
		}
		length++
		plain = plain && letter
	}
	if length != 0 {
		messages++
	}
	var output [outputSize]byte
	line := strconv.AppendInt(output[:0], int64(messages), decimal)
	os.Stdout.Write(append(line, '\n'))
}
