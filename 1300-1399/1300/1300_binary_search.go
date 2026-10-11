package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	cents  = 100
	digits = 2
	bits   = 64
)

var (
	limits, rates      []int64
	topRate, bonusRate int64
)

// toCents reads a non-negative amount with at most two decimals
func toCents(token string) int64 {
	whole, frac := token, ""
	if dot := strings.IndexByte(token, '.'); dot >= 0 {
		whole, frac = token[:dot], token[dot+1:]
	}
	frac = (frac + "00")[:digits]
	w, _ := strconv.ParseInt("0"+whole, 10, bits)
	f, _ := strconv.ParseInt(frac, 10, bits)
	return w*cents + f
}

// percent is rate percent of an amount in cents, rounded half up
func percent(amount, rate int64) int64 {
	return (amount*rate + cents/2) / cents
}

func tax(amount int64) int64 {
	var raw, previous int64
	for i, limit := range limits {
		if amount <= limit {
			return (raw + (amount-previous)*rates[i] + cents/2) / cents
		}
		raw += (limit - previous) * rates[i]
		previous = limit
	}
	return (raw + (amount-previous)*topRate + cents/2) / cents
}

func net(gross int64) int64 {
	bonus := percent(gross, bonusRate)
	return gross - tax(gross) + bonus - tax(bonus)
}

// grossFor bisects for the largest salary whose net does not exceed the
// amount paid; net never decreases as the salary grows
func grossFor(amount int64) int64 {
	lo, hi := int64(0), int64(1)
	for net(hi) <= amount {
		hi *= 2
	}
	for hi-lo > 1 {
		mid := (lo + hi) / 2
		if net(mid) <= amount {
			lo = mid
		} else {
			hi = mid
		}
	}
	return lo
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() string {
		in.Scan()
		return in.Text()
	}
	bonusRate, _ = strconv.ParseInt(next(), 10, bits)
	for {
		limit := toCents(next())
		rate, _ := strconv.ParseInt(next(), 10, bits)
		if limit == 0 {
			topRate = rate
			break
		}
		limits = append(limits, limit)
		rates = append(rates, rate)
	}
	var total, withheld int64
	for token := next(); token != "-1" && token != ""; token = next() {
		gross := grossFor(toCents(token))
		total += gross
		withheld += tax(gross) + tax(percent(gross, bonusRate))
	}
	owed := tax(total) + tax(percent(total, bonusRate)) - withheld
	sign := ""
	if owed < 0 {
		sign, owed = "-", -owed
	}
	fmt.Printf("%s%d.%02d\n", sign, owed/cents, owed%cents)
}
