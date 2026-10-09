use std::io::{self, Read};

fn digits(mut v: u64, base: u64) -> Vec<u64> {
    let mut out = Vec::new();
    while v > 0 {
        out.push(v % base);
        v /= base;
    }
    out.reverse();
    out
}

fn fits(x: u64, y: u64, base: u64) -> bool {
    let dy = digits(y, base);
    let mut j = 0;
    for d in digits(x, base) {
        if j < dy.len() && d == dy[j] {
            j += 1;
        }
    }
    j == dy.len()
}

fn answer(x: u64, y: u64) -> Option<u64> {
    let mut base = 2;
    while base * base <= x {
        if fits(x, y, base) {
            return Some(base);
        }
        base += 1;
    }
    // from here on x has two digits x / b and x % b, and y must be one of them
    let mut best: Option<u64> = None;
    let low = base.max(x / (y + 1) + 1);
    if low <= x / y {
        best = Some(low);
    }
    // x % b == y means that b divides x - y and is larger than y
    let least = base.max(y + 1);
    let n = x - y;
    let mut d = 1;
    while d * d <= n {
        if n % d == 0 {
            for b in [d, n / d] {
                if b >= least && best.map_or(true, |c| b < c) {
                    best = Some(b);
                }
            }
        }
        d += 1;
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    match answer(v[0], v[1]) {
        Some(b) => println!("{}", b),
        None => println!("No solution"),
    }
}
