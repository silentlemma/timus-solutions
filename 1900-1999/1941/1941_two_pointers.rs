use std::io::{self, Read};

const LOWEST_SYMBOL: usize = 33;
const SYMBOL_COUNT: usize = 90;
const ALPHABET_SIZE: usize = SYMBOL_COUNT * SYMBOL_COUNT * SYMBOL_COUNT;

fn encode(token: &str) -> usize {
    let bytes = token.as_bytes();
    ((bytes[0] as usize - LOWEST_SYMBOL) * SYMBOL_COUNT + bytes[1] as usize - LOWEST_SYMBOL)
        * SYMBOL_COUNT
        + bytes[2] as usize
        - LOWEST_SYMBOL
}

struct WindowCounter {
    deficit: Vec<i32>,
    ring: Vec<usize>,
    missing: usize,
    position: usize,
    used: usize,
}

impl WindowCounter {
    fn new(pattern: &[usize]) -> Self {
        let mut deficit = vec![0; ALPHABET_SIZE];
        for &code in pattern {
            deficit[code] += 1;
        }
        Self {
            deficit,
            ring: vec![0; pattern.len()],
            missing: pattern.len(),
            position: 0,
            used: 0,
        }
    }

    fn push(&mut self, code: usize) -> bool {
        if self.used == self.ring.len() {
            let old = self.ring[self.position];
            if self.deficit[old] >= 0 {
                self.missing += 1;
            }
            self.deficit[old] += 1;
        } else {
            self.used += 1;
        }
        if self.deficit[code] > 0 {
            self.missing -= 1;
        }
        self.deficit[code] -= 1;
        self.ring[self.position] = code;
        self.position += 1;
        if self.position == self.ring.len() {
            self.position = 0;
        }
        self.missing == 0
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let (first, text) = input.split_once('\n').unwrap();
    let pattern: Vec<usize> = first.split_whitespace().map(encode).collect();
    let mut counter = WindowCounter::new(&pattern);
    let answer = text
        .split_whitespace()
        .filter(|token| counter.push(encode(token)))
        .count();
    println!("{}", answer);
}
