use std::io::{self, Read};

fn solve(k: i64, m: i64) -> i64 {
    let digits = k.to_string();
    // numbers not longer than k that come no later than k: for each length,
    // those from 10^(l-1) up to the first l digits of k; any N >= k has them
    let (mut before, mut low) = (0i64, 1i64);
    for l in 1..=digits.len() {
        before += digits[..l].parse::<i64>().unwrap() - low + 1;
        low *= 10;
    }
    if m < before {
        return 0;
    }
    // each further number before k is longer than k: of length l it lies in
    // [10^(l-1), k * 10^(l-len(k))), and N is the (m - before)-th of them
    let (mut need, mut top) = (m - before, k * 10);
    if need == 0 {
        return k;
    }
    while top > low {
        if top - low >= need {
            return low + need - 1;
        }
        need -= top - low;
        low *= 10;
        top *= 10;
    }
    // k is a power of ten, and no longer number comes before it
    0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    println!("{}", solve(v[0], v[1]));
}
