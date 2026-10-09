use std::io::{self, Read};

const DIGITS: usize = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let half = n / 2;
    let limit = DIGITS.pow(half as u32);
    // ways[s]: how many halves (numbers below 10^half) have digit sum s
    let mut ways = vec![0u64; (DIGITS - 1) * half + 1];
    for x in 0..limit {
        let (mut s, mut y) = (0, x);
        while y > 0 {
            s += y % DIGITS;
            y /= DIGITS;
        }
        ways[s] += 1;
    }
    // the two halves are chosen independently with the same sum
    let total: u64 = ways.iter().map(|w| w * w).sum();
    println!("{}", total);
}
