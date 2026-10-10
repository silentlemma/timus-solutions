use std::io::{self, Read};

// answers above this are reported as 0
const LIMIT: usize = 10000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (m, n, k) = (v[0], v[1], v[2]);
    // x tiles make one rectangle per divisor pair a * b = x with a <= b, that
    // is half the number of divisors, rounded up
    let mut divisors = vec![0; LIMIT + 1];
    for d in 1..=LIMIT {
        for x in (d..=LIMIT).step_by(d) {
            divisors[x] += 1;
        }
    }
    let shapes = |x: usize| (divisors[x] + 1) / 2;
    let answer = (k + 1..=LIMIT)
        .find(|&t| shapes(t) == n && shapes(t - k) == m)
        .unwrap_or(0);
    println!("{}", answer);
}
