package main

import (
	"fmt"
	"strconv"
	"strings"
)

const (
	digits = 4 // lengths are given to a tenth of a millimetre
	bits   = 64
)

// a length in tenths of a millimetre, read exactly
func tenths(text string) int64 {
	whole, frac := text, ""
	if dot := strings.IndexByte(text, '.'); dot >= 0 {
		whole, frac = text[:dot], text[dot+1:]
	}
	frac = (frac + strings.Repeat("0", digits))[:digits]
	w, _ := strconv.ParseInt("0"+whole, 10, bits)
	f, _ := strconv.ParseInt(frac, 10, bits)
	scale := int64(1)
	for i := 0; i < digits; i++ {
		scale *= 10
	}
	return w*scale + f
}

func main() {
	var n int64
	var sText, railText string
	fmt.Scan(&n, &sText, &railText)
	s, rail := tenths(sText), tenths(railText)
	full, rest := s/rail, s%rail
	if rest == 0 {
		fmt.Println(n * full)
		return
	}
	// each line takes its full rails and a short piece; a rail holds rail / rest such pieces
	perRail := rail / rest
	fmt.Println(n*full + (n+perRail-1)/perRail)
}
