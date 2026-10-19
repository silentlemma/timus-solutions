package main

import (
	"bufio"
	"fmt"
	"os"
)

var streets = []string{"preflop", "flop", "turn", "river"}

type game struct {
	stack      []int
	bet        []int
	folded     []bool
	pending    []bool
	dealer     int
	cursor     int
	street     int
	currentBet int
}

func smaller(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func (g *game) resetPending() {
	for i := range g.stack {
		g.pending[i] = !g.folded[i] && g.stack[i] > 0
	}
}

func (g *game) act(player, paid int, fold bool) {
	g.stack[player] -= paid
	g.bet[player] += paid
	if fold {
		g.folded[player] = true
	}
	if g.bet[player] > g.currentBet {
		g.currentBet = g.bet[player]
		g.resetPending()
	}
	g.pending[player] = false
	g.cursor = (player + 1) % len(g.stack)
}

func (g *game) deal() {
	g.street++
	g.currentBet = 0
	for i := range g.bet {
		g.bet[i] = 0
	}
	g.resetPending()
	g.cursor = (g.dealer + 1) % len(g.stack)
}

func (g *game) nextPlayer() int {
	for offset := range g.stack {
		player := (g.cursor + offset) % len(g.stack)
		if g.pending[player] && !g.folded[player] && g.stack[player] > 0 {
			return player
		}
	}
	return -1
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var smallBlind, bigBlind, ante, count, dealer, bot int
	if _, err := fmt.Fscan(in, &smallBlind, &bigBlind, &ante); err != nil {
		return
	}
	fmt.Fscan(in, &count, &dealer, &bot)
	dealer--
	bot--
	var targetName string
	fmt.Fscan(in, &targetName)
	target := 0
	for i, name := range streets {
		if name == targetName {
			target = i
		}
	}
	names := make([]string, count)
	indices := make(map[string]int)
	g := game{
		stack: make([]int, count), bet: make([]int, count),
		folded: make([]bool, count), pending: make([]bool, count), dealer: dealer,
	}
	for i := range names {
		fmt.Fscan(in, &names[i], &g.stack[i])
		indices[names[i]] = i
		g.stack[i] -= smaller(g.stack[i], ante)
	}
	small := (dealer + 1) % count
	if count == 2 {
		small = dealer
	}
	big := (small + 1) % count
	g.bet[small] = smaller(g.stack[small], smallBlind)
	g.stack[small] -= g.bet[small]
	g.bet[big] = smaller(g.stack[big], bigBlind)
	g.stack[big] -= g.bet[big]
	g.currentBet = bigBlind
	g.cursor = (big + 1) % count
	g.resetPending()

	var known int
	fmt.Fscan(in, &known)
	for action := 0; action < known; action++ {
		var name, kind string
		fmt.Fscan(in, &name, &kind)
		if name == "dealing" {
			g.deal()
			continue
		}
		player := indices[name]
		paid := 0
		switch kind {
		case "calls", "bets":
			fmt.Fscan(in, &paid)
		case "raises":
			var increase, total int
			var separator string
			fmt.Fscan(in, &increase, &separator, &total)
			paid = total - g.bet[player]
		}
		g.act(player, paid, kind == "folds")
	}
	finalStack := make([]int, count)
	for i := range finalStack {
		fmt.Fscan(in, &finalStack[i])
	}

	answer := make([]string, 0)
	for {
		player := g.nextPlayer()
		if player < 0 {
			g.deal()
			answer = append(answer, "dealing "+streets[g.street])
			continue
		}
		if player == bot && g.street == target {
			matches := true
			for i := range g.stack {
				if g.stack[i] != finalStack[i] {
					matches = false
				}
			}
			if matches {
				break
			}
		}
		paid := g.stack[player] - finalStack[player]
		// Before the next street, only the bot can spend beyond the current bet.
		if g.street != target && player != bot {
			paid = smaller(paid, g.currentBet-g.bet[player])
		}
		fold := false
		var action string
		switch {
		case paid == 0:
			fold = g.bet[player] < g.currentBet
			if fold {
				action = fmt.Sprintf("%s folds", names[player])
			} else {
				action = fmt.Sprintf("%s checks", names[player])
			}
		case g.currentBet == 0:
			action = fmt.Sprintf("%s bets %d", names[player], paid)
		case g.bet[player]+paid > g.currentBet:
			total := g.bet[player] + paid
			action = fmt.Sprintf("%s raises %d to %d", names[player], total-g.currentBet, total)
		default:
			action = fmt.Sprintf("%s calls %d", names[player], paid)
		}
		answer = append(answer, action)
		g.act(player, paid, fold)
	}
	fmt.Fprintln(out, len(answer))
	for _, action := range answer {
		fmt.Fprintln(out, action)
	}
}
