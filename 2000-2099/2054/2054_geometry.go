package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	longMonth    = 31
	shortMonth   = 30
	february     = 28
	solsticeDay  = 171
	hoursPerDay  = 24
	hoursPerYear = 8760
	noon         = 12
	halfTurn     = 180
	tiltDegrees  = 23.439281
)

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	months := [...]string{
		"jan", "feb", "mar", "apr", "may", "jun",
		"jul", "aug", "sep", "oct", "nov", "dec",
	}
	lengths := [...]int{
		longMonth, february, longMonth, shortMonth, longMonth, shortMonth,
		longMonth, longMonth, shortMonth, longMonth, shortMonth, longMonth,
	}
	prefix := make(map[string]int)
	days := 0
	for index, month := range months {
		prefix[month] = days
		days += lengths[index]
	}
	var latitude float64
	var count int
	fmt.Fscan(input, &latitude, &count)
	radians := math.Pi / halfTurn
	latitude *= radians
	tilt := tiltDegrees * radians
	equatorial := math.Cos(latitude) * math.Cos(tilt)
	transverse := math.Cos(latitude)
	axial := math.Sin(latitude) * math.Sin(tilt)
	for ; count > 0; count-- {
		var day, hour int
		var month string
		fmt.Fscan(input, &day, &month, &hour)
		elapsed := (prefix[month]+day-1-solsticeDay)*hoursPerDay + hour - noon
		orbit := 2 * math.Pi * float64(elapsed) / hoursPerYear
		spin := orbit + 2*math.Pi*float64(hour-noon)/hoursPerDay
		sine := equatorial*math.Cos(spin)*math.Cos(orbit) +
			transverse*math.Sin(spin)*math.Sin(orbit) + axial*math.Cos(orbit)
		angle := math.Asin(math.Max(0, math.Min(1, sine))) / radians
		fmt.Fprintf(output, "%.10f\n", angle)
	}
}
