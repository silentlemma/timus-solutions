package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

// set records what is known about a set of words: is it non-empty, does it
// hold the empty word, does it hold a non-empty word, is it infinite
type set struct{ any, emptyWord, longWord, infinite bool }

var (
	nothing   = set{}
	emptyWord = set{any: true, emptyWord: true}
	letter    = set{any: true, longWord: true}
)

func unite(x, y set) set {
	return set{x.any || y.any, x.emptyWord || y.emptyWord, x.longWord || y.longWord,
		x.infinite || y.infinite}
}

func concat(x, y set) set {
	if !x.any || !y.any {
		return nothing
	}
	return set{true, x.emptyWord && y.emptyWord, x.longWord || y.longWord, x.infinite || y.infinite}
}

// star: repeating a non-empty word gives ever longer words
func star(x set) set {
	return set{true, true, x.longWord, x.longWord}
}

// frame is one level of brackets: the union so far, the concatenation so far
// and the last symbol, which a star may still apply to
type frame struct {
	all, cat, last set
	hasLast        bool
}

func (f *frame) close() set {
	if f.hasLast {
		return unite(f.all, concat(f.cat, f.last))
	}
	return unite(f.all, f.cat)
}

func (f *frame) push(symbol set) {
	if f.hasLast {
		f.cat = concat(f.cat, f.last)
	}
	f.last, f.hasLast = symbol, true
}

func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	frames := []*frame{{all: nothing, cat: emptyWord}}
	for _, c := range text {
		f := frames[len(frames)-1]
		switch {
		case c == '(':
			frames = append(frames, &frame{all: nothing, cat: emptyWord})
		case c == ')':
			frames = frames[:len(frames)-1]
			frames[len(frames)-1].push(f.close())
		case c == '|':
			f.all, f.cat, f.hasLast = f.close(), emptyWord, false
		case c == '*':
			f.last = star(f.last)
		case c == '0':
			f.push(nothing)
		case c >= 'a' && c <= 'z':
			f.push(letter)
		}
	}
	if frames[0].close().infinite {
		fmt.Println("N")
	} else {
		fmt.Println("F")
	}
}
