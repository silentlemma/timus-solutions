package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const (
	idBits     = 10
	idMask     = 1<<idBits - 1
	fieldSize  = 16
	bufferSize = 4096
	decimal    = 10
)

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func latest(free []uint16, day uint16) uint16 {
	for free[day] != day {
		free[day] = free[free[day]]
		day = free[day]
	}
	return day
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	size := nextInt(input)
	orders := make([]int, size)
	for i := range orders {
		deadline, reward := nextInt(input), nextInt(input)
		if deadline > size {
			deadline = size
		}
		orders[i] = ((reward<<idBits | deadline) << idBits) | (i + 1)
	}
	sort.Ints(orders)
	free, assigned := make([]uint16, size+1), make([]uint16, size+1)
	for day := range free {
		free[day] = uint16(day)
	}
	count := 0
	for i := size - 1; i >= 0; i-- {
		order := orders[i]
		day := latest(free, uint16(order>>idBits&idMask))
		if day != 0 {
			assigned[day] = uint16(order & idMask)
			free[day] = latest(free, day-1)
			count++
		}
	}
	output := bufio.NewWriter(os.Stdout)
	var storage [fieldSize]byte
	line := strconv.AppendInt(storage[:0], int64(count), decimal)
	output.Write(append(line, '\n'))
	written := 0
	for _, order := range assigned {
		if order == 0 {
			continue
		}
		if written != 0 {
			output.WriteByte(' ')
		}
		written++
		output.Write(strconv.AppendUint(storage[:0], uint64(order), decimal))
	}
	output.WriteByte('\n')
	output.Flush()
}
