package main

import (
	"io/ioutil"
	"os"
	"sort"
	"strconv"
)

const (
	maxDigit      int64 = 9
	centsPerUnit  int64 = 100
	totalBase     int64 = 1000000000
	totalDigits         = 9
	outputPerItem       = 24
)

type scanner struct {
	data []byte
	pos  int
}

func (s *scanner) next() int64 {
	for s.pos < len(s.data) && s.data[s.pos] <= ' ' {
		s.pos++
	}
	var value int64
	for s.pos < len(s.data) && s.data[s.pos] > ' ' {
		value = value*10 + int64(s.data[s.pos]-'0')
		s.pos++
	}
	return value
}

func excess(value, limit int64) int64 {
	if value > limit {
		return value - limit
	}
	return 0
}

func largestChange(value int64) int64 {
	place := int64(1)
	for value/place >= 10 {
		place *= 10
	}
	for place > 0 {
		digit := value / place % 10
		if digit < maxDigit {
			return value + (maxDigit-digit)*place
		}
		place /= 10
	}
	return value
}

type change struct {
	index  int
	value  int64
	whole  int64
	cents  int64
	weight bool
}

type changes []change

func (items changes) Len() int { return len(items) }

func (items changes) Swap(i, j int) { items[i], items[j] = items[j], items[i] }

func (items changes) Less(i, j int) bool {
	if items[i].whole != items[j].whole {
		return items[i].whole > items[j].whole
	}
	if items[i].cents != items[j].cents {
		return items[i].cents > items[j].cents
	}
	return items[i].index < items[j].index
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := scanner{data: data}
	n, k := int(input.next()), int(input.next())
	maxWeight, maxPrice := input.next(), input.next()
	weightRate, priceRate := input.next(), input.next()
	weights, prices := make([]int64, n), make([]int64, n)
	items := make(changes, n)
	for i := 0; i < n; i++ {
		weight, price := input.next(), input.next()
		weights[i], prices[i] = weight, price
		newWeight, newPrice := largestChange(weight), largestChange(price)
		weightGain := (excess(newWeight, maxWeight) - excess(weight, maxWeight)) * weightRate
		priceGain := (excess(newPrice, maxPrice) - excess(price, maxPrice)) * priceRate
		whole, cents := priceGain/centsPerUnit, priceGain%centsPerUnit
		if weightGain > whole || weightGain == whole && cents == 0 {
			items[i] = change{i, newWeight, weightGain, 0, true}
		} else {
			items[i] = change{i, newPrice, whole, cents, false}
		}
	}
	if k > 0 {
		sort.Sort(items)
		for i := 0; i < k; i++ {
			item := items[i]
			if item.whole == 0 && item.cents == 0 {
				break
			}
			if item.weight {
				weights[item.index] = item.value
			} else {
				prices[item.index] = item.value
			}
		}
	}
	// Split the total because the sum of weight charges can exceed int64.
	var totalHigh, totalLow, priceCents int64
	for i := 0; i < n; i++ {
		fee := excess(weights[i], maxWeight) * weightRate
		totalHigh += fee / totalBase
		totalLow += fee % totalBase
		priceCents += excess(prices[i], maxPrice) * priceRate
	}
	totalLow += priceCents / centsPerUnit
	totalHigh += totalLow / totalBase
	totalLow %= totalBase
	output := make([]byte, 0, n*outputPerItem)
	if totalHigh > 0 {
		output = strconv.AppendInt(output, totalHigh, 10)
		lowText := strconv.FormatInt(totalLow, 10)
		for i := len(lowText); i < totalDigits; i++ {
			output = append(output, '0')
		}
		output = append(output, lowText...)
	} else {
		output = strconv.AppendInt(output, totalLow, 10)
	}
	output = append(output, '.')
	fraction := priceCents % centsPerUnit
	if fraction < 10 {
		output = append(output, '0')
	}
	output = strconv.AppendInt(output, fraction, 10)
	output = append(output, '\n')
	for i := 0; i < n; i++ {
		output = strconv.AppendInt(output, weights[i], 10)
		output = append(output, ' ')
		output = strconv.AppendInt(output, prices[i], 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
