use std::fmt::Write;
use std::io::{self, Read};

const HORIZON: usize = 25;
const ALPHABET_SIZE: usize = 2;
const UNREACHABLE: i32 = -1;

struct Solver {
    text: Vec<usize>,
    border: Vec<usize>,
    rank: Vec<i32>,
    answer: [i32; HORIZON + 1],
    split: usize,
}

impl Solver {
    fn new() -> Self {
        Self {
            text: Vec::new(),
            border: vec![0],
            rank: vec![0],
            answer: [0; HORIZON + 1],
            split: 0,
        }
    }

    fn append(&mut self, symbol: usize) -> i32 {
        let length = self.text.len();
        let mut matched = self.border[length];
        while matched > 0 && self.text[matched] != symbol {
            matched = self.border[matched];
        }
        if length > 0 && self.text[matched] == symbol {
            matched += 1;
        }
        self.text.push(symbol);
        self.border.push(matched);
        let period = length + 1 - matched;
        let previous_period = matched - self.border[matched];
        self.rank
            .push(self.rank[matched] + i32::from(period != previous_period));
        self.rank[matched]
    }

    fn relax(values: &mut [i32], active: &mut Vec<usize>, target: usize, value: i32) {
        if values[target] == UNREACHABLE {
            active.push(target);
        }
        values[target] = values[target].max(value);
    }

    fn solve_tail(&mut self, score: i32) {
        let length = self.text.len();
        let remaining = HORIZON - self.split;
        let mut transition = vec![[0; ALPHABET_SIZE]; length];
        for state in 0..length {
            for symbol in 0..ALPHABET_SIZE {
                transition[state][symbol] = if self.text[state] == symbol {
                    state + 1
                } else if state > 0 {
                    transition[self.border[state]][symbol]
                } else {
                    0
                };
            }
        }

        let mut periods = Vec::new();
        let mut state = self.border[length];
        while length - state <= remaining {
            periods.push(length - state);
            if state == 0 {
                break;
            }
            state = self.border[state];
        }

        // A border reaching the fixed prefix follows one of these periodic paths.
        let mut seeds = vec![Vec::new(); remaining + 1];
        for period in periods {
            let mut path_score = score;
            for step in 1..=remaining {
                let symbol = self.text[(length + step - 1) % period];
                let mut matched = *self.border.last().unwrap();
                if matched >= length {
                    let other = 1 - symbol;
                    while matched >= length && self.text[matched] != other {
                        matched = self.border[matched];
                    }
                    matched = if matched < length {
                        transition[matched][other]
                    } else {
                        matched + 1
                    };
                    if matched < length {
                        seeds[step].push((matched, path_score + self.rank[matched]));
                    }
                }
                path_score += self.append(symbol);
                let index = self.split + step;
                self.answer[index] = self.answer[index].max(path_score);
            }
            self.text.truncate(length);
            self.border.truncate(length + 1);
            self.rank.truncate(length + 1);
        }

        let mut best = vec![UNREACHABLE; length];
        let mut next = vec![UNREACHABLE; length];
        let mut active = vec![self.border[length]];
        let mut next_active = Vec::new();
        best[self.border[length]] = score;
        for step in 1..=remaining {
            next_active.clear();
            for &current in &active {
                for symbol in 0..ALPHABET_SIZE {
                    let target = transition[current][symbol];
                    if target < length {
                        let value = best[current] + self.rank[target];
                        Self::relax(&mut next, &mut next_active, target, value);
                    }
                }
            }
            for &(target, value) in &seeds[step] {
                Self::relax(&mut next, &mut next_active, target, value);
            }
            for &current in &active {
                best[current] = UNREACHABLE;
            }
            std::mem::swap(&mut best, &mut next);
            std::mem::swap(&mut active, &mut next_active);
            let index = self.split + step;
            for &current in &active {
                self.answer[index] = self.answer[index].max(best[current]);
            }
        }
    }

    fn search(&mut self, depth: usize, score: i32) {
        if depth == self.split {
            self.solve_tail(score);
            return;
        }
        for symbol in 0..ALPHABET_SIZE {
            let next_score = score + self.append(symbol);
            self.answer[depth + 1] = self.answer[depth + 1].max(next_score);
            self.search(depth + 1, next_score);
            self.text.pop();
            self.border.pop();
            self.rank.pop();
        }
    }

    fn run(&mut self, input: &str) -> String {
        let mut score = 0;
        for symbol in input.bytes() {
            if symbol == b'X' || symbol == b'.' {
                score += self.append(usize::from(symbol == b'X'));
            }
        }
        self.split = (HORIZON + 1).saturating_sub(self.text.len()) / 2;
        self.search(0, score);
        let mut output = String::new();
        for step in 1..=HORIZON {
            writeln!(output, "{}", self.answer[step]).unwrap();
        }
        output
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut solver = Solver::new();
    print!("{}", solver.run(&input));
}
