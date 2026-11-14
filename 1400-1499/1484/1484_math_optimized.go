package main

import "syscall"

const decimal = 10
const scale = 2 * decimal
const inputSize = 64
const outputSize = 16
const fields = 3

func readValues() (values [fields]int, ok bool) {
	var input [inputSize]byte
	field, value := 0, 0
	started := false
	for {
		size, err := syscall.Read(syscall.Stdin, input[:])
		if err == syscall.EINTR {
			continue
		}
		if err != nil {
			return values, false
		}
		data := input[:size]
		if size == 0 {
			data = []byte(" ")
		}
		for _, ch := range data {
			switch {
			case ch >= '0' && ch <= '9':
				value = decimal*value + int(ch-'0')
				started = true
			case ch <= ' ' && started:
				values[field] = value
				field++
				if field == len(values) {
					return values, true
				}
				value, started = 0, false
			}
		}
		if size == 0 {
			return values, false
		}
	}
}

func write(data []byte) {
	for len(data) > 0 {
		size, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return
		}
		data = data[size:]
	}
}

func main() {
	values, ok := readValues()
	if !ok {
		return
	}
	current, target, count := values[0], values[1], values[2]

	total := ((2*current+1)*count - 1) / scale
	if total > decimal*count {
		total = decimal * count
	}
	if total < count || scale*total < (2*current-1)*count {
		write([]byte("Impossible\n"))
		return
	}

	bound := 2*target + 1
	excess := scale*total - bound*count
	result := 0
	if excess >= 0 {
		result = excess/(bound-scale) + 1
	}
	var output [outputSize]byte
	pos := len(output) - 1
	output[pos] = '\n'
	for {
		pos--
		output[pos] = byte(result%decimal) + '0'
		result /= decimal
		if result == 0 {
			break
		}
	}
	write(output[pos:])
}
