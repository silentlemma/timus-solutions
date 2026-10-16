package main

import "fmt"

const r = 8.314

func main() {
	// lines "X = value"
	known := map[string]float64{}
	for {
		var name, eq string
		var value float64
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
		fmt.Printf("p = %.6f\n", n*r*t/v)
	case !hasN:
		fmt.Printf("n = %.6f\n", p*v/(r*t))
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
			fmt.Printf("V = %.6f\n", n*r*t/p)
		default:
			fmt.Printf("T = %.6f\n", p*v/(n*r))
		}
	}
}
