use std::cmp::Ordering;
use std::io::{self, Read};

const BASE: u64 = 1_000_000_000; // digits of a big number, lowest first
const PERCENT: u64 = 100;

fn multiply(a: &mut Vec<u64>, f: u64) {
    let mut carry = 0;
    for d in a.iter_mut() {
        let cur = *d * f + carry;
        *d = cur % BASE;
        carry = cur / BASE;
    }
    if carry > 0 {
        a.push(carry);
    }
}

// compares numbers without leading zero digits
fn compare(a: &[u64], b: &[u64]) -> Ordering {
    a.len()
        .cmp(&b.len())
        .then_with(|| a.iter().rev().cmp(b.iter().rev()))
}

fn number(mut v: u64) -> Vec<u64> {
    let mut a = Vec::new();
    while v > 0 {
        a.push(v % BASE);
        v /= BASE;
    }
    a
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u64>().unwrap());
    let (gold, limit, fee) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    // after k years the gold is gold * ((100 - fee) / 100)^k exactly, so
    // compare gold * (100 - fee)^k with limit * 100^k in whole numbers
    let (mut left, mut right) = (number(gold), number(limit));
    let mut years = 0;
    while compare(&left, &right) == Ordering::Greater {
        multiply(&mut left, PERCENT - fee);
        multiply(&mut right, PERCENT);
        years += 1;
    }
    println!("{}", years);
}
