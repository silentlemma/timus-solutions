package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"strconv"
	"strings"
)

const (
	radius     = 6875.0 / 2
	danger     = 100.0
	minutes    = 60
	seconds    = 3600
	hundredths = 100
	parts      = 3
	bitSize    = 64

	radiansPerDegree = math.Pi / 180
)

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	text := strings.NewReplacer("^", " ", "'", " ", "\"", " ").Replace(string(data))
	tokens := strings.Fields(text)
	// every coordinate is "degrees minutes seconds" followed by NL, SL, EL or WL
	var angle []float64
	for i := parts; i < len(tokens); i++ {
		t := tokens[i]
		if len(t) < 2 || t[1] != 'L' || !strings.ContainsRune("NSEW", rune(t[0])) {
			continue
		}
		d, _ := strconv.ParseFloat(tokens[i-parts], bitSize)
		m, _ := strconv.ParseFloat(tokens[i-2], bitSize)
		s, _ := strconv.ParseFloat(tokens[i-1], bitSize)
		degrees := d + m/minutes + s/seconds
		if t[0] == 'S' || t[0] == 'W' {
			degrees = -degrees
		}
		angle = append(angle, degrees*radiansPerDegree)
	}
	lat1, lon1, lat2, lon2 := angle[0], angle[1], angle[2], angle[len(angle)-1]
	// the haversine formula keeps its precision for small distances
	h := math.Pow(math.Sin((lat2-lat1)/2), 2) +
		math.Cos(lat1)*math.Cos(lat2)*math.Pow(math.Sin((lon2-lon1)/2), 2)
	distance := 2 * radius * math.Asin(math.Min(1, math.Sqrt(h)))
	fmt.Printf("The distance to the iceberg: %.2f miles.\n", distance)
	// the comparison uses the printed value: 99.996 is printed as 100.00
	if math.Round(distance*hundredths) < danger*hundredths {
		fmt.Println("DANGER!")
	}
}
