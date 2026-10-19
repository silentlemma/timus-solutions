package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
)

const snapshotAge = 60

type input struct {
	data []byte
	at   int
}

func (in *input) number() int64 {
	for in.at < len(in.data) && in.data[in.at] <= ' ' {
		in.at++
	}
	sign := int64(1)
	if in.data[in.at] == '-' {
		sign = -1
		in.at++
	}
	var value int64
	for in.at < len(in.data) && in.data[in.at] > ' ' {
		value = value*10 + int64(in.data[in.at]-'0')
		in.at++
	}
	return sign * value
}

type point struct {
	x, y int64
}

func rotatePolygon(points []point) []point {
	start := 0
	for i, p := range points {
		if p.y < points[start].y || (p.y == points[start].y && p.x < points[start].x) {
			start = i
		}
	}
	result := make([]point, 0, len(points)+1)
	result = append(result, points[start:]...)
	result = append(result, points[:start]...)
	return append(result, result[0])
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n, m := int(in.number()), int(in.number())
	airport, cloud := make([]point, n), make([]point, m)
	for i := range airport {
		airport[i] = point{in.number(), in.number()}
	}
	for i := range cloud {
		cloud[i] = point{-in.number(), -in.number()}
	}
	airport, cloud = rotatePolygon(airport), rotatePolygon(cloud)
	x, y := airport[0].x+cloud[0].x, airport[0].y+cloud[0].y
	i, j := 0, 0
	distance := math.Inf(1)
	for i < n || j < m {
		var ax, ay, bx, by int64
		if i < n {
			ax, ay = airport[i+1].x-airport[i].x, airport[i+1].y-airport[i].y
		}
		if j < m {
			bx, by = cloud[j+1].x-cloud[j].x, cloud[j+1].y-cloud[j].y
		}
		turn := ax*by - ay*bx
		takeAirport := i < n && (j == m || turn >= 0)
		takeCloud := j < m && (i == n || turn <= 0)
		var dx, dy int64
		if takeAirport {
			dx, dy = ax, ay
			i++
		}
		if takeCloud {
			dx, dy = dx+bx, dy+by
			j++
		}
		// Integer cross products avoid cancellation for nearly parallel coordinates.
		candidate := float64(x*dy-y*dx) / math.Hypot(float64(dx), float64(dy))
		distance = math.Min(distance, candidate)
		x, y = x+dx, y+dy
	}
	fmt.Printf("%.10f\n", math.Max(0, distance-snapshotAge))
}
