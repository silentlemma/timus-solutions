package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const outputCapacity = 24

const percentScale = 100

func plateaus(size, kept, percentage int, use func(int, int)) {
	start, end := 0, size-kept
	for weight := 1; start < size; weight++ {
		use(end-start, weight)
		start, end = end, percentScale*end/percentage+1
		if end > size {
			end = size
		}
	}
}

func main() {
	var size, kept, percentage int
	fmt.Fscan(os.Stdin, &size, &kept, &percentage)
	var total int64
	plateaus(size, kept, percentage, func(count, weight int) {
		total += int64(count) * int64(weight)
	})
	out := bufio.NewWriter(os.Stdout)
	var buffer [outputCapacity]byte
	out.Write(append(strconv.AppendInt(buffer[:0], total, 10), '\n'))
	separator := ""
	plateaus(size, kept, percentage, func(count, weight int) {
		digits := strconv.AppendInt(buffer[:0], int64(weight), 10)
		for i := 0; i < count; i++ {
			out.WriteString(separator)
			out.Write(digits)
			separator = " "
		}
	})
	out.WriteByte('\n')
	out.Flush()
}
