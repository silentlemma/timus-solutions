package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const edge = 1000000000

type point struct{ x, y int64 }

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(reader, &n, &k)
	candles := make([]point, n)
	for i := range candles {
		fmt.Fscan(reader, &candles[i].x, &candles[i].y)
	}
	sort.Slice(candles, func(i, j int) bool {
		if candles[i].x != candles[j].x {
			return candles[i].x < candles[j].x
		}
		return candles[i].y < candles[j].y
	})
	// take the first k candles from the left, ties broken from below: all
	// columns left of candle k, and its own column up to it; the cut from it
	// to (x - 1, edge) leaves the rest of its column outside
	t := candles[k-1]
	polygon := []point{{-edge, -edge}, {t.x, -edge}, {t.x, t.y}}
	if t.x-1 > -edge {
		polygon = append(polygon, point{t.x - 1, edge})
	}
	polygon = append(polygon, point{-edge, edge})
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprintln(writer, len(polygon))
	for _, p := range polygon {
		fmt.Fprintln(writer, p.x, p.y)
	}
}
