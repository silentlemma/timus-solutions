use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let mut out = String::new();
    // g(n) = n by induction, so f(n) = 1 + sum of i f(i) = n f(n - 1) = n!
    for case in v.chunks(2) {
        let (n, p) = (case[0], case[1]);
        if n == 0 && p == 0 {
            break;
        }
        let mut r = if n >= p { 0 } else { 1 }; // when n >= p, p itself is a factor of n!
        let mut i = 2;
        while i <= n && r != 0 {
            r = r * i % p;
            i += 1;
        }
        writeln!(out, "{}", r).unwrap();
    }
    print!("{}", out);
}
