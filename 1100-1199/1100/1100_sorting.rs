use std::fmt::Write as _;
use std::io::{self, Read, Write};

const MOST: usize = 100;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u32>().unwrap());
    let n = it.next().unwrap() as usize;
    // bubble sort never swaps equal scores, so teams with the same score keep
    // their input order: a counting sort by score does the same
    let mut buckets: Vec<Vec<u32>> = vec![Vec::new(); MOST + 1];
    for _ in 0..n {
        let team = it.next().unwrap();
        let solved = it.next().unwrap() as usize;
        buckets[solved].push(team);
    }
    let mut out = String::new();
    for solved in (0..=MOST).rev() {
        for team in &buckets[solved] {
            writeln!(out, "{} {}", team, solved).unwrap();
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
