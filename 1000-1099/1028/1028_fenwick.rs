use std::fmt::Write as _;
use std::io::{self, Read};

const MAX_COORD: usize = 32000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    // stars come by y, then x: the level of a star is the number of stars
    // already seen with x not greater than its own; a Fenwick tree counts them
    let mut tree = vec![0usize; MAX_COORD + 2];
    let mut count = vec![0usize; n];
    for star in v[1..].chunks(2).take(n) {
        let mut j = star[0] + 1;
        let mut level = 0;
        while j > 0 {
            level += tree[j];
            j &= j - 1;
        }
        count[level] += 1;
        let mut j = star[0] + 1;
        while j <= MAX_COORD + 1 {
            tree[j] += 1;
            j += j & j.wrapping_neg();
        }
    }
    let mut out = String::new();
    for c in count {
        writeln!(out, "{}", c).unwrap();
    }
    print!("{}", out);
}
