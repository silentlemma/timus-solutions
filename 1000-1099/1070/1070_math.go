package main

import "syscall"

const (
	hour         = 60
	day          = 24 * hour
	decimal      = 10
	clockSize    = len("HH.MM")
	minuteOffset = len("HH.")
	flightClocks = 4
	readSize     = 64
)

func main() {
	var buffer [readSize]byte
	var clocks [flightClocks]int
	var digits [clockSize]byte
	index, width := 0, 0
	for index < len(clocks) {
		size, err := syscall.Read(syscall.Stdin, buffer[:])
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return
		}
		for _, c := range buffer[:size] {
			if width == 0 && c <= ' ' {
				continue
			}
			digits[width] = c
			width++
			if width == clockSize {
				h := int(digits[0]-'0')*decimal + int(digits[1]-'0')
				m := int(digits[minuteOffset]-'0')*decimal + int(digits[minuteOffset+1]-'0')
				clocks[index] = h*hour + m
				index++
				width = 0
				if index == len(clocks) {
					break
				}
			}
		}
	}
	first := clocks[1] - clocks[0]
	second := clocks[flightClocks-1] - clocks[flightClocks-2]
	difference := first - second
	// Wrap the difference to half a day. It is twice the shift, up to
	// ten minutes of flight-time imbalance.
	centered := ((difference+day/2)%day+day)%day - day/2
	if centered < 0 {
		centered = -centered
	}
	shift := (centered + hour) / (2 * hour)
	answer := [2]byte{'0' + byte(shift), '\n'}
	for output := answer[:]; len(output) > 0; {
		n, err := syscall.Write(syscall.Stdout, output)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		output = output[n:]
	}
}
