use std::io::{self, Read};

// a big number as base 10^9 digits, least significant first
const BASE: u64 = 1_000_000_000;

fn mul_small(a: &mut Vec<u64>, m: u64) {
    let mut carry = 0;
    for d in a.iter_mut() {
        let cur = *d * m + carry;
        *d = cur % BASE;
        carry = cur / BASE;
    }
    while carry > 0 {
        a.push(carry % BASE);
        carry /= BASE;
    }
}

// divides by m and returns the remainder
fn div_small(a: &mut Vec<u64>, m: u64) -> u64 {
    let mut rest = 0;
    for d in a.iter_mut().rev() {
        let cur = rest * BASE + *d;
        *d = cur / m;
        rest = cur % m;
    }
    while a.len() > 1 && *a.last().unwrap() == 0 {
        a.pop();
    }
    rest
}

fn add(a: &mut Vec<u64>, b: &[u64]) {
    if a.len() < b.len() {
        a.resize(b.len(), 0);
    }
    let mut carry = 0;
    for (i, d) in a.iter_mut().enumerate() {
        let cur = *d + b.get(i).copied().unwrap_or(0) + carry;
        *d = cur % BASE;
        carry = cur / BASE;
    }
    if carry > 0 {
        a.push(carry);
    }
}

fn less(a: &[u64], b: &[u64]) -> bool {
    if a.len() != b.len() {
        return a.len() < b.len();
    }
    for i in (0..a.len()).rev() {
        if a[i] != b[i] {
            return a[i] < b[i];
        }
    }
    false
}

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

const SCALE: i64 = 20000000;

fn exact_floor(load: i64, stage: i64, lower: i64) -> i64 {
    let (mut num, mut den) = (vec![0u64], vec![1u64]);
    let factor = (load * (2 * stage - 1)) as u64;
    for i in 1..stage {
        let d = (2 * i - 1) as u64;
        let r = factor % d;
        if r == 0 {
            continue;
        }
        let mut copy = den.clone();
        let g = gcd(d, div_small(&mut copy, d));
        let mut part = den.clone();
        div_small(&mut part, g);
        mul_small(&mut part, r);
        mul_small(&mut num, d / g);
        add(&mut num, &part);
        mul_small(&mut den, d / g);
    }
    // The interval width is below one, leaving at most one integer correction.
    let mut upper = den;
    mul_small(&mut upper, (lower + 1) as u64);
    lower + if !less(&num, &upper) { 1 } else { 0 }
}

fn line_ceiling(distance: i64, load: i64, stage: i64) -> i64 {
    let factor = load * (2 * stage - 1);
    let mut whole = (stage - 1) * load + (2 * stage - 1) * distance;
    let mut lower = 0;
    for i in 1..stage {
        let d = 2 * i - 1;
        whole -= factor / d;
        lower += (factor % d) * SCALE / d;
    }
    let mut floor = lower / SCALE;
    if stage > 1 && (lower + stage - 2) / SCALE != floor {
        floor = exact_floor(load, stage, floor);
    }
    whole - floor
}

fn main() {
    let mut raw = String::new();
    io::stdin().read_to_string(&mut raw).unwrap();
    let mut values = raw
        .split_ascii_whitespace()
        .map(|token| token.parse::<i64>().unwrap());
    let (distance, load) = (values.next().unwrap(), values.next().unwrap());
    let (mut lower, mut stage) = (0, 1);
    while lower + load * SCALE / (2 * stage - 1) < distance * SCALE {
        lower += load * SCALE / (2 * stage - 1);
        stage += 1;
    }
    // Lower-bound selection can overshoot the true active line by at most one.
    let mut answer = line_ceiling(distance, load, stage);
    if stage > 1 {
        answer = answer.max(line_ceiling(distance, load, stage - 1));
    }
    println!("{}", answer);
}
