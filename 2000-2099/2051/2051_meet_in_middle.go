package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math/bits"
	"os"
	"sort"
)

type point struct{ time, height int64 }
type input struct {
	data []byte
	at   int
}

func (in *input) next() int64 {
	for in.data[in.at] <= ' ' {
		in.at++
	}
	value := int64(0)
	for in.at < len(in.data) && in.data[in.at] > ' ' {
		value = value*10 + int64(in.data[in.at]-'0')
		in.at++
	}
	return value
}

func contactsOf(upper, lower []point, duration int64) []point {
	i, j, time := 0, 0, int64(0)
	var contacts []point
	for {
		for i+2 < len(upper) && upper[i+1].time <= time {
			i++
		}
		for j+2 < len(lower) && lower[j+1].time <= time {
			j++
		}
		a, b, c, d := upper[i], upper[i+1], lower[j], lower[j+1]
		hn := a.height*(b.time-time) + b.height*(time-a.time)
		gn := c.height*(d.time-time) + d.height*(time-c.time)
		hd, gd := b.time-a.time, d.time-c.time
		if hn*gd == gn*hd && time > 0 && time < duration {
			contacts = append(contacts, point{time, hn / hd})
		}
		if time == duration {
			return contacts
		}
		time = b.time
		if d.time < time {
			time = d.time
		}
	}
}

func augment(curve, contacts []point) []point {
	result := make([]point, 0, len(curve)+len(contacts))
	i, j := 0, 0
	for i < len(curve) || j < len(contacts) {
		if j == len(contacts) || (i < len(curve) && curve[i].time < contacts[j].time) {
			result = append(result, curve[i])
			i++
		} else if i == len(curve) || contacts[j].time < curve[i].time {
			result = append(result, contacts[j])
			j++
		} else {
			result = append(result, curve[i])
			i++
			j++
		}
	}
	return result
}

func areas(curve []point, boundaries []int64) []int64 {
	var result []int64
	total, region := int64(0), 1
	for i := 0; i+1 < len(curve); i++ {
		a, b := curve[i], curve[i+1]
		total += (a.height + b.height) * (b.time - a.time)
		if b.time == boundaries[region] {
			result = append(result, total)
			total = 0
			region++
		}
	}
	return result
}

func choose(weights []int64) int {
	leftCount := len(weights) / 2
	scale := int64(1) << uint(leftCount)
	total := int64(0)
	for _, weight := range weights {
		total += weight
	}
	target := total / 2
	keys := make([]int64, 1, 1<<uint(leftCount))
	for bit := 0; bit < leftCount; bit++ {
		step := weights[bit]*scale + (int64(1) << uint(bit))
		oldSize := len(keys)
		for i := 0; i < oldSize; i++ {
			keys = append(keys, keys[i]+step)
		}
	}
	sort.Slice(keys, func(i, j int) bool { return keys[i] < keys[j] })
	previous, rightSum := 0, int64(0)
	for index := 0; index < 1<<uint(len(weights)-leftCount); index++ {
		gray := index ^ (index >> 1)
		if index != 0 {
			changed := gray ^ previous
			bit := bits.TrailingZeros(uint(changed))
			weight := weights[leftCount+bit]
			if gray&changed != 0 {
				rightSum += weight
			} else {
				rightSum -= weight
			}
		}
		previous = gray
		need := target - rightSum
		position := sort.Search(len(keys), func(i int) bool { return keys[i] >= need*scale })
		if position < len(keys) && keys[position]/scale == need {
			return int(keys[position]&(scale-1)) | (gray << uint(leftCount))
		}
	}
	return 0
}

func add(curve []point, p point) []point {
	if len(curve) > 0 && curve[len(curve)-1].time == p.time {
		return curve
	}
	for len(curve) >= 2 {
		a, b := curve[len(curve)-2], curve[len(curve)-1]
		if (b.height-a.height)*(p.time-b.time) != (p.height-b.height)*(b.time-a.time) {
			break
		}
		curve = curve[:len(curve)-1]
	}
	return append(curve, p)
}

func solve(duration int64, originalUpper, originalLower []point) [2][]point {
	contacts := contactsOf(originalUpper, originalLower, duration)
	boundaries := []int64{0}
	for _, p := range contacts {
		boundaries = append(boundaries, p.time)
	}
	boundaries = append(boundaries, duration)
	upper, lower := augment(originalUpper, contacts), augment(originalLower, contacts)
	ua, la := areas(upper, boundaries), areas(lower, boundaries)
	weights := make([]int64, len(ua))
	for i := range ua {
		weights[i] = ua[i] - la[i]
	}
	mask := choose(weights)
	var result [2][]point
	hi, lo := 0, 0
	for region := 0; region+1 < len(boundaries); region++ {
		destination := 1
		if mask&(1<<uint(region)) != 0 {
			destination = 0
		}
		end := boundaries[region+1]
		for hi < len(upper) && upper[hi].time <= end {
			result[destination] = add(result[destination], upper[hi])
			hi++
		}
		for lo < len(lower) && lower[lo].time <= end {
			result[1-destination] = add(result[1-destination], lower[lo])
			lo++
		}
		hi--
		lo--
	}
	return result
}

func readCurve(in *input) []point {
	curve := make([]point, int(in.next()))
	for i := range curve {
		curve[i] = point{in.next(), in.next()}
	}
	return curve
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	duration := in.next()
	upper, lower := readCurve(&in), readCurve(&in)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, curve := range solve(duration, upper, lower) {
		fmt.Fprintln(out, len(curve))
		for _, p := range curve {
			fmt.Fprintln(out, p.time, p.height)
		}
	}
}
