package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var m, d1, d2 int
	if _, err := fmt.Scan(&m, &d1, &d2); err != nil {
		return
	}
	// the work is m * d1 digger-days; spreading it as evenly as possible
	// over d2 days needs the fewest diggers, the rounded-up average
	work := m * d1
	low, extra := work/d2, work%d2
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for day := 0; day < d2; day++ {
		if day > 0 {
			writer.WriteByte(' ')
		}
		count := low
		if day >= d2-extra {
			count++
		}
		writer.WriteString(strconv.Itoa(count))
	}
	writer.WriteByte('\n')
}
