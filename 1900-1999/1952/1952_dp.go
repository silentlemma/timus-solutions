package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
	"math/bits"
	"os"
	"sort"
)

const (
	stormName            = "Storm"
	breathName           = "Breath"
	tailName             = "Tail"
	initialRootDigits    = 16
	boundRootDigits      = 32
	missingParent        = 255
	maskKeyBits          = 16
	intervalProductCount = 4
)

type point struct{ x, y int64 }
type aura struct{ cap, rise, fall int64 }
type spell struct {
	kind            string
	power, duration int64
	places          []point
}
type interval struct{ low, high float64 }

func down(x float64) float64         { return math.Nextafter(x, math.Inf(-1)) }
func up(x float64) float64           { return math.Nextafter(x, math.Inf(1)) }
func exactInterval(x int64) interval { return interval{float64(x), float64(x)} }
func addInterval(a, b interval) interval {
	return interval{down(a.low + b.low), up(a.high + b.high)}
}
func subInterval(a, b interval) interval {
	return interval{down(a.low - b.high), up(a.high - b.low)}
}
func mulInterval(a, b interval) interval {
	values := [intervalProductCount]float64{
		a.low * b.low, a.low * b.high, a.high * b.low, a.high * b.high,
	}
	low, high := values[0], values[0]
	for _, value := range values[1:] {
		low = math.Min(low, value)
		high = math.Max(high, value)
	}
	return interval{down(low), up(high)}
}
func divInterval(a interval, b int64) interval {
	return interval{down(a.low / float64(b)), up(a.high / float64(b))}
}
func minInterval(a, b interval) interval {
	return interval{math.Min(a.low, b.low), math.Min(a.high, b.high)}
}
func maxInterval(a, b interval) interval {
	return interval{math.Max(a.low, b.low), math.Max(a.high, b.high)}
}
func positiveInterval(a interval) interval { return maxInterval(interval{}, a) }
func squaredDistance(a, b point) int64     { x, y := a.x-b.x, a.y-b.y; return x*x + y*y }
func travel(a, b point, speed int64) float64 {
	return math.Sqrt(float64(squaredDistance(a, b))) / float64(speed)
}
func travelInterval(a, b point, speed int64) interval {
	squared := squaredDistance(a, b)
	if squared == 0 {
		return interval{}
	}
	value := travel(a, b, speed)
	low, high := down(value), up(value)
	target := big.NewRat(squared, 1)
	check := func(x float64) int {
		r := new(big.Rat).SetFloat64(x)
		r.Mul(r, r)
		r.Mul(r, big.NewRat(speed*speed, 1))
		return r.Cmp(target)
	}
	for check(low) > 0 {
		low = down(low)
	}
	for check(high) < 0 {
		high = up(high)
	}
	return interval{low, high}
}

type auraValue struct{ power, damage, deficit float64 }

func auraFloat(start float64, a aura, running, duration float64) auraValue {
	cap, rise, fall := float64(a.cap), float64(a.rise), float64(a.fall)
	falling := math.Min(running, start/fall)
	after := math.Max(0, start-fall*running)
	runArea := (start + after) * falling / 2
	runLoss := ((cap-start)+(cap-after))*falling/2 + cap*(running-falling)
	casting := math.Max(0, duration-running)
	rising := math.Min(casting, (cap-after)/rise)
	final := math.Min(cap, after+rise*casting)
	castArea := (after+final)*rising/2 + cap*(casting-rising)
	castLoss := ((cap - after) + (cap - final)) * rising / 2
	return auraValue{final, runArea + castArea, runLoss + castLoss}
}
func auraInterval(start interval, a aura, running, duration interval) (interval, interval) {
	cap := exactInterval(a.cap)
	falling := positiveInterval(minInterval(running, divInterval(start, a.fall)))
	after := positiveInterval(subInterval(start, mulInterval(exactInterval(a.fall), running)))
	casting := positiveInterval(subInterval(duration, running))
	rising := positiveInterval(minInterval(casting,
		divInterval(positiveInterval(subInterval(cap, after)), a.rise)))
	final := minInterval(cap, addInterval(after, mulInterval(exactInterval(a.rise), casting)))
	run := divInterval(mulInterval(addInterval(
		positiveInterval(subInterval(cap, start)),
		positiveInterval(subInterval(cap, after))), falling), 2)
	run = addInterval(run, mulInterval(cap, positiveInterval(subInterval(running, falling))))
	cast := divInterval(mulInterval(addInterval(
		positiveInterval(subInterval(cap, after)),
		positiveInterval(subInterval(cap, final))), rising), 2)
	return final, positiveInterval(addInterval(run, cast))
}

// Coefficients of distinct squarefree radicals give an exact canonical zero test.
type surd map[uint64]*big.Rat
type rootKey struct {
	radicand uint64
	digits   int
}
type rationalBounds struct{ low, high *big.Rat }

var rootCache = make(map[rootKey]rationalBounds)
var factorCache = make(map[int64]surd)

func integerSurd(x int64) surd {
	if x == 0 {
		return surd{}
	}
	return surd{1: big.NewRat(x, 1)}
}
func addSurd(a, b surd) surd {
	result := make(surd, len(a)+len(b))
	for key, value := range a {
		result[key] = value
	}
	for key, value := range b {
		if old, ok := result[key]; ok {
			value = new(big.Rat).Add(old, value)
			if value.Sign() == 0 {
				delete(result, key)
				continue
			}
		}
		result[key] = value
	}
	return result
}
func negSurd(a surd) surd {
	result := make(surd, len(a))
	for key, value := range a {
		result[key] = new(big.Rat).Neg(value)
	}
	return result
}
func subSurd(a, b surd) surd { return addSurd(a, negSurd(b)) }
func gcd(a, b uint64) uint64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
func mulSurd(a, b surd) surd {
	result := make(surd)
	for first, x := range a {
		for second, y := range b {
			common := gcd(first, second)
			key := (first / common) * (second / common)
			value := new(big.Rat).Mul(x, y)
			value.Mul(value, new(big.Rat).SetInt(new(big.Int).SetUint64(common)))
			if old, ok := result[key]; ok {
				value.Add(value, old)
			}
			if value.Sign() == 0 {
				delete(result, key)
			} else {
				result[key] = value
			}
		}
	}
	return result
}
func scaleSurd(a surd, scalar int64) surd {
	if scalar == 0 {
		return surd{}
	}
	result := make(surd, len(a))
	for key, value := range a {
		result[key] = new(big.Rat).Mul(value, big.NewRat(scalar, 1))
	}
	return result
}
func divSurd(a surd, denominator int64) surd {
	result := make(surd, len(a))
	for key, value := range a {
		result[key] = new(big.Rat).Quo(value, big.NewRat(denominator, 1))
	}
	return result
}
func rootBounds(radicand uint64, digits int) rationalBounds {
	key := rootKey{radicand, digits}
	if result, ok := rootCache[key]; ok {
		return result
	}
	den := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(digits)), nil)
	value := new(big.Int).Mul(den, den)
	value.Mul(value, new(big.Int).SetUint64(radicand))
	value.Sqrt(value)
	result := rationalBounds{new(big.Rat).SetFrac(value, den),
		new(big.Rat).SetFrac(new(big.Int).Add(value, big.NewInt(1)), den)}
	rootCache[key] = result
	return result
}
func boundSurd(a surd, digits int) rationalBounds {
	low, high := new(big.Rat), new(big.Rat)
	for key, value := range a {
		if key == 1 {
			low.Add(low, value)
			high.Add(high, value)
			continue
		}
		bounds := rootBounds(key, digits)
		left, right := bounds.low, bounds.high
		if value.Sign() < 0 {
			left, right = right, left
		}
		low.Add(low, new(big.Rat).Mul(value, left))
		high.Add(high, new(big.Rat).Mul(value, right))
	}
	return rationalBounds{low, high}
}
func signSurd(a surd) int {
	if len(a) == 0 {
		return 0
	}
	if len(a) == 1 {
		for _, value := range a {
			return value.Sign()
		}
	}
	for digits := initialRootDigits; ; digits *= 2 {
		bounds := boundSurd(a, digits)
		if bounds.low.Sign() > 0 {
			return 1
		}
		if bounds.high.Sign() < 0 {
			return -1
		}
	}
}
func compareSurd(a, b surd) int { return signSurd(subSurd(a, b)) }
func equalSurd(a, b surd) bool {
	if len(a) != len(b) {
		return false
	}
	for key, value := range a {
		other, ok := b[key]
		if !ok || value.Cmp(other) != 0 {
			return false
		}
	}
	return true
}
func minSurd(a, b surd) surd {
	if compareSurd(a, b) <= 0 {
		return a
	}
	return b
}
func maxSurd(a, b surd) surd {
	if compareSurd(a, b) >= 0 {
		return a
	}
	return b
}
func floatBounds(a surd) interval {
	bounds := boundSurd(a, boundRootDigits)
	low, _ := bounds.low.Float64()
	high, _ := bounds.high.Float64()
	if new(big.Rat).SetFloat64(low).Cmp(bounds.low) > 0 {
		low = down(low)
	}
	if new(big.Rat).SetFloat64(high).Cmp(bounds.high) < 0 {
		high = up(high)
	}
	return interval{low, high}
}
func squareRoot(value int64) surd {
	if value == 0 {
		return surd{}
	}
	if result, ok := factorCache[value]; ok {
		return result
	}
	remaining, outside, inside := value, int64(1), int64(1)
	for divisor := int64(2); divisor*divisor <= remaining; divisor++ {
		count := 0
		for remaining%divisor == 0 {
			remaining /= divisor
			count++
		}
		for pair := 0; pair < count/2; pair++ {
			outside *= divisor
		}
		if count%2 != 0 {
			inside *= divisor
		}
	}
	result := surd{uint64(inside * remaining): big.NewRat(outside, 1)}
	factorCache[value] = result
	return result
}
func exactTravel(a, b point, speed int64) surd {
	return divSurd(squareRoot(squaredDistance(a, b)), speed)
}
func exactAura(start surd, a aura, running, duration surd, healing bool) (surd, surd) {
	cap := integerSurd(a.cap)
	after := maxSurd(integerSurd(0), subSurd(start, scaleSurd(running, a.fall)))
	final := minSurd(cap, addSurd(after, scaleSurd(subSurd(duration, running), a.rise)))
	run := divSurd(subSurd(mulSurd(start, start), mulSurd(after, after)), 2*a.fall)
	left, right := subSurd(cap, after), subSurd(cap, final)
	deficit := divSurd(subSurd(mulSurd(left, left), mulSurd(right, right)), 2*a.rise)
	if healing {
		return final, addSurd(subSurd(scaleSurd(running, a.cap), run), deficit)
	}
	return final, subSurd(addSurd(run, scaleSurd(subSurd(duration, running), a.cap)), deficit)
}

type exactWeights [][][]surd

func exactGroup(auras []aura, speed int64, start point, breaths []spell,
	storm spell, initial, healing bool) exactWeights {
	first := storm
	if len(breaths) > 0 {
		first = breaths[0]
	}
	outgoing := make([]surd, len(first.places))
	for i, p := range first.places {
		outgoing[i] = exactTravel(start, p, speed)
	}
	returning := []surd{}
	latest := outgoing[0]
	if len(breaths) > 0 {
		latest = integerSurd(0)
		for _, p := range breaths[len(breaths)-1].places {
			t := exactTravel(p, storm.places[0], speed)
			returning = append(returning, t)
			latest = maxSurd(latest, t)
		}
	}
	pairs := len(breaths) == 2
	between := make([][]surd, len(first.places))
	if pairs {
		for i, p := range first.places {
			for _, q := range breaths[1].places {
				between[i] = append(between[i], exactTravel(p, q, speed))
			}
		}
	}
	result := make(exactWeights, len(auras))
	for actor, a := range auras {
		initialPower := integerSurd(a.cap)
		if initial && !healing {
			initialPower = integerSurd(0)
		}
		result[actor] = make([][]surd, len(outgoing))
		for left, t := range outgoing {
			duration := integerSurd(first.duration)
			if healing && len(breaths) == 0 {
				duration = latest
			}
			power, metric := exactAura(initialPower, a, t, duration, healing)
			columns := 1
			if pairs {
				columns = len(returning)
			}
			for right := 0; right < columns; right++ {
				value := metric
				if len(breaths) > 0 {
					at, slot := power, left
					if pairs {
						var extra surd
						at, extra = exactAura(power, a, between[left][right],
							integerSurd(breaths[1].duration), healing)
						value = addSurd(value, extra)
						slot = right
					}
					end := integerSurd(storm.duration)
					if healing {
						end = latest
					}
					_, extra := exactAura(at, a, returning[slot], end, healing)
					value = addSurd(value, extra)
				}
				result[actor][left] = append(result[actor][left], value)
			}
		}
	}
	return result
}

func maskPlaces(mask int) []int {
	result := []int{}
	for mask != 0 {
		bit := mask & -mask
		result = append(result, bits.TrailingZeros(uint(bit)))
		mask ^= bit
	}
	return result
}
func restrictWeights(weights exactWeights, firstMask, secondMask int, pairs bool) exactWeights {
	first, second := maskPlaces(firstMask), []int{0}
	if pairs {
		second = maskPlaces(secondMask)
	}
	result := make(exactWeights, len(weights))
	for actor, person := range weights {
		for _, left := range first {
			row := []surd{}
			for _, right := range second {
				row = append(row, person[left][right])
			}
			result[actor] = append(result[actor], row)
		}
	}
	return result
}
func sameWeights(a, b [][]surd) bool {
	for i, row := range a {
		for j, value := range row {
			if !equalSurd(value, b[i][j]) {
				return false
			}
		}
	}
	return true
}

// Only a parent byte and outward intervals are stored at each exact DP state.
func restrictedOptimum(weights exactWeights, pairs bool) surd {
	size := len(weights)
	identical := true
	for _, person := range weights[1:] {
		identical = identical && sameWeights(person, weights[0])
	}
	if identical {
		if !pairs {
			result := integerSurd(0)
			for _, row := range weights[0] {
				result = addSurd(result, row[0])
			}
			return result
		}
		matrix := weights[0]
		weights = make(exactWeights, size)
		for actor := 0; actor < size; actor++ {
			for place := 0; place < size; place++ {
				weights[actor] = append(weights[actor], []surd{matrix[actor][place]})
			}
		}
		pairs = false
	}
	limit := 1 << uint(size)
	count := limit
	if pairs {
		count *= limit
	}
	lower, upper := make([]float64, count), make([]float64, count)
	parent := make([]byte, count)
	for i := range lower {
		lower[i] = math.Inf(1)
		upper[i] = math.Inf(1)
		parent[i] = missingParent
	}
	lower[0], upper[0] = 0, 0
	bounds := make([][][]interval, size)
	for actor, person := range weights {
		for _, row := range person {
			converted := []interval{}
			for _, value := range row {
				converted = append(converted, floatBounds(value))
			}
			bounds[actor] = append(bounds[actor], converted)
		}
	}
	groups := make([][]int, size+1)
	for mask := 0; mask < limit; mask++ {
		k := bits.OnesCount(uint(mask))
		groups[k] = append(groups[k], mask)
	}
	path := func(index, people int) [][2]int {
		result := make([][2]int, people)
		for people > 0 {
			code := int(parent[index])
			a, b := code, 0
			if pairs {
				a, b = code/size, code%size
			}
			result[people-1] = [2]int{a, b}
			left, right := index, 0
			if pairs {
				left, right = index/limit, index%limit
			}
			left ^= 1 << uint(a)
			if pairs {
				right ^= 1 << uint(b)
				index = left*limit + right
			} else {
				index = left
			}
			people--
		}
		return result
	}
	for actor := 0; actor < size; actor++ {
		for _, left := range groups[actor] {
			seconds := []int{0}
			if pairs {
				seconds = groups[actor]
			}
			for _, right := range seconds {
				index := left
				if pairs {
					index = left*limit + right
				}
				if math.IsInf(lower[index], 1) {
					continue
				}
				for freeA := (limit - 1) ^ left; freeA != 0; {
					bitA := freeA & -freeA
					freeA ^= bitA
					a := bits.TrailingZeros(uint(bitA))
					freeB := 1
					if pairs {
						freeB = (limit - 1) ^ right
					}
					for freeB != 0 {
						bitB := freeB & -freeB
						freeB ^= bitB
						b := 0
						if pairs {
							b = bits.TrailingZeros(uint(bitB))
						}
						target := left | bitA
						if pairs {
							target = target*limit + (right | bitB)
						}
						bound := bounds[actor][a][b]
						low, high := down(lower[index]+bound.low), up(upper[index]+bound.high)
						choose := math.IsInf(lower[target], 1) || high < lower[target]
						if !choose && low < upper[target] {
							candidate := append(path(index, actor), [2]int{a, b})
							incumbent := path(target, actor+1)
							difference := integerSurd(0)
							for person, choice := range candidate {
								other := incumbent[person]
								if choice != other {
									difference = addSurd(difference, subSurd(
										weights[person][choice[0]][choice[1]],
										weights[person][other[0]][other[1]]))
								}
							}
							choose = signSurd(difference) < 0
						}
						if choose {
							lower[target], upper[target] = low, high
							code := a
							if pairs {
								code = a*size + b
							}
							parent[target] = byte(code)
						}
					}
				}
			}
		}
	}
	result := integerSurd(0)
	for actor, choice := range path(count-1, size) {
		result = addSurd(result, weights[actor][choice[0]][choice[1]])
	}
	return result
}

type block struct {
	attackers, healers []aura
	health, speed      int64
	start              point
	breaths            []spell
	storm              spell
	initial            bool
}

func (b block) exactBudget() surd {
	capSum := int64(0)
	for _, a := range b.healers {
		capSum += a.cap
	}
	fixed := int64(0)
	for _, s := range b.breaths {
		fixed += (s.power - capSum) * s.duration
	}
	latest := exactTravel(b.start, b.storm.places[0], b.speed)
	if len(b.breaths) > 0 {
		latest = integerSurd(0)
		for _, p := range b.breaths[len(b.breaths)-1].places {
			latest = maxSurd(latest, exactTravel(p, b.storm.places[0], b.speed))
		}
	}
	return subSurd(integerSurd(b.health-fixed), scaleSurd(latest, b.storm.power-capSum))
}

type survivalRefiner struct {
	weights exactWeights
	budget  surd
	pairs   bool
	cache   map[int]bool
}

func newSurvivalRefiner(b block) *survivalRefiner {
	return &survivalRefiner{
		exactGroup(b.healers, b.speed, b.start, b.breaths, b.storm, b.initial, true),
		b.exactBudget(), len(b.breaths) == 2, make(map[int]bool)}
}
func (r *survivalRefiner) feasible(first, second int) bool {
	key := first<<maskKeyBits | second
	if result, ok := r.cache[key]; ok {
		return result
	}
	weights := restrictWeights(r.weights, first, second, r.pairs)
	low, diagonal := integerSurd(0), integerSurd(0)
	for actor, person := range weights {
		best := person[0][0]
		for _, row := range person {
			for _, value := range row {
				best = minSurd(best, value)
			}
		}
		low = addSurd(low, best)
		column := 0
		if r.pairs {
			column = actor
		}
		diagonal = addSurd(diagonal, person[actor][column])
	}
	result := false
	if compareSurd(low, r.budget) < 0 {
		result = compareSurd(diagonal, r.budget) < 0
		if !result {
			result = compareSurd(restrictedOptimum(weights, r.pairs), r.budget) < 0
		}
	}
	r.cache[key] = result
	return result
}

type floatWeights [][][]float64

func (b block) group(auras []aura, healing bool) (floatWeights, float64) {
	first := b.storm
	if len(b.breaths) > 0 {
		first = b.breaths[0]
	}
	size := len(first.places)
	outgoing, outBounds := make([]float64, size), make([]interval, size)
	for i, p := range first.places {
		outgoing[i] = travel(b.start, p, b.speed)
		outBounds[i] = travelInterval(b.start, p, b.speed)
	}
	returning, retBounds := []float64{}, []interval{}
	latest, latestBounds := outgoing[0], outBounds[0]
	if len(b.breaths) > 0 {
		latest, latestBounds = 0, interval{}
		for _, p := range b.breaths[len(b.breaths)-1].places {
			t, bound := travel(p, b.storm.places[0], b.speed), travelInterval(p, b.storm.places[0], b.speed)
			returning = append(returning, t)
			retBounds = append(retBounds, bound)
			latest = math.Max(latest, t)
			latestBounds = maxInterval(latestBounds, bound)
		}
	}
	pairs := len(b.breaths) == 2
	between := make([][]float64, size)
	betweenBounds := make([][]interval, size)
	if pairs {
		for i, p := range first.places {
			for _, q := range b.breaths[1].places {
				between[i] = append(between[i], travel(p, q, b.speed))
				betweenBounds[i] = append(betweenBounds[i], travelInterval(p, q, b.speed))
			}
		}
	}
	result := make(floatWeights, len(auras))
	error, largestSum := 0.0, 0.0
	for actor, a := range auras {
		initialPower := a.cap
		if b.initial && !healing {
			initialPower = 0
		}
		largestError, largestWeight := 0.0, 0.0
		result[actor] = make([][]float64, size)
		for left, t := range outgoing {
			duration, durationBounds := float64(first.duration), exactInterval(first.duration)
			if healing && len(b.breaths) == 0 {
				duration, durationBounds = latest, latestBounds
			}
			state := auraFloat(float64(initialPower), a, t, duration)
			powerBound, lossBound := auraInterval(
				exactInterval(initialPower), a, outBounds[left], durationBounds)
			columns := 1
			if pairs {
				columns = size
			}
			for right := 0; right < columns; right++ {
				value := state.damage
				if healing {
					value = state.deficit
				}
				loss, area := lossBound, mulInterval(exactInterval(a.cap), durationBounds)
				if len(b.breaths) > 0 {
					middle, middleBound, slot := state, powerBound, left
					if pairs {
						middle = auraFloat(state.power, a, between[left][right], float64(b.breaths[1].duration))
						var extra interval
						middleBound, extra = auraInterval(powerBound, a, betweenBounds[left][right],
							exactInterval(b.breaths[1].duration))
						loss = addInterval(loss, extra)
						area = addInterval(area, exactInterval(a.cap*b.breaths[1].duration))
						if healing {
							value += middle.deficit
						} else {
							value += middle.damage
						}
						slot = right
					}
					end, endBound := float64(b.storm.duration), exactInterval(b.storm.duration)
					if healing {
						end, endBound = latest, latestBounds
					}
					final := auraFloat(middle.power, a, returning[slot], end)
					_, extra := auraInterval(middleBound, a, retBounds[slot], endBound)
					loss = addInterval(loss, extra)
					area = addInterval(area, mulInterval(exactInterval(a.cap), endBound))
					if healing {
						value += final.deficit
					} else {
						value += final.damage
					}
				}
				bound := loss
				if !healing {
					bound = subInterval(area, loss)
				}
				largestError = up(math.Max(largestError,
					math.Max(math.Abs(value-bound.low), math.Abs(bound.high-value))))
				largestWeight = math.Max(largestWeight, math.Max(math.Abs(value),
					math.Max(math.Abs(bound.low), math.Abs(bound.high))))
				result[actor][left] = append(result[actor][left], value)
			}
		}
		error = up(error + largestError)
		largestSum = up(largestSum + largestWeight)
	}
	ulp := math.Nextafter(largestSum, math.Inf(1)) - largestSum
	return result, up(error + 2*float64(len(auras))*ulp)
}

type maskLayout struct {
	groups         [][]int
	ranks, offsets []int
}

var layoutCache = make(map[int]*maskLayout)

func layoutFor(size int) *maskLayout {
	if result, ok := layoutCache[size]; ok {
		return result
	}
	limit := 1 << uint(size)
	result := &maskLayout{make([][]int, size+1), make([]int, limit), make([]int, size+2)}
	for mask := 0; mask < limit; mask++ {
		count := bits.OnesCount(uint(mask))
		result.ranks[mask] = len(result.groups[count])
		result.groups[count] = append(result.groups[count], mask)
	}
	for count, group := range result.groups {
		result.offsets[count+1] = result.offsets[count] + len(group)*len(group)
	}
	layoutCache[size] = result
	return result
}

type costTable struct {
	values []float64
	layout *maskLayout
	pairs  bool
}

func (t *costTable) get(first, second int) float64 {
	index := first
	if t.pairs {
		count := bits.OnesCount(uint(first))
		index = t.layout.offsets[count] + t.layout.ranks[first]*len(t.layout.groups[count])
		index += t.layout.ranks[second]
	}
	return t.values[index]
}

func assignment(weights floatWeights, size int, pairs, maximize bool, cutoff float64) *costTable {
	limit := 1 << uint(size)
	layout := layoutFor(size)
	count := limit
	if pairs {
		count = layout.offsets[len(weights)+1]
	}
	missing := cutoff
	if maximize {
		missing = -1
	}
	result := make([]float64, count)
	for i := range result {
		result[i] = missing
	}
	result[0] = 0
	groups := layout.groups
	for actor, person := range weights {
		for _, left := range groups[actor] {
			seconds := []int{0}
			if pairs {
				seconds = groups[actor]
			}
			for _, right := range seconds {
				index := left
				if pairs {
					index = layout.offsets[actor] + layout.ranks[left]*len(groups[actor])
					index += layout.ranks[right]
				}
				current := result[index]
				if (maximize && current < 0) || (!maximize && current >= cutoff) {
					continue
				}
				for freeA := (limit - 1) ^ left; freeA != 0; {
					bitA := freeA & -freeA
					freeA ^= bitA
					a := bits.TrailingZeros(uint(bitA))
					freeB := 1
					if pairs {
						freeB = (limit - 1) ^ right
					}
					for freeB != 0 {
						bitB := freeB & -freeB
						freeB ^= bitB
						b := 0
						if pairs {
							b = bits.TrailingZeros(uint(bitB))
						}
						target := left | bitA
						if pairs {
							target = layout.offsets[actor+1] + layout.ranks[target]*len(groups[actor+1])
							target += layout.ranks[right|bitB]
						}
						candidate := current + person[a][b]
						if (maximize && candidate > result[target]) || (!maximize && candidate < result[target]) {
							result[target] = candidate
						}
					}
				}
			}
		}
	}
	return &costTable{result, layout, pairs}
}

type candidate struct {
	first, second int
	value         float64
}
type damageCertificate struct {
	bounds interval
	exact  surd
	refine func() surd
}

func (d *damageCertificate) exactValue() surd {
	if d.refine != nil {
		d.exact = d.refine()
		d.refine = nil
	}
	return d.exact
}
func (b block) exactDamage(candidates []candidate, error float64) surd {
	weights := exactGroup(b.attackers, b.speed, b.start, b.breaths, b.storm, b.initial, false)
	if len(b.breaths) == 0 {
		result := integerSurd(0)
		for _, person := range weights {
			result = addSurd(result, person[0][0])
		}
		return result
	}
	pairs := len(b.breaths) == 2
	sort.Slice(candidates, func(i, j int) bool { return candidates[i].value > candidates[j].value })
	globalUpper := integerSurd(0)
	for _, person := range weights {
		largest := person[0][0]
		for _, row := range person {
			for _, value := range row {
				largest = maxSurd(largest, value)
			}
		}
		globalUpper = addSurd(globalUpper, largest)
	}
	for _, choice := range candidates {
		if pairs && choice.first != choice.second {
			continue
		}
		places := maskPlaces(choice.first)
		diagonal := integerSurd(0)
		for actor, place := range places {
			column := 0
			if pairs {
				column = place
			}
			diagonal = addSurd(diagonal, weights[actor][place][column])
		}
		if equalSurd(diagonal, globalUpper) {
			return globalUpper
		}
		break
	}
	var best surd
	bestLow := math.Inf(-1)
	for _, choice := range candidates {
		if up(choice.value+error) < bestLow {
			break
		}
		part := restrictWeights(weights, choice.first, choice.second, pairs)
		upper, diagonal := integerSurd(0), integerSurd(0)
		for actor, person := range part {
			maximum := person[0][0]
			for _, row := range person {
				for _, value := range row {
					maximum = maxSurd(maximum, value)
				}
			}
			upper = addSurd(upper, maximum)
			column := 0
			if pairs {
				column = actor
			}
			diagonal = addSurd(diagonal, person[actor][column])
		}
		if best != nil && compareSurd(upper, best) <= 0 {
			continue
		}
		value := upper
		if !equalSurd(diagonal, upper) {
			negative := make(exactWeights, len(part))
			for actor, person := range part {
				for _, row := range person {
					converted := []surd{}
					for _, cost := range row {
						converted = append(converted, negSurd(cost))
					}
					negative[actor] = append(negative[actor], converted)
				}
			}
			value = negSurd(restrictedOptimum(negative, pairs))
		}
		if best == nil || compareSurd(value, best) > 0 {
			best = value
			if equalSurd(best, globalUpper) {
				return best
			}
			bestLow = floatBounds(best).low
		}
	}
	return best
}
func (b block) damage() *damageCertificate {
	capSum := int64(0)
	for _, a := range b.healers {
		capSum += a.cap
	}
	fixed := int64(0)
	for _, s := range b.breaths {
		fixed += (s.power - capSum) * s.duration
	}
	latest := travel(b.start, b.storm.places[0], b.speed)
	latestBound := travelInterval(b.start, b.storm.places[0], b.speed)
	if len(b.breaths) > 0 {
		latest, latestBound = 0, interval{}
		for _, p := range b.breaths[len(b.breaths)-1].places {
			latest = math.Max(latest, travel(p, b.storm.places[0], b.speed))
			latestBound = maxInterval(latestBound, travelInterval(p, b.storm.places[0], b.speed))
		}
	}
	budget := float64(b.health-fixed) - float64(b.storm.power-capSum)*latest
	budgetBound := subInterval(exactInterval(b.health-fixed),
		mulInterval(exactInterval(b.storm.power-capSum), latestBound))
	if budgetBound.high <= 0 {
		return nil
	}
	healerWeights, error := b.group(b.healers, true)
	error = up(error + up(math.Max(
		math.Abs(budget-budgetBound.low), math.Abs(budgetBound.high-budget))))
	var refiner *survivalRefiner
	survives := func(value float64, first, second int) bool {
		if math.IsInf(value, 1) {
			return false
		}
		if up(value+error) < budget {
			return true
		}
		if down(value-error) >= budget {
			return false
		}
		if len(b.breaths) == 0 {
			loss := integerSurd(0)
			for _, person := range exactGroup(
				b.healers, b.speed, b.start, b.breaths, b.storm, b.initial, true) {
				loss = addSurd(loss, person[0][0])
			}
			return compareSurd(loss, b.exactBudget()) < 0
		}
		if refiner == nil {
			refiner = newSurvivalRefiner(b)
		}
		return refiner.feasible(first, second)
	}
	if len(b.breaths) == 0 {
		loss := 0.0
		for _, person := range healerWeights {
			loss += person[0][0]
		}
		if !survives(loss, 0, 0) {
			return nil
		}
		weights, damageError := b.group(b.attackers, false)
		value := 0.0
		for _, person := range weights {
			value += person[0][0]
		}
		return &damageCertificate{
			bounds: interval{down(value - damageError), up(value + damageError)},
			refine: func() surd { return b.exactDamage(nil, damageError) }}
	}
	size := len(b.attackers) + len(b.healers)
	pairs := len(b.breaths) == 2
	limit := 1 << uint(size)
	full := limit - 1
	masks := []int{}
	for mask := 0; mask < limit; mask++ {
		if bits.OnesCount(uint(mask)) == len(b.healers) {
			masks = append(masks, mask)
		}
	}
	upperLoss := 0.0
	for _, person := range healerWeights {
		largest := 0.0
		for _, row := range person {
			for _, value := range row {
				largest = math.Max(largest, value)
			}
		}
		upperLoss = up(upperLoss + largest)
	}
	allSurvive := up(upperLoss+error) < budget
	var survival *costTable
	if !allSurvive {
		survival = assignment(healerWeights, size, pairs, false, up(budget+error))
	}
	feasible := func(first, second int) bool {
		if allSurvive {
			return true
		}
		return survives(survival.get(first, second), first, second)
	}
	any := allSurvive
	if !any {
		for _, first := range masks {
			seconds := []int{0}
			if pairs {
				seconds = masks
			}
			for _, second := range seconds {
				if feasible(first, second) {
					any = true
					break
				}
			}
			if any {
				break
			}
		}
	}
	if !any {
		return nil
	}
	attackerWeights, damageError := b.group(b.attackers, false)
	damage := assignment(attackerWeights, size, pairs, true, math.Inf(1))
	candidates := []candidate{}
	best := math.Inf(-1)
	for _, first := range masks {
		seconds := []int{0}
		if pairs {
			seconds = masks
		}
		for _, second := range seconds {
			if !feasible(first, second) {
				continue
			}
			left, right := full^first, 0
			if pairs {
				right = full ^ second
			}
			value := damage.get(left, right)
			best = math.Max(best, value)
			candidates = append(candidates, candidate{left, right, value})
		}
	}
	threshold := down(best - damageError)
	kept := candidates[:0]
	for _, choice := range candidates {
		if up(choice.value+damageError) >= threshold {
			kept = append(kept, choice)
		}
	}
	return &damageCertificate{
		bounds: interval{down(best - damageError), up(best + damageError)},
		refine: func() surd { return b.exactDamage(kept, damageError) }}
}
func killed(amounts []*damageCertificate, health int64) bool {
	total := interval{}
	for _, amount := range amounts {
		total = addInterval(total, amount.bounds)
	}
	if total.low >= float64(health) {
		return true
	}
	if total.high < float64(health) {
		return false
	}
	exact := integerSurd(0)
	for _, amount := range amounts {
		exact = addSurd(exact, amount.exactValue())
	}
	return compareSurd(exact, integerSurd(health)) >= 0
}
func solve(attackers, healers []aura, health, speed, dragon int64, spells []spell) int {
	start, initial := point{}, true
	breaths := []spell{}
	amounts := []*damageCertificate{}
	for index, s := range spells {
		if s.kind == tailName {
			break
		}
		if s.kind == breathName {
			breaths = append(breaths, s)
			continue
		}
		current := block{attackers, healers, health, speed, start, breaths, s, initial}
		amount := current.damage()
		if amount == nil {
			return 0
		}
		amounts = append(amounts, amount)
		if killed(amounts, dragon) {
			return index + 1
		}
		start, initial, breaths = s.places[0], false, nil
	}
	return 0
}
func readAndSolve(in *bufio.Reader) int {
	var n, m, k int
	var health, speed, dragon int64
	if _, err := fmt.Fscan(in, &n, &m, &k, &health, &speed, &dragon); err != nil {
		return 0
	}
	attackers, healers := make([]aura, n), make([]aura, m)
	for i := range attackers {
		fmt.Fscan(in, &attackers[i].cap, &attackers[i].rise, &attackers[i].fall)
	}
	for i := range healers {
		fmt.Fscan(in, &healers[i].cap, &healers[i].rise, &healers[i].fall)
	}
	spells := make([]spell, k)
	for i := range spells {
		fmt.Fscan(in, &spells[i].kind)
		if spells[i].kind == tailName {
			continue
		}
		fmt.Fscan(in, &spells[i].power, &spells[i].duration)
		places := 1
		if spells[i].kind == breathName {
			places = n + m
		}
		spells[i].places = make([]point, places)
		for j := range spells[i].places {
			fmt.Fscan(in, &spells[i].places[j].x, &spells[i].places[j].y)
		}
	}
	return solve(attackers, healers, health, speed, dragon, spells)
}
func main() {
	answer := readAndSolve(bufio.NewReader(os.Stdin))
	if answer == 0 {
		fmt.Println("You are not prepared")
	} else {
		fmt.Printf("No useful loot again\n%d\n", answer)
	}
}
