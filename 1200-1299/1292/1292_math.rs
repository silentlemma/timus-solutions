use std::io::{self, BufWriter, Read, Write};

const FIXED: i64 = 153; // 1 + 125 + 27: every multiple of 3 ends here
const TEN: i64 = 10;

fn cubes(mut x: i64) -> i64 {
    let mut s = 0;
    while x > 0 {
        let d = x % TEN;
        s += d * d * d;
        x /= TEN;
    }
    s
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let t = it.next().unwrap();
    let mut out = BufWriter::new(io::stdout().lock());
    for _ in 0..t {
        let (n, k, l) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
        // the gap before base N is F applied N - 1 times to K; from a
        // multiple of 3 it reaches 153 within 14 steps and stays there
        let mut gap = k;
        let mut step = 0;
        while step < n - 1 && gap != FIXED {
            gap = cubes(gap);
            step += 1;
        }
        writeln!(out, "{}", gap - l).unwrap();
    }
}
