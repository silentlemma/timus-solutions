package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

const (
	perfect = iota
	great
	good
	boo
	miss
	marks
)

const (
	baseScore  = 1000000
	percent    = 100
	allPerfect = 10000000
	allGreat   = 1000000
	low        = 100
	slowest    = 1000 // ms per beat on Easy, halved on each harder level
	tenths     = 10
	perfectBy  = 4 // tenths of the period: under 40 % is perfect
	greatBy    = 7 // under 70 % is great
	separator  = "--------------------"
)

var (
	levels = []string{"Easy", "Medium", "Hard"}
	names  = [marks]string{"Perfect", "Great", "Good", "Boo", "Miss"}
	score  = [marks]int64{10, 5, 0, 0, 0}  // p
	combo  = [marks]int64{55, 33, 0, 0, 0} // q
	dance  = [marks]int{2, 1, 0, -4, -5}   // dance points

	// level bonuses: share of the most dance points needed, in percent
	shares     = []int64{80, 64, 50}
	shareBonus = []int64{100000, 10000, 1000}
)

type press struct {
	time int
	key  byte
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var duration, level, beats string
	fmt.Fscan(in, &duration, &level, &beats)
	index := 0
	for levels[index] != level {
		index++
	}
	diff, period := int64(index+1), slowest>>index
	var log []press
	for {
		var p press
		var key string
		if _, err := fmt.Fscan(in, &p.time, &key); err != nil {
			break
		}
		p.key = key[0]
		log = append(log, p)
	}
	sort.Slice(log, func(a, b int) bool { return log[a].time < log[b].time })
	steps := int64(len(beats) - strings.Count(beats, "N"))
	unit := diff * baseScore / (steps * (steps + 1) / 2) // B div S
	var counts [marks]int64
	var stage, comboBonus, run, n int64
	points, wentNegative := 0, false
	k := 0 // the first logged press not before the current beat
	for i := 0; i < len(beats); i++ {
		start, end := i*period, (i+1)*period
		for k < len(log) && log[k].time < start {
			k++
		}
		if beats[i] == 'N' {
			continue
		}
		n++
		// only the first press within the beat counts
		var mark int
		switch {
		case k == len(log) || log[k].time >= end:
			mark = boo
		case log[k].key != beats[i]:
			mark = miss
		default:
			elapsed := log[k].time - start
			switch {
			case tenths*elapsed < perfectBy*period:
				mark = perfect
			case tenths*elapsed < greatBy*period:
				mark = great
			default:
				mark = good
			}
		}
		counts[mark]++
		stage += score[mark] * n * unit
		if mark <= good {
			run++
		} else {
			run = 0
		}
		comboBonus += combo[mark] * run
		points += dance[mark]
		wentNegative = wentNegative || points < 0
	}
	most := int64(dance[perfect]) * steps
	bonus := int64(low)
	switch {
	case wentNegative:
		bonus = 0
	case counts[perfect] == steps:
		bonus = allPerfect
	case counts[perfect]+counts[great] == steps:
		bonus = allGreat
	default:
		for i, share := range shares {
			if percent*int64(points) >= share*most {
				bonus = shareBonus[i]
				break
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i, name := range names {
		fmt.Fprintf(out, "%s: %d\n", name, counts[i])
	}
	fmt.Fprintln(out, separator)
	fmt.Fprintf(out, "Stage Score: %d\nCombo Bonus: %d\n", stage, comboBonus)
	fmt.Fprintf(out, "Dance Level Bonus: %d\nTotal Score: %d\n", bonus, stage+comboBonus+bonus)
}
