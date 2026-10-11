use std::fmt::Write as _;
use std::io::{self, Read, Write};

const MAX_N: usize = 200;
// state i (1 to MAX_N+1) stands on cell i of the minuses; state SEEK+d
// still has to move d cells to the left before reaching the survivor
const SEEK: usize = 300;
// states that cross the minuses to the right of the survivor, walk back
// over it, cross those to its left and return to it
const RIGHT: usize = 600;
const BACK: usize = 601;
const LEFT: usize = 602;
const RETURNED: usize = 603;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let k: usize = input.trim().parse().unwrap();
    let mut rules = String::new();
    let mut count = 0;
    let mut rule = |state: usize, read: char, next: usize, write: char, mv: char| {
        writeln!(rules, "{} {} {} {} {}", state, read, next, write, mv).unwrap();
        count += 1;
    };
    // survivor = 0-based position of the minus that stays out of n, by the
    // Josephus recurrence
    let mut survivor = 0;
    for n in 1..=MAX_N {
        survivor = (survivor + k) % n;
        rule(n, '-', n + 1, '-', '>');
        // the head stands on the # after n minuses and moves onto cell n
        rule(n + 1, '#', SEEK + n - 1 - survivor, '#', '<');
    }
    for d in 1..MAX_N {
        rule(SEEK + d, '-', SEEK + d - 1, '-', '<');
    }
    rule(SEEK, '-', RIGHT, '-', '>');
    rule(RIGHT, '-', RIGHT, '+', '>');
    rule(RIGHT, '+', RIGHT, '+', '>');
    rule(RIGHT, '#', BACK, '#', '<');
    rule(BACK, '+', BACK, '+', '<');
    rule(BACK, '-', LEFT, '-', '<');
    rule(LEFT, '-', LEFT, '+', '<');
    rule(LEFT, '+', LEFT, '+', '<');
    rule(LEFT, '#', RETURNED, '#', '>');
    rule(RETURNED, '+', RETURNED, '+', '>');
    let mut out = io::stdout();
    write!(out, "{}\n{}", count, rules).unwrap();
}
