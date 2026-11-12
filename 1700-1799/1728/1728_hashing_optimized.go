package main

import "syscall"

const lyoshaName = "Efremov"
const vadikName = "Kantorov"
const fullTeam = 3

const inputSize = 512
const nameLimit = 50
const decimalBase = 10
const winPrefix = "Win\n"

var input [inputSize]byte
var position, available int

func readByte() byte {
	for position == available {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, available = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	c := input[position]
	position++
	return c
}

func firstByte() byte {
	c := readByte()
	for c != 0 && c <= ' ' {
		c = readByte()
	}
	return c
}

func number() int {
	value := 0
	for c := firstByte(); c >= '0' && c <= '9'; c = readByte() {
		value = value*decimalBase + int(c-'0')
	}
	return value
}

func next() string {
	var name [nameLimit]byte
	length := 0
	for c := firstByte(); c > ' '; c = readByte() {
		name[length] = c
		length++
	}
	return string(name[:length])
}

func writeOutput(output []byte) {
	for len(output) > 0 {
		count, err := syscall.Write(syscall.Stdout, output)
		if count > 0 {
			output = output[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return
		}
	}
}

func main() {
	n := number()
	full, pairs := map[string]bool{}, map[string]bool{}
	for i := 0; i < n; i++ {
		size := number()
		for j := 0; j < size; j++ {
			name := next()
			if name != lyoshaName && name != vadikName {
				if size == fullTeam {
					full[name] = true
				} else {
					pairs[name] = true
				}
			}
		}
	}
	lyosha, vadik, m := number(), number(), number()
	best, chosen := -1, ""
	for i := 0; i < m; i++ {
		name, rating := next(), number()
		strength := vadik + rating
		if !full[name] {
			strength += lyosha
		} else if pairs[name] {
			continue
		}
		if strength > best {
			best, chosen = strength, name
		}
	}
	var buffer [len(winPrefix) + nameLimit + 1]byte
	if best < 0 {
		writeOutput(buffer[:copy(buffer[:], "Fail\n")])
		return
	}
	length := copy(buffer[:], winPrefix)
	length += copy(buffer[length:], chosen)
	buffer[length] = '\n'
	writeOutput(buffer[:length+1])
}
