package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	scale      = 100 // coordinates have at most two decimals
	digits     = 2
	volumeCent = scale * scale // a hundredth of a volume unit, counted in 1 / scale^3
)

type point struct{ y, z int64 }

func scaled(token string) int64 {
	whole, frac := token, ""
	if dot := strings.IndexByte(token, '.'); dot >= 0 {
		whole, frac = token[:dot], token[dot+1:]
	}
	frac = (frac + "00")[:digits]
	w, _ := strconv.Atoi("0" + whole)
	f, _ := strconv.Atoi(frac)
	return int64(w)*scale + int64(f)
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() string {
		in.Scan()
		return in.Text()
	}
	u, v, w := scaled(next()), scaled(next()), scaled(next())
	n, _ := strconv.Atoi(next())
	var px, py, pz []int64
	for i := 0; i < n; i++ {
		x, y, z := scaled(next()), scaled(next()), scaled(next())
		// a point outside A can never be inside G
		if x <= u && y <= v && z <= w {
			px, py, pz = append(px, x), append(py, y), append(pz, z)
		}
	}
	n = len(px)
	xs := map[int64]bool{0: true, u: true}
	for _, x := range px {
		xs[x] = true
	}
	var xList []int64
	for x := range xs {
		xList = append(xList, x)
	}
	sort.Slice(xList, func(a, b int) bool { return xList[a] < xList[b] })
	var best int64
	for i := range xList {
		for j := len(xList) - 1; j > i; j-- {
			x1, x2 := xList[i], xList[j]
			width := x2 - x1
			if width*v*w <= best {
				break // the remaining x2 are closer still
			}
			var inside []point
			for p := 0; p < n; p++ {
				if x1 < px[p] && px[p] < x2 {
					inside = append(inside, point{py[p], pz[p]})
				}
			}
			sort.Slice(inside, func(a, b int) bool { return inside[a].y < inside[b].y })
			m := len(inside)
			// the lower y face lies on the floor or on a point; the upper
			// face sweeps down from the top, and every point it passes
			// leaves the slab, so neighbouring z gaps merge into one
			for k := -1; k < m; k++ {
				var y1 int64
				if k >= 0 {
					y1 = inside[k].y
				}
				if width*(v-y1)*w <= best {
					break
				}
				zs := []int64{0, w}
				for q := k + 1; q < m; q++ {
					// a point on the floor or the ceiling never splits a gap
					if z := inside[q].z; 0 < z && z < w {
						zs = append(zs, z)
					}
				}
				sort.Slice(zs, func(a, b int) bool { return zs[a] < zs[b] })
				prev, nxt := make([]int, len(zs)), make([]int, len(zs))
				var gap int64
				for t := range zs {
					prev[t], nxt[t] = t-1, t+1
					if t > 0 {
						gap = max(gap, zs[t]-zs[t-1])
					}
				}
				y2 := v
				for q := m - 1; q > k; q-- {
					best = max(best, width*(y2-y1)*gap)
					y2 = inside[q].y
					z := inside[q].z
					if z <= 0 || z >= w {
						continue
					}
					t := sort.Search(len(zs), func(s int) bool { return zs[s] >= z })
					lo, hi := prev[t], nxt[t]
					nxt[lo], prev[hi] = hi, lo
					gap = max(gap, zs[hi]-zs[lo])
				}
				best = max(best, width*(y2-y1)*gap)
			}
		}
	}
	cents := (best + volumeCent/2) / volumeCent
	fmt.Printf("%d.%02d\n", cents/scale, cents%scale)
}
