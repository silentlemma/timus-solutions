package main

import "io"

import (
	"bufio"

	"os"
	"sort"
	"strconv"
)

type person struct {
	city   int
	wealth int64
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() string { in.Scan(); return in.Text() }
	number := func() int { v, _ := strconv.Atoi(next()); return v }
	n := number()
	ids, people := map[string]int{}, map[string]person{}
	var names []string
	var totals []int64
	cityID := func(name string) int {
		if id, ok := ids[name]; ok {
			return id
		}
		id := len(names)
		ids[name] = id
		names = append(names, name)
		totals = append(totals, 0)
		return id
	}
	const wealthBits = 64
	for i := 0; i < n; i++ {
		who, city := next(), next()
		wealth, _ := strconv.ParseInt(next(), 10, wealthBits)
		id := cityID(city)
		people[who] = person{id, wealth}
		totals[id] += wealth
	}
	m, k := number(), number()
	// each move introduces at most one city; no move records need to be stored.
	size := 1
	for size < len(names)+k {
		size *= 2
	}
	// a max tree over cities: the best total and the one city that reaches it,
	// or minus one when several cities do
	best, where, days := make([]int64, 2*size), make([]int32, 2*size), make([]int32, size)
	for i := 0; i < size; i++ {
		where[size+i] = int32(i)
	}
	copy(best[size:], totals)
	pull := func(i int) {
		a, b := 2*i, 2*i+1
		// minus one denotes a tie, replacing a full multiplicity array.
		if best[a] == best[b] {
			best[i], where[i] = best[a], -1
		} else {
			w := a
			if best[b] > best[a] {
				w = b
			}
			best[i], where[i] = best[w], where[w]
		}
	}
	for i := size - 1; i > 0; i-- {
		pull(i)
	}
	add := func(city int, amount int64) {
		i := size + city
		best[i] += amount
		for i /= 2; i > 0; i /= 2 {
			value, winner := best[i], where[i]
			pull(i)
			// unchanged maxima and tie status cannot affect an ancestor.
			if value == best[i] && winner == where[i] {
				break
			}
		}
	}
	today := 1
	for i := 0; i < k; i++ {
		day, who, city := number(), next(), next()
		// a strict leader only; the moves of a day count from the next morning
		if where[1] >= 0 {
			days[where[1]] += int32(day + 1 - today)
		}
		today = day + 1
		p, to := people[who], cityID(city)
		if p.city != to {
			add(p.city, -p.wealth)
			add(to, p.wealth)
			people[who] = person{to, p.wealth}
		}
	}
	if where[1] >= 0 {
		days[where[1]] += int32(m + 1 - today)
	}
	sort.Strings(names)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, name := range names {
		if d := days[ids[name]]; d > 0 {
			fastPrint(out, true, true, name, int(d))
		}
	}
}

var fastOutputBuffer = make([]byte, 0, 64)

// Reuse one output buffer; io.Writer cannot retain it after Write returns.
func fastPrint(writer io.Writer, spaced, newline bool, values ...interface{}) (int, error) {
	buffer := fastOutputBuffer[:0]
	previousString := false
	for index, value := range values {
		_, isString := value.(string)
		if index > 0 && (spaced || (!previousString && !isString)) {
			buffer = append(buffer, ' ')
		}
		switch value := value.(type) {
		case string:
			buffer = append(buffer, value...)
		case int:
			buffer = strconv.AppendInt(buffer, int64(value), 10)

		default:
			panic("unsupported output type")
		}
		previousString = isString
	}
	if newline {
		buffer = append(buffer, '\n')
	}
	fastOutputBuffer = buffer
	return writer.Write(buffer)
}
