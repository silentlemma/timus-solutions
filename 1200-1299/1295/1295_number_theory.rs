use std::io::{self, Read};

const MOD: u32 = 100;
const BASES: u32 = 4;
const TEN: u32 = 10;

fn power(mut base: u32, mut n: u32) -> u32 {
    let mut r = 1;
    while n > 0 {
        if n & 1 == 1 {
            r = r * base % MOD;
        }
        base = base * base % MOD;
        n >>= 1;
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u32 = input.trim().parse().unwrap();
    // from the second power on the sum is even but never divisible by 8,
    // so it ends in at most two zeros and its remainder mod 100 decides
    let s = (1..=BASES).map(|b| power(b, n)).sum::<u32>() % MOD;
    let zeros = if s == 0 {
        2
    } else if s % TEN == 0 {
        1
    } else {
        0
    };
    println!("{}", zeros);
}
