package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	scale    = 100000
	digits   = 10
	angleEps = 1e-12
	gridEps  = 1e-7
	halfTurn = 180
)

type gun struct {
	angle float64
	x, y  int64
}

func product(values ...int64) *big.Int {
	result := big.NewInt(1)
	for _, value := range values {
		result.Mul(result, big.NewInt(value))
	}
	return result
}

func fits(left, right gun, distance, cosine int64) bool {
	cross := left.x*right.y - left.y*right.x
	dot := left.x*right.x + left.y*right.y
	if cross < 0 {
		return false
	}
	if cross == 0 {
		return dot > 0
	}
	if dot >= 0 && cosine < 0 {
		return true
	}
	if cosine >= 0 && dot < 0 {
		return false
	}
	lhs := product(dot, dot, distance, distance)
	rhs := product(cosine, cosine, left.x*left.x+left.y*left.y,
		right.x*right.x+right.y*right.y)
	comparison := lhs.Cmp(rhs)
	if dot >= 0 {
		return comparison >= 0
	}
	return comparison <= 0
}

func power(base, exponent int) *big.Int {
	return new(big.Int).Exp(big.NewInt(int64(base)), big.NewInt(int64(exponent)), nil)
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var n, shots, queries int
	fmt.Fscan(input, &n, &shots, &queries)
	guns := make([]gun, n)
	for i := range guns {
		fmt.Fscan(input, &guns[i].x, &guns[i].y)
		guns[i].angle = math.Atan2(float64(guns[i].y), float64(guns[i].x))
	}
	var a, b, radius int64
	fmt.Fscan(input, &a, &b, &radius)
	distance := a*a + b*b
	radiusSquared := radius * radius
	cosine := distance - 2*radiusSquared
	halfWidth := math.Atan2(float64(radius), math.Sqrt(float64(distance-radiusSquared)))
	width := 2 * halfWidth
	fullTurn := 2 * math.Pi
	lower := math.Atan2(float64(b), float64(a)) - halfWidth
	sort.Slice(guns, func(i, j int) bool {
		if guns[i].angle != guns[j].angle {
			return guns[i].angle < guns[j].angle
		}
		return guns[i].x*guns[j].y-guns[i].y*guns[j].x > 0
	})
	initial := 0
	for _, current := range guns {
		cross := a*current.y - b*current.x
		if a*current.x+b*current.y >= 0 &&
			product(cross, cross).Cmp(product(radiusSquared,
				current.x*current.x+current.y*current.y)) <= 0 {
			initial++
		}
	}
	best := make([]float64, n+1)
	for i := range best {
		best[i] = math.Inf(1)
	}
	best[0], best[initial] = 0, 0
	end := 0
	for begin, current := range guns {
		if end < begin {
			end = begin
		}
		for end < begin+n {
			other := guns[end%n]
			delta := other.angle - current.angle
			if end >= n {
				delta += fullTurn
			}
			inside := delta < width
			if math.Abs(delta-width) <= angleEps {
				inside = fits(current, other, distance, cosine)
			}
			if !inside {
				break
			}
			end++
		}
		angle := math.Mod(lower-current.angle, fullTurn)
		if angle < 0 {
			angle += fullTurn
		}
		if angle <= angleEps || fullTurn-angle <= angleEps {
			// The exact side of the tangent distinguishes zero from a full turn.
			cross := a*current.y - b*current.x
			strict := product(cross, cross).Cmp(product(radiusSquared,
				current.x*current.x+current.y*current.y)) < 0
			angle = 0
			if strict {
				angle = fullTurn - angleEps
			}
		}
		if angle < best[end-begin] {
			best[end-begin] = angle
		}
	}
	for count := n - 1; count >= 0; count-- {
		best[count] = math.Min(best[count], best[count+1])
	}
	levels := make([]int, n+1)
	denominator := power(n, shots)
	for count := 1; count < n; count++ {
		if shots == 1 {
			levels[count] = int(int64(scale) * int64(count) / int64(n))
			continue
		}
		remaining := n - count
		value := scale * (1 - math.Pow(float64(remaining)/float64(n), float64(shots)))
		nearest := int(value + 1.0/2)
		level := int(value)
		if math.Abs(value-float64(nearest)) < gridEps {
			lhs := new(big.Int).Mul(big.NewInt(scale), power(remaining, shots))
			rhs := new(big.Int).Mul(big.NewInt(int64(scale-nearest)), denominator)
			level = nearest
			if lhs.Cmp(rhs) > 0 {
				level--
			}
		}
		if level >= scale {
			level = scale - 1
		}
		levels[count] = level
	}
	levels[n] = scale
	answers := make(map[int]string)
	for query := 0; query < queries; query++ {
		var word string
		fmt.Fscan(input, &word)
		parts := strings.Split(word, ".")
		integer, _ := strconv.Atoi(parts[0])
		probability := integer * scale
		if len(parts) > 1 {
			place := scale
			for _, digit := range parts[1] {
				place /= 10
				probability += int(digit-'0') * place
			}
		}
		count := sort.SearchInts(levels, probability)
		answer, found := answers[count]
		if !found {
			answer = "-1"
			if !math.IsInf(best[count], 1) {
				answer = fmt.Sprintf("%.*f", digits, best[count]*halfTurn/math.Pi)
			}
			answers[count] = answer
		}
		fmt.Fprintln(output, answer)
	}
}
