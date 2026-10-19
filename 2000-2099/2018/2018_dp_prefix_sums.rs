use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

fn solve(n: usize, a: usize, b: usize) -> u64 {
    let mut ends_one = vec![0u64; b + 1];
    let mut ends_two = vec![0u64; a + 1];
    ends_one[0] = 1;
    ends_two[0] = 1;
    let (mut window_one, mut window_two) = (1, 1);
    let (mut last_one, mut last_two) = (0, 0);
    for length in 1..=n {
        last_one = window_one;
        last_two = window_two;
        let expired_two = if length >= a {
            ends_two[(length - a) % (a + 1)]
        } else {
            0
        };
        let expired_one = if length >= b {
            ends_one[(length - b) % (b + 1)]
        } else {
            0
        };
        window_one = (window_one + last_two + MOD - expired_two) % MOD;
        window_two = (window_two + last_one + MOD - expired_one) % MOD;
        ends_one[length % (b + 1)] = last_one;
        ends_two[length % (a + 1)] = last_two;
    }
    (last_one + last_two) % MOD
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let n = tokens.next().unwrap();
    let a = tokens.next().unwrap();
    let b = tokens.next().unwrap();
    println!("{}", solve(n, a, b));
}
