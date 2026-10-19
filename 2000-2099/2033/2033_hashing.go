package main

import (
	"bufio"
	"fmt"
	"os"
)

const recordCount = 6

type Record struct {
	model string
	price int
}
type Stats struct{ count, cheapest int }

func solve(records []Record) string {
	groups := make(map[string]Stats)
	for _, record := range records {
		stats := groups[record.model]
		if stats.count == 0 || record.price < stats.cheapest {
			stats.cheapest = record.price
		}
		stats.count++
		groups[record.model] = stats
	}
	answer, bestCount, bestPrice := "", -1, 0
	for model, stats := range groups {
		if stats.count > bestCount || stats.count == bestCount && stats.cheapest < bestPrice ||
			stats.count == bestCount && stats.cheapest == bestPrice && model < answer {
			answer, bestCount, bestPrice = model, stats.count, stats.cheapest
		}
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	records := make([]Record, recordCount)
	for i := range records {
		var name string
		if _, err := fmt.Fscan(input, &name, &records[i].model, &records[i].price); err != nil {
			return
		}
	}
	fmt.Println(solve(records))
}
