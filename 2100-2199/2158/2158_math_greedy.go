package main

import (
	"io/ioutil"
	"os"
	"sort"
	"strconv"
)

const (
	maxGeometric = 30
	seedLimit    = maxGeometric + 2
	majoritySize = 2 * (2*maxGeometric + 1)
)

type answer struct {
	arithmetic []int64
	geometric  []int64
}

func isArithmetic(values []int64) bool {
	for i := 2; i < len(values); i++ {
		if values[i]-values[i-1] != values[1]-values[0] {
			return false
		}
	}
	return true
}

func isGeometric(values []int64) bool {
	if len(values) == 0 {
		return false
	}
	if values[0] == 0 {
		return values[len(values)-1] == 0
	}
	for i := 2; i < len(values); i++ {
		if values[i]*values[0] != values[i-1]*values[1] {
			return false
		}
	}
	return true
}

func insert(values []int64, value int64) []int64 {
	index := sort.Search(len(values), func(i int) bool { return values[i] > value })
	values = append(values, 0)
	copy(values[index+1:], values[index:])
	values[index] = value
	return values
}

func extract(values []int64, start, step int64) answer {
	arithmetic := make([]int64, 0, len(values))
	geometric := make([]int64, 0, maxGeometric+2)
	expected := start
	for _, value := range values {
		if value == expected {
			arithmetic = append(arithmetic, value)
			expected += step
		} else {
			geometric = append(geometric, value)
			if len(geometric) > maxGeometric {
				return answer{}
			}
		}
	}
	// Three distinct geometric terms cannot form an arithmetic progression.
	for removed := 0; removed <= 2; removed++ {
		if len(arithmetic) != 0 && isGeometric(geometric) {
			return answer{arithmetic, geometric}
		}
		if removed == 2 || len(arithmetic) <= 1 {
			break
		}
		value := arithmetic[len(arithmetic)-1]
		arithmetic = arithmetic[:len(arithmetic)-1]
		geometric = insert(geometric, value)
	}
	return answer{}
}

func solve(values []int64) answer {
	sort.Slice(values, func(i, j int) bool { return values[i] < values[j] })
	distinct := make([]int64, 0)
	repeated := make([]int64, 0)
	for i, value := range values {
		if i == 0 || value != values[i-1] {
			distinct = append(distinct, value)
		} else if i == 1 || value != values[i-2] {
			repeated = append(repeated, value)
		}
	}
	if len(distinct) == 1 {
		return answer{values[:1], values[1:]}
	}
	if len(distinct) == 2 {
		cut := sort.Search(len(values), func(i int) bool { return values[i] > values[0] })
		return answer{values[:cut], values[cut:]}
	}
	if len(repeated) == 1 {
		constant := repeated[0]
		copies := 0
		other := make([]int64, 0)
		for _, value := range values {
			if value == constant {
				copies++
			} else {
				other = append(other, value)
			}
		}
		for moved := 0; moved < 2; moved++ {
			rest := append([]int64(nil), other...)
			if moved != 0 {
				rest = insert(rest, constant)
			}
			equal := make([]int64, copies-moved)
			for i := range equal {
				equal[i] = constant
			}
			if isGeometric(rest) {
				return answer{equal, rest}
			}
			if isArithmetic(rest) {
				return answer{rest, equal}
			}
		}
	}
	if len(values) <= maxGeometric+1 {
		for i, value := range values {
			rest := make([]int64, 0, len(values)-1)
			rest = append(rest, values[:i]...)
			rest = append(rest, values[i+1:]...)
			if isGeometric(rest) {
				return answer{[]int64{value}, rest}
			}
		}
	}
	if len(values) >= majoritySize {
		gaps := make([]int64, 0, len(values)-1)
		for i := 1; i < len(values); i++ {
			gaps = append(gaps, values[i]-values[i-1])
		}
		sort.Slice(gaps, func(i, j int) bool { return gaps[i] < gaps[j] })
		step := gaps[len(gaps)/2]
		if step != 0 {
			for _, start := range values[:maxGeometric+1] {
				result := extract(values, start, step)
				if result.arithmetic != nil {
					return result
				}
			}
		}
	} else {
		limit := len(values)
		if limit > seedLimit {
			limit = seedLimit
		}
		for i := 0; i < limit; i++ {
			for j := i + 1; j < limit; j++ {
				step := values[j] - values[i]
				if step != 0 {
					result := extract(values, values[i], step)
					if result.arithmetic != nil {
						return result
					}
				}
			}
		}
	}
	return answer{}
}

func appendSequence(output []byte, values []int64) []byte {
	for i, value := range values {
		if i != 0 {
			output = append(output, ' ')
		}
		output = strconv.AppendInt(output, value, 10)
	}
	return append(output, '\n')
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	next := func() int64 {
		for position < len(data) && data[position] <= ' ' {
			position++
		}
		value := int64(0)
		for position < len(data) && data[position] >= '0' && data[position] <= '9' {
			value = value*10 + int64(data[position]-'0')
			position++
		}
		return value
	}
	size := int(next())
	values := make([]int64, size)
	for i := range values {
		values[i] = next()
	}
	result := solve(values)
	if result.arithmetic == nil {
		os.Stdout.Write([]byte("-1\n"))
		return
	}
	output := strconv.AppendInt(nil, int64(len(result.arithmetic)), 10)
	output = append(output, '\n')
	output = appendSequence(output, result.arithmetic)
	output = appendSequence(output, result.geometric)
	os.Stdout.Write(output)
}
