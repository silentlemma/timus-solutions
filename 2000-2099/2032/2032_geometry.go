package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"sort"
)

const firstOdd int64 = 3
const minHypotenuse int64 = 5

func smallRoot(value int64) int64 {
	low, high := int64(0), value+1
	for high-low > 1 {
		middle := (low + high) / 2
		if middle*middle <= value {
			low = middle
		} else {
			high = middle
		}
	}
	return low
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func divisors(number int64) []int64 {
	values := []int64{1}
	for prime := int64(2); prime*prime <= number; {
		previous, power := len(values), int64(1)
		for number%prime == 0 {
			number /= prime
			power *= prime
			for i := 0; i < previous; i++ {
				values = append(values, values[i]*power)
			}
		}
		if prime == 2 {
			prime = firstOdd
		} else {
			prime += 2
		}
	}
	if number > 1 {
		previous := len(values)
		for i := 0; i < previous; i++ {
			values = append(values, values[i]*number)
		}
	}
	return values
}

type Geometry struct{ dot, cross, denominator *big.Int }

func (geometry *Geometry) point(x, y int64) []int64 {
	u := new(big.Int).Sub(new(big.Int).Mul(geometry.dot, big.NewInt(x)),
		new(big.Int).Mul(geometry.cross, big.NewInt(y)))
	v := new(big.Int).Add(new(big.Int).Mul(geometry.dot, big.NewInt(y)),
		new(big.Int).Mul(geometry.cross, big.NewInt(x)))
	qx, rx, qy, ry := new(big.Int), new(big.Int), new(big.Int), new(big.Int)
	qx.QuoRem(u, geometry.denominator, rx)
	qy.QuoRem(v, geometry.denominator, ry)
	if rx.Sign() != 0 || ry.Sign() != 0 {
		return nil
	}
	return []int64{0, 0, x, y, qx.Int64(), qy.Int64()}
}

func solve(input []int64) []int64 {
	sides := append([]int64(nil), input...)
	sort.Slice(sides, func(i, j int) bool { return sides[i] < sides[j] })
	radius, length, opposite := sides[0], sides[1], sides[2]
	twiceDot := radius*radius + length*length - opposite*opposite
	if twiceDot%2 != 0 {
		return nil
	}
	dot := big.NewInt(twiceDot / 2)
	denominator := big.NewInt(radius * radius)
	square := new(big.Int).Sub(new(big.Int).Mul(denominator, big.NewInt(length*length)),
		new(big.Int).Mul(dot, dot))
	if square.Sign() < 0 {
		return nil
	}
	cross := new(big.Int).Sqrt(square)
	if new(big.Int).Mul(cross, cross).Cmp(square) != 0 {
		return nil
	}
	geometry := Geometry{dot, cross, denominator}
	if answer := geometry.point(radius, 0); answer != nil {
		return answer
	}
	if answer := geometry.point(0, radius); answer != nil {
		return answer
	}
	for _, hypotenuse := range divisors(radius) {
		if hypotenuse < minHypotenuse || hypotenuse%2 == 0 {
			continue
		}
		end := smallRoot(hypotenuse - 1)
		for m := smallRoot(hypotenuse/2) + 1; m <= end; m++ {
			rest := hypotenuse - m*m
			k := smallRoot(rest)
			if k*k != rest || gcd(m, k) != 1 || (m-k)%2 == 0 {
				continue
			}
			scale := radius / hypotenuse
			x, y := scale*(m*m-k*k), scale*2*m*k
			if answer := geometry.point(x, y); answer != nil {
				return answer
			}
			if answer := geometry.point(y, x); answer != nil {
				return answer
			}
		}
	}
	return nil
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var a, b, c int64
	if _, err := fmt.Fscan(input, &a, &b, &c); err != nil {
		return
	}
	answer := solve([]int64{a, b, c})
	if answer == nil {
		fmt.Println(-1)
	} else {
		for i := 0; i < len(answer); i += 2 {
			fmt.Println(answer[i], answer[i+1])
		}
	}
}
