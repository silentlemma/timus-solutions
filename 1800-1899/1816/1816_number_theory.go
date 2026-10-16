package main

import "fmt"

type part struct {
	offset int
	chance float64
}

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	var primes []int64
	var exps []int
	rest := n
	for p := int64(2); p*p <= rest; p++ {
		if rest%p != 0 {
			continue
		}
		primes = append(primes, p)
		exps = append(exps, 0)
		for rest%p == 0 {
			rest /= p
			exps[len(exps)-1]++
		}
	}
	if rest > 1 {
		primes = append(primes, rest)
		exps = append(exps, 1)
	}
	// a divisor is its exponent vector, numbered in mixed radix: every
	// proper divisor of a divisor gets a smaller number
	radix := []int{1}
	for _, e := range exps {
		radix = append(radix, radix[len(radix)-1]*(e+1))
	}
	count := radix[len(radix)-1]
	expected := make([]float64, count)
	for index := 0; index < count; index++ {
		total := 0
		parts := []part{{0, 1}}
		for i, q := range primes {
			top := index / radix[i] % (exps[i] + 1)
			total += top
			// gcd(m, r) for a uniform r splits over the primes: the
			// exponent of p in it is b < top with chance (1 - 1/p) / p^b,
			// or top with chance 1/p^top
			var next []part
			for _, pt := range parts {
				scale := 1.0
				for b := 0; b <= top; b++ {
					factor := 1 / scale
					if b < top {
						factor *= 1 - 1/float64(q)
					}
					next = append(next, part{pt.offset + b*radix[i], pt.chance * factor})
					scale *= float64(q)
				}
			}
			parts = next
		}
		if total <= 1 {
			continue // 1 or a prime: no gcd is taken
		}
		stay := parts[0].chance + parts[len(parts)-1].chance
		sum := 1.0
		for _, pt := range parts[1 : len(parts)-1] {
			sum += pt.chance * (expected[pt.offset] + expected[index-pt.offset])
		}
		expected[index] = sum / (1 - stay)
	}
	fmt.Printf("%.10f\n", expected[count-1])
}
