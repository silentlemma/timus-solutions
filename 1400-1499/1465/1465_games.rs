use std::collections::HashSet;
use std::io::{self, Read};

const LIMIT: i64 = 200; // the values repeat with PERIOD from 52 on, well below this
const PERIOD: i64 = 34;
const TAKE: usize = 3; // a move takes up to three files out of play

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut n: i64 = input.trim().parse().unwrap();
    // Dawson's chess: a row of n files plays like the octal game 0.137, where
    // a move takes one file (only if it is all), two (leaving one row) or three
    // (leaving up to two rows); White, moving first, wins when the value is not 0
    let limit = LIMIT as usize;
    let mut g = vec![0usize; limit + 1];
    for size in 1..=limit {
        let mut seen = HashSet::new();
        if size == 1 {
            seen.insert(0);
        }
        if size >= 2 {
            seen.insert(g[size - 2]);
        }
        if size >= TAKE {
            for left in 0..=size - TAKE {
                seen.insert(g[left] ^ g[size - TAKE - left]);
            }
        }
        while seen.contains(&g[size]) {
            g[size] += 1;
        }
    }
    if n > LIMIT {
        n = LIMIT - PERIOD + (n - LIMIT) % PERIOD;
    }
    println!("{}", if g[n as usize] != 0 { "White" } else { "Black" });
}
