package main

import (
	"bufio"
	"os"
	"strconv"
)

const integerBuffer = 12

func poppedCoins(operations []int32, out *bufio.Writer) {
	remaining := 0
	for _, operation := range operations {
		if operation == -1 {
			remaining++
		}
	}
	if remaining == 0 {
		return
	}
	capacity := remaining
	coins := make([]int32, capacity)
	line := make([]byte, 0, integerBuffer)
	bottom, size := 0, 0
	for _, operation := range operations {
		if remaining == 0 {
			break
		}
		if operation > 0 {
			if size == remaining {
				bottom = (bottom + 1) % capacity
				size--
			}
			coins[(bottom+size)%capacity] = operation
			size++
		} else if operation == -1 {
			remaining--
			size--
			line = strconv.AppendInt(line[:0], int64(coins[(bottom+size)%capacity]), 10)
			line = append(line, '\n')
			out.Write(line)
		} else {
			extra := size
			if remaining-size < extra {
				extra = remaining - size
			}
			newBottom := (bottom + capacity - extra) % capacity
			source, destination := (bottom+size-extra)%capacity, newBottom
			for index := 0; index < extra; index++ {
				coins[destination] = coins[source]
				source++
				destination++
				if source == capacity {
					source = 0
				}
				if destination == capacity {
					destination = 0
				}
			}
			bottom = newBottom
			size += extra
		}
	}
}

var reader = bufio.NewReader(os.Stdin)

func next() int32 {
	c, err := reader.ReadByte()
	for err == nil && c <= ' ' {
		c, err = reader.ReadByte()
	}
	sign := int32(1)
	if c == '-' {
		sign = -1
		c, err = reader.ReadByte()
	}
	value := int32(0)
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int32(c-'0')
		c, err = reader.ReadByte()
	}
	return value * sign
}

func main() {
	count := int(next())
	operations := make([]int32, count)
	for i := range operations {
		operations[i] = next()
	}
	out := bufio.NewWriter(os.Stdout)
	poppedCoins(operations, out)
	out.Flush()
}
