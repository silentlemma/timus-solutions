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

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m) = (v[0], v[1]);
    // from the target backwards: the last m km take one load; before it, a
    // stretch of m / (2k - 1) km is crossed 2k - 1 times to bring k loads
    let (target, load) = (n as f64, m as f64);
    let mut stretch = 0.0;
    let mut k: i64 = 1;
    loop {
        let step = load / (2 * k - 1) as f64;
        if stretch + step >= target {
            break;
        }
        stretch += step;
        k += 1;
    }
    // fuel = (k-1) m + (2k-1) n - sum over i < k of m (2k-1) / (2i-1); its
    // fractional sum f = sum r_i / (2i-1) is kept exactly as num / den
    let mut whole = (k - 1) * m + (2 * k - 1) * n;
    let (mut num, mut den) = (vec![0u64], vec![1u64]);
    let mut approx = 0.0;
    for i in 1..k {
        let d = (2 * i - 1) as u64;
        let r = (m * (2 * k - 1)) as u64 % d;
        whole -= m * (2 * k - 1) / d as i64;
        if r == 0 {
            continue;
        }
        approx += r as f64 / d as f64;
        let mut copy = den.clone();
        let g = gcd(d, div_small(&mut copy, d));
        // num/den + r/d over the denominator den * (d / g)
        let mut part = den.clone();
        div_small(&mut part, g);
        mul_small(&mut part, r);
        mul_small(&mut num, d / g);
        add(&mut num, &part);
        mul_small(&mut den, d / g);
    }
    // floor(f) from its approximation, then corrected exactly
    let times = |t: i64| {
        let mut b = den.clone();
        mul_small(&mut b, t as u64);
        b
    };
    let mut t = approx.floor() as i64;
    while t > 0 && less(&num, &times(t)) {
        t -= 1;
    }
    while !less(&num, &times(t + 1)) {
        t += 1;
    }
    println!("{}", whole - t);
}
