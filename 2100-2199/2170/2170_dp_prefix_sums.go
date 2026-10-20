package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

type inputReader struct {
	data  []byte
	index int
}

func (reader *inputReader) nextInt() int {
	for reader.index < len(reader.data) && reader.data[reader.index] <= ' ' {
		reader.index++
	}
	value := 0
	for reader.index < len(reader.data) && reader.data[reader.index] >= '0' {
		value = value*10 + int(reader.data[reader.index]-'0')
		reader.index++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	reader := inputReader{data: data}
	exponent := reader.nextInt()
	queryCount := reader.nextInt()
	count := 1 << uint(exponent)
	prefix := make([]int64, count+1)
	for index := 0; index < count; index++ {
		prefix[index+1] = prefix[index] + int64(reader.nextInt())
	}

	time := make([][]int64, exponent+1)
	time[0] = make([]int64, count)
	for power := 1; power <= exponent; power++ {
		half := 1 << uint(power-1)
		width := 2 * half
		starts := count - width + 1
		time[power] = make([]int64, starts)
		for left := 0; left < starts; left++ {
			difference := 2*prefix[left+half] - prefix[left] - prefix[left+width]
			if difference < 0 {
				difference = -difference
			}
			// The two halves finish independently before their final merge.
			previous := time[power-1][left]
			if time[power-1][left+half] > previous {
				previous = time[power-1][left+half]
			}
			time[power][left] = previous + difference
		}
	}

	output := make([]byte, 0)
	for query := 0; query < queryCount; query++ {
		left := reader.nextInt() - 1
		power := reader.nextInt()
		output = strconv.AppendInt(output, time[power][left], 10)
		output = append(output, '.', '0', '\n')
	}
	os.Stdout.Write(output)
}
