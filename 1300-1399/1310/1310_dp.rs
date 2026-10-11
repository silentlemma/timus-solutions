use std::cmp::Ordering;
use std::io::{self, Read};

const BASE: u64 = 1_000_000_000; // a limb holds nine decimal digits
const LIMB_DIGITS: usize = 9;

// a non-negative number as limbs of nine decimal digits, lowest first
fn parse(s: &str) -> Vec<u64> {
    let bytes = s.as_bytes();
    let mut limbs = Vec::new();
    let mut end = bytes.len();
    while end > 0 {
        let start = end.saturating_sub(LIMB_DIGITS);
        limbs.push(s[start..end].parse().unwrap());
        end = start;
    }
    while limbs.last() == Some(&0) {
        limbs.pop();
    }
    limbs
}

fn add(a: &mut Vec<u64>, b: &[u64]) {
    if a.len() < b.len() {
        a.resize(b.len(), 0);
    }
    let mut carry = 0;
    for i in 0..a.len() {
        let sum = a[i] + b.get(i).copied().unwrap_or(0) + carry;
        a[i] = sum % BASE;
        carry = sum / BASE;
    }
    if carry > 0 {
        a.push(carry);
    }
}

fn compare(a: &[u64], b: &[u64]) -> Ordering {
    a.len()
        .cmp(&b.len())
        .then_with(|| a.iter().rev().cmp(b.iter().rev()))
}

// a -= b, where a >= b
fn subtract(a: &mut Vec<u64>, b: &[u64]) {
    let mut borrow = 0;
    for i in 0..a.len() {
        let take = b.get(i).copied().unwrap_or(0) + borrow;
        borrow = (a[i] < take) as u64;
        a[i] = a[i] + borrow * BASE - take;
    }
    while a.last() == Some(&0) {
        a.pop();
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut number = || words.next().unwrap().parse::<usize>().unwrap();
    let (length, top, k) = (number(), number(), number());
    let mut n = parse(words.next().unwrap());
    // ways[i][r]: how many ways i registers can hold values 1..M with a sum
    // that leaves remainder r modulo K
    let mut ways = vec![vec![Vec::new(); k]; length + 1];
    ways[0][0].push(1);
    for i in 1..=length {
        for v in 1..=top {
            for r in 0..k {
                let prev = ways[i - 1][r].clone();
                add(&mut ways[i][(r + v) % k], &prev);
            }
        }
    }
    let mut out = Vec::with_capacity(length);
    let mut total = 0;
    for pos in 0..length {
        let left = length - pos - 1;
        // try the values in increasing order and skip whole blocks of states
        for v in 1..=top {
            let block = &ways[left][(k - (total + v) % k) % k];
            if compare(&n, block) == Ordering::Less {
                out.push(v.to_string());
                total += v;
                break;
            }
            subtract(&mut n, block);
        }
    }
    println!("{}", out.join(" "));
}
