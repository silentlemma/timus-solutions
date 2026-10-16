package main

import "fmt"

const rNum, rDen, scale int64 = 8314, 1000, 1000000

func printValue(name string, numerator, denominator int64) {
	value := (numerator*scale + denominator/2) / denominator
	fmt.Printf("%s = %d.%06d\n", name, value/scale, value%scale)
}

func main() {
	// lines "X = value"
	known := map[string]int64{}
	for {
		var name, eq string
		var value int64
		if _, err := fmt.Scan(&name, &eq, &value); err != nil {
			break
		}
		known[name] = value
	}
	_, hasP := known["p"]
	_, hasN := known["n"]
	_, hasV := known["V"]
	p, n, v, t := known["p"], known["n"], known["V"], known["T"]
	// p V = n R T, with V and T strictly positive
	switch {
	case !hasP:
		printValue("p", n*rNum*t, rDen*v)
	case !hasN:
		printValue("n", p*v*rDen, rNum*t)
	default:
		// the unknown is V (beside p) or T (beside n R), and both must be
		// positive: a zero factor leaves 0 = 0 or a contradiction
		factor, other := n, p
		if !hasV {
			factor, other = p, n
		}
		switch {
		case factor == 0 && other == 0:
			fmt.Println("undefined")
		case factor == 0 || other == 0:
			fmt.Println("error")
		case !hasV:
			printValue("V", n*rNum*t, rDen*p)
		default:
			printValue("T", p*v*rDen, n*rNum)
		}
	}
}
