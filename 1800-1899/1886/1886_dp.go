package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

const percent = 100.0

type flight struct {
	a, b    int
	t, f, d int64
	p       float64
}

func main() {
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	scanner.Split(bufio.ScanWords)
	next := func() int64 {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return int64(v)
	}
	n, m := int(next()), int(next())
	flights := make([]flight, m)
	for i := range flights {
		a, b, t, f := next(), next(), next(), next()
		p, d := next(), next()
		flights[i] = flight{int(a), int(b), t, f, d, float64(p)}
	}
	// per airport, over the flights seen so far (latest first): departure
	// times, and the best expected arrival over the flights leaving at that
	// time or later
	departs := make([][]int64, n+1)
	best := make([][]float64, n+1)
	inf := math.Inf(1)
	// expected is the best expected arrival for someone at airport a at time
	expected := func(a int, time int64) float64 {
		if a == n {
			return float64(time)
		}
		late := departs[a]
		k := sort.Search(len(late), func(i int) bool { return late[i] < time })
		if k == 0 {
			return inf
		}
		return best[a][k-1]
	}
	// an arrival is always later than the departure, so taking flights from
	// the latest departure down sees every flight a connection could use
	sort.Slice(flights, func(i, j int) bool { return flights[i].t > flights[j].t })
	for _, x := range flights {
		onTime, delayed := expected(x.b, x.t+x.f), expected(x.b, x.t+x.f+x.d)
		value := ((percent-x.p)*onTime + x.p*delayed) / percent
		if len(best[x.a]) > 0 {
			value = math.Min(value, best[x.a][len(best[x.a])-1])
		}
		departs[x.a] = append(departs[x.a], x.t)
		best[x.a] = append(best[x.a], value)
	}
	answer := expected(1, 0)
	if math.IsInf(answer, 1) {
		fmt.Println("Fail")
	} else {
		fmt.Printf("%.6f\n", answer)
	}
}
