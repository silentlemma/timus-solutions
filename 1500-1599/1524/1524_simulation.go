package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
	"sort"
	"strings"
)

const eps = 1e-9 // rounding to the closest minute must not suffer from 0.4999999
const day, hour = 24 * 60, 60
const none = -1

// quest kinds
const (
	run = iota
	kill
	findout
	talk
)

// message kinds in the order they are printed within one minute
const (
	bought = iota + 1
	broken
	killed
	finished
	tired
	joined
	started
)

const half = 0.5

// the order of the traits of an agent in the input
const (
	accIdx = iota
	walkIdx
	intelIdx
	expIdx
	driveIdx
	traits
)

func minutes(x float64) int { return int(math.Floor(x + half + eps)) }

type agent struct {
	name                         string
	letter                       byte
	acc, walk, intel, exp, drive float64
	busy, alive                  bool
}

type carType struct {
	need  float64
	limit int
	name  string
}

type car struct {
	kind, passed int
	id           string
	busy, broken bool
}

type monster struct {
	needExp, needInt float64
	evade, value     int
	name             string
}

type quest struct {
	kind, dist, monster int
	need                float64
	mint                int
	state               int // 0 waiting, 1 under way, 2 done
}

// a team with its car (or none) and the moments of the quest counted from
// its start, none where there is no such moment
type plan struct {
	team               []int
	car                int
	total, broke, kill int
	walked, drove      int
}

type event struct{ time, kind, num int }
type timeline []event

func (h timeline) Len() int { return len(h) }
func (h timeline) Less(i, j int) bool {
	a, b := h[i], h[j]
	if a.time != b.time {
		return a.time < b.time
	}
	if a.kind != b.kind {
		return a.kind < b.kind
	}
	return a.num < b.num
}
func (h timeline) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *timeline) Push(x interface{}) { *h = append(*h, x.(event)) }
func (h *timeline) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

type message struct {
	kind int
	text string
}

var (
	agents   []*agent
	types    []carType
	cars     []*car
	monsters []monster
	quests   []*quest
	active   = map[int]*plan{}
	events   timeline
	log      []message

	maxWalk, maxEvade, maxValue int
	retire                      float64
)

func letters(team []int) string {
	s := ""
	for _, a := range team {
		s += string(agents[a].letter)
	}
	return s
}

func teamText(team []int) string {
	s := fmt.Sprintf("Agent %c", agents[team[0]].letter)
	if len(team) > 1 {
		s += fmt.Sprintf(" and agent %c", agents[team[1]].letter)
	}
	return s
}

type stats struct {
	walk, drive, acc, exp, intel float64
	driver                       int
}

func teamStats(team []int) stats {
	a := agents[team[0]]
	if len(team) == 1 {
		return stats{a.walk, a.drive, a.acc, a.exp, a.intel, team[0]}
	}
	b := agents[team[1]]
	driver := team[0]
	if b.drive > a.drive {
		driver = team[1]
	}
	return stats{math.Min(a.walk, b.walk), math.Max(a.drive, b.drive), (a.acc + b.acc) / 2,
		1 - (1-a.exp)*(1-b.exp), 1 - (1-a.intel)*(1-b.intel), driver}
}

// the time of the work at the place, and whether the team may do it
func actionTime(q *quest, st stats) (int, bool) {
	switch q.kind {
	case kill:
		m := monsters[q.monster]
		return minutes(float64(m.evade) / st.acc), st.exp >= m.needExp && st.intel >= m.needInt
	case findout:
		return minutes(float64(q.mint) / st.intel), st.intel >= q.need
	case talk:
		return minutes(float64(q.mint) / st.exp), st.exp >= q.need
	}
	return 0, true
}

func withCar(team []int, q *quest, action int, st stats, c int) *plan {
	cr := cars[c]
	t := types[cr.kind]
	rest := t.limit - cr.passed
	if rest <= 0 || st.drive < t.need {
		return nil
	}
	d := q.dist
	byCar := func(x int) int { return minutes(float64(x) / st.drive) }
	onFoot := func(x int) int { return minutes(float64(x) / st.walk) }
	p := &plan{team: team, car: c, broke: none, kill: none}
	var there, back int
	switch {
	case rest < d: // breaks on the way there, the rest is walked
		there = byCar(rest) + onFoot(d-rest)
		back = onFoot(d)
		p.broke, p.walked, p.drove = byCar(rest), 2*d-rest, rest
	case rest == d: // breaks on arrival
		there, back = byCar(d), onFoot(d)
		p.broke, p.walked, p.drove = there, d, d
	case rest < 2*d: // breaks on the way back
		there = byCar(d)
		back = byCar(rest-d) + onFoot(2*d-rest)
		p.broke, p.walked, p.drove = there+action+byCar(rest-d), 2*d-rest, rest
	default:
		there, back = byCar(d), byCar(d)
		p.walked, p.drove = 0, 2*d
		if rest == 2*d { // breaks on return
			p.broke = there + action + back
		}
	}
	p.total = there + action + back
	if q.kind == kill {
		p.kill = there + action
	}
	return p
}

func bestForTeam(team []int, q *quest, freeCars []int) *plan {
	st := teamStats(team)
	action, ok := actionTime(q, st)
	if !ok {
		return nil
	}
	there := minutes(float64(q.dist) / st.walk)
	best := &plan{team: team, car: none, total: 2*there + action, broke: none, kill: none,
		walked: 2 * q.dist}
	if q.kind == kill {
		best.kill = there + action
	}
	for _, c := range freeCars {
		p := withCar(team, q, action, st, c)
		// a car only when strictly faster, then the smaller id
		if p != nil && (p.total < best.total ||
			(p.total == best.total && best.car != none && cars[c].id < cars[best.car].id)) {
			best = p
		}
	}
	return best
}

func better(a, b *plan) bool {
	if b == nil {
		return true
	}
	if a.total != b.total {
		return a.total < b.total
	}
	if len(a.team) != len(b.team) {
		return len(a.team) < len(b.team)
	}
	return letters(a.team) < letters(b.team)
}

func bestPlan(q *quest) *plan {
	var free, freeCars []int
	for i, a := range agents {
		if a.alive && !a.busy {
			free = append(free, i)
		}
	}
	sort.Slice(free, func(i, j int) bool { return agents[free[i]].letter < agents[free[j]].letter })
	for i, c := range cars {
		if !c.broken && !c.busy && c.passed < types[c.kind].limit {
			freeCars = append(freeCars, i)
		}
	}
	sort.Slice(freeCars, func(i, j int) bool { return cars[freeCars[i]].id < cars[freeCars[j]].id })
	var teams [][]int
	for _, a := range free {
		teams = append(teams, []int{a})
	}
	for i, a := range free {
		for _, b := range free[i+1:] {
			teams = append(teams, []int{a, b})
		}
	}
	var best *plan
	for _, team := range teams {
		if p := bestForTeam(team, q, freeCars); p != nil && better(p, best) {
			best = p
		}
	}
	return best
}

func start(num int, q *quest, p *plan, now int) {
	q.state = 1
	active[num] = p
	if p.broke != none {
		heap.Push(&events, event{now + p.broke, broken, num})
	}
	if p.kill != none {
		heap.Push(&events, event{now + p.kill, killed, num})
	}
	heap.Push(&events, event{now + p.total, finished, num})
	for _, a := range p.team {
		agents[a].busy = true
	}
	text := fmt.Sprintf("%s started quest %d", teamText(p.team), num)
	if p.car != none {
		cars[p.car].busy = true
		text += " using car " + cars[p.car].id
	}
	log = append(log, message{started, text + "."})
}

func finish(num int) {
	p := active[num]
	delete(active, num)
	q := quests[num-1]
	log = append(log, message{finished, fmt.Sprintf("%s finished quest %d.", teamText(p.team), num)})
	if p.car != none {
		c := cars[p.car]
		if !c.broken {
			c.busy = false
			c.passed += p.drove
			if limit := types[c.kind].limit; c.passed > limit {
				c.passed = limit
			}
		}
	}
	var gone []string
	for _, i := range p.team {
		a := agents[i]
		a.busy = false
		acc, walk, intel, exp, drive := a.acc, a.walk, a.intel, a.exp, a.drive
		if p.walked > 0 {
			a.walk = walk + (1-walk)*float64(p.walked)/float64(maxWalk)
		}
		if p.car != none && p.drove > 0 {
			a.drive = drive + (1-drive)*float64(p.drove)/float64(maxWalk)
		}
		switch q.kind {
		case kill:
			m := monsters[q.monster]
			a.exp = exp + (1-exp)*float64(m.value)/float64(maxValue)
			a.acc = acc + (1-acc)*float64(m.evade)/float64(maxEvade)
		case findout:
			a.exp = exp + (1-exp)*intel/float64(q.mint)
			a.intel = intel + (1-intel)*intel/float64(q.mint)
		case talk:
			a.exp = exp + (1-exp)*exp/float64(q.mint)
		}
		if a.alive && a.exp >= retire {
			a.alive = false
			gone = append(gone, string(a.letter))
		}
	}
	sort.Strings(gone)
	for _, letter := range gone {
		log = append(log, message{tired, "Agent " + letter + " has tired."})
	}
	q.state = 2
}

func newLetter(name string) byte {
	used := map[byte]bool{}
	for _, a := range agents {
		if a.alive {
			used[a.letter] = true
		}
	}
	target := int(strings.ToUpper(name[:1])[0])
	best, bestDist := byte(0), 0
	for c := byte('A'); c <= 'Z'; c++ {
		if used[c] {
			continue
		}
		d := int(c) - target
		if d < 0 {
			d = -d
		}
		if best == 0 || d < bestDist {
			best, bestDist = c, d
		}
	}
	return best
}

// an outside event: a new agent, a bought car or a received quest
type outside struct {
	time   int
	word   string
	name   string
	values [traits]float64
	passed int
	id     string
	q      quest
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		a := &agent{alive: true}
		var letter string
		fmt.Fscan(in, &a.name, &a.acc, &a.walk, &a.intel, &a.exp, &a.drive, &letter)
		a.letter = letter[0]
		agents = append(agents, a)
	}
	typeOf, monsterOf := map[string]int{}, map[string]int{}
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		var t carType
		fmt.Fscan(in, &t.need, &t.limit, &t.name)
		typeOf[t.name] = len(types)
		types = append(types, t)
	}
	newCar := func(name string, passed int, id string) {
		kind := typeOf[name]
		cars = append(cars, &car{kind: kind, passed: passed, id: id, broken: passed >= types[kind].limit})
	}
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		var name, id string
		var passed int
		fmt.Fscan(in, &name, &passed, &id)
		newCar(name, passed, id)
	}
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		var m monster
		fmt.Fscan(in, &m.needExp, &m.needInt, &m.evade, &m.value, &m.name)
		monsterOf[m.name] = len(monsters)
		monsters = append(monsters, m)
	}
	fmt.Fscan(in, &maxWalk, &maxEvade, &maxValue, &retire)
	fmt.Fscan(in, &n)
	outsides := make([]outside, n)
	for i := range outsides {
		e := &outsides[i]
		fmt.Fscan(in, &e.time, &e.word)
		switch e.word {
		case "newagent":
			fmt.Fscan(in, &e.name)
			for k := range e.values {
				fmt.Fscan(in, &e.values[k])
			}
		case "newcar":
			fmt.Fscan(in, &e.name, &e.passed, &e.id)
		default:
			var kind, monsterName string
			fmt.Fscan(in, &kind, &e.q.dist)
			switch kind {
			case "run":
				e.q.kind = run
			case "kill":
				e.q.kind = kill
				fmt.Fscan(in, &monsterName)
				e.q.monster = monsterOf[monsterName]
			default:
				e.q.kind = findout
				if kind == "talk" {
					e.q.kind = talk
				}
				fmt.Fscan(in, &e.q.need, &e.q.mint)
			}
		}
	}
	for next := 0; next < len(outsides) || events.Len() > 0; {
		now := math.MaxInt64
		if next < len(outsides) {
			now = outsides[next].time
		}
		if events.Len() > 0 && events[0].time < now {
			now = events[0].time
		}
		log = log[:0]
		for events.Len() > 0 && events[0].time == now {
			e := heap.Pop(&events).(event)
			p := active[e.num]
			if p == nil {
				continue // a moment that came after the quest had ended
			}
			switch e.kind {
			case broken:
				if c := cars[p.car]; !c.broken {
					c.broken, c.busy, c.passed = true, false, types[c.kind].limit
					log = append(log, message{broken, "Car " + c.id + " was broken."})
				}
			case killed:
				name := monsters[quests[e.num-1].monster].name
				log = append(log, message{killed, teamText(p.team) + " killed monster " + name + "."})
			default:
				finish(e.num)
			}
		}
		if next < len(outsides) && outsides[next].time == now {
			e := outsides[next]
			next++
			switch e.word {
			case "newagent":
				v := e.values
				letter := newLetter(e.name)
				agents = append(agents, &agent{e.name, letter, v[accIdx], v[walkIdx], v[intelIdx],
					v[expIdx], v[driveIdx], false, true})
				log = append(log, message{joined, fmt.Sprintf("New agent %s got a letter %c.", e.name, letter)})
			case "newcar":
				newCar(e.name, e.passed, e.id)
				log = append(log, message{bought, "MIB bought a car of class " + e.name + "."})
			default:
				q := e.q
				quests = append(quests, &q)
			}
		}
		// all quests that can start now, the earliest received first
		for again := true; again; {
			again = false
			for i, q := range quests {
				if q.state == 0 {
					if p := bestPlan(q); p != nil {
						start(i+1, q, p, now)
						again = true
						break
					}
				}
			}
		}
		sort.Slice(log, func(i, j int) bool {
			if log[i].kind != log[j].kind {
				return log[i].kind < log[j].kind
			}
			return log[i].text < log[j].text
		})
		stamp := fmt.Sprintf("%04d:%02d:%02d", now/day, now%day/hour, now%hour)
		for _, m := range log {
			fmt.Fprintf(out, "%s    %s\n", stamp, m.text)
		}
	}
}
