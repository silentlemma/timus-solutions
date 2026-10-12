use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // before[i] is the sum of the first i readings
    let mut before = vec![0i64; n + 1];
    for i in 1..=n {
        before[i] = before[i - 1] + it.next().unwrap();
    }
    let q = it.next().unwrap_or(0);
    let mut out = String::new();
    for _ in 0..q {
        let (i, j) = (it.next().unwrap() as usize, it.next().unwrap() as usize);
        writeln!(out, "{}", before[j] - before[i - 1]).unwrap();
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
