use std::fmt::Write as _;
use std::io::{self, Read};

const LIMIT: u64 = 1_000_000_000_000_000_000;
const PRIMES: [u64; 16] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53];
const MOST: u32 = 64;

// the smallest number with a given set of exponents puts the largest
// exponents on the smallest primes, so only numbers 2^a 3^b 5^c ... with
// a >= b >= c >= ... can be answers
fn grow(found: &mut Vec<(u64, u64)>, index: usize, cap: u32, value: u64, divisors: u64) {
    found.push((value, divisors));
    if index == PRIMES.len() {
        return;
    }
    let mut value = value;
    for e in 1..=cap {
        if value > LIMIT / PRIMES[index] {
            break;
        }
        value *= PRIMES[index];
        grow(found, index + 1, e, value, divisors * (e as u64 + 1));
    }
}

fn main() {
    let mut found = Vec::new();
    grow(&mut found, 0, MOST, 1, 1);
    found.sort();
    let mut best = Vec::with_capacity(found.len());
    let mut top = (0u64, 0u64);
    for &f in &found {
        if f.1 > top.1 {
            top = f;
        }
        best.push(top);
    }
    let values: Vec<u64> = found.iter().map(|f| f.0).collect();
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let t: usize = it.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..t {
        let n: u64 = it.next().unwrap().parse().unwrap();
        let k = values.partition_point(|&v| v <= n) - 1;
        writeln!(out, "{} {}", best[k].0, best[k].1).unwrap();
    }
    print!("{}", out);
}
