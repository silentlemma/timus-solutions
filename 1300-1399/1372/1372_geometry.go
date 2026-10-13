package main

import (
	"fmt"
	"math"
)

const (
	tiny     = 1e-9 // a torque this small is no torque at all
	turn     = 360.0
	halfUnit = 5e-9 // half of the last printed digit
	degree   = math.Pi / 180
)

const dim = 3

type vec [dim]float64

func unit(lon, lat float64) vec {
	lon, lat = lon*degree, lat*degree
	return vec{math.Cos(lat) * math.Cos(lon), math.Cos(lat) * math.Sin(lon), math.Sin(lat)}
}

func cross(a, b vec) vec {
	return vec{a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]}
}

func dot(a, b vec) float64 { return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] }

func angles(v vec) (float64, float64) {
	length := math.Sqrt(dot(v, v))
	lat := math.Asin(math.Max(-1, math.Min(1, v[2]/length))) / degree
	lon := math.Mod(math.Atan2(v[1], v[0])/degree+turn, turn)
	if lon >= turn-halfUnit {
		lon = 0 // it would print as 360
	}
	return lon + 0, lat + 0 // no negative zeros
}

func main() {
	var radius, mass, mast, thrust float64
	var count int
	fmt.Scan(&radius, &mass, &mast, &thrust, &count)
	arm := radius + mast // the engines sit on masts above the surface
	var torque vec
	for i := 0; i < count; i++ {
		var lon, lat, dlon, dlat float64
		fmt.Scan(&lon, &lat, &dlon, &dlat)
		t := cross(unit(lon, lat), unit(dlon, dlat))
		for k := range torque {
			torque[k] += arm * thrust * t[k]
		}
	}
	size := math.Sqrt(dot(torque, torque))
	if size < tiny {
		fmt.Printf("%.8f %.8f %.8f %.8f %.8f\n", 0.0, 0.0, 0.0, 0.0, 0.0)
		return
	}
	// a force f at p turns the station by p x f, at most |p| |f|; so the
	// least thrust |T| / |p| needs p across the torque T and f = p x T / |p|^2
	axis := vec{torque[0] / size, torque[1] / size, torque[2] / size}
	axes := []vec{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}
	pick := axes[0]
	for _, e := range axes {
		if math.Abs(dot(e, axis)) < math.Abs(dot(pick, axis)) {
			pick = e
		}
	}
	d := dot(pick, axis)
	place := vec{pick[0] - d*axis[0], pick[1] - d*axis[1], pick[2] - d*axis[2]}
	push := cross(place, torque)
	lon, lat := angles(place)
	dlon, dlat := angles(push)
	fmt.Printf("%.8f %.8f %.8f %.8f %.8f\n", lon, lat, dlon, dlat, size/arm)
}
