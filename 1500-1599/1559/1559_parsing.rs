use std::io::{self, Read};

/// What is known about a set of words: is it non-empty, does it hold the
/// empty word, does it hold a non-empty word, is it infinite.
#[derive(Clone, Copy)]
struct Set {
    any: bool,
    empty_word: bool,
    long_word: bool,
    infinite: bool,
}

const NOTHING: Set = Set {
    any: false,
    empty_word: false,
    long_word: false,
    infinite: false,
};
const EMPTY_WORD: Set = Set {
    any: true,
    empty_word: true,
    long_word: false,
    infinite: false,
};
const LETTER: Set = Set {
    any: true,
    empty_word: false,
    long_word: true,
    infinite: false,
};

fn unite(x: Set, y: Set) -> Set {
    Set {
        any: x.any || y.any,
        empty_word: x.empty_word || y.empty_word,
        long_word: x.long_word || y.long_word,
        infinite: x.infinite || y.infinite,
    }
}

fn concat(x: Set, y: Set) -> Set {
    if !x.any || !y.any {
        return NOTHING;
    }
    Set {
        any: true,
        empty_word: x.empty_word && y.empty_word,
        long_word: x.long_word || y.long_word,
        infinite: x.infinite || y.infinite,
    }
}

/// Repeating a non-empty word gives ever longer words.
fn star(x: Set) -> Set {
    Set {
        any: true,
        empty_word: true,
        long_word: x.long_word,
        infinite: x.long_word,
    }
}

/// One level of brackets: the union so far, the concatenation so far and the
/// last symbol, which a star may still apply to.
struct Frame {
    all: Set,
    cat: Set,
    last: Option<Set>,
}

impl Frame {
    fn new() -> Frame {
        Frame {
            all: NOTHING,
            cat: EMPTY_WORD,
            last: None,
        }
    }

    fn close(&self) -> Set {
        unite(
            self.all,
            self.last.map_or(self.cat, |l| concat(self.cat, l)),
        )
    }

    fn push(&mut self, symbol: Set) {
        if let Some(l) = self.last {
            self.cat = concat(self.cat, l);
        }
        self.last = Some(symbol);
    }
}

fn main() {
    let mut text = Vec::new();
    io::stdin().read_to_end(&mut text).unwrap();
    let mut frames = vec![Frame::new()];
    for &c in &text {
        match c {
            b'(' => frames.push(Frame::new()),
            b')' => {
                let value = frames.pop().unwrap().close();
                frames.last_mut().unwrap().push(value);
            }
            b'|' => {
                let frame = frames.last_mut().unwrap();
                frame.all = frame.close();
                frame.cat = EMPTY_WORD;
                frame.last = None;
            }
            b'*' => {
                let frame = frames.last_mut().unwrap();
                frame.last = frame.last.map(star);
            }
            b'0' => frames.last_mut().unwrap().push(NOTHING),
            b'a'..=b'z' => frames.last_mut().unwrap().push(LETTER),
            _ => {}
        }
    }
    println!("{}", if frames[0].close().infinite { "N" } else { "F" });
}
