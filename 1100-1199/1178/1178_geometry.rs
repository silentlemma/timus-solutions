use std::fmt::Write;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let at = |i: usize| (v[2 * i - 1], v[2 * i]);
    let mut cities: Vec<usize> = (1..=n).collect();
    cities.sort_by_key(|&i| at(i));
    // neighbours in (x, y) order: each road lies in its own strip of x, and
    // two roads can share only the border line, where they end at different
    // cities because no three cities are on one line
    let mut out = String::new();
    for pair in cities.chunks(2) {
        writeln!(out, "{} {}", pair[0], pair[1]).unwrap();
    }
    print!("{}", out);
}
