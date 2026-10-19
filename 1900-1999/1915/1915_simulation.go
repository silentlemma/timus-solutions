package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
)

const integerBuffer = 12

func poppedCoins(operations []int32) []int32 {
	remaining := 0
	for _, operation := range operations {
		if operation == -1 {
			remaining++
		}
	}
	if remaining == 0 {
		return nil
	}
	capacity := remaining
	coins := make([]int32, capacity)
	answer := make([]int32, 0, capacity)
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
			answer = append(answer, coins[(bottom+size)%capacity])
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
	return answer
}

type input struct {
	data []byte
	at   int
}

func (in *input) next() int32 {
	for in.data[in.at] <= ' ' {
		in.at++
	}
	sign := int32(1)
	if in.data[in.at] == '-' {
		sign = -1
		in.at++
	}
	value := int32(0)
	for in.at < len(in.data) && in.data[in.at] > ' ' {
		value = value*10 + int32(in.data[in.at]-'0')
		in.at++
	}
	return value * sign
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	count := int(in.next())
	operations := make([]int32, count)
	for index := range operations {
		operations[index] = in.next()
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	line := make([]byte, 0, integerBuffer)
	for _, coin := range poppedCoins(operations) {
		line = strconv.AppendInt(line[:0], int64(coin), 10)
		line = append(line, '\n')
		out.Write(line)
	}
}
