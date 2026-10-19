use std::io::{self, Read};

const MOD: u64 = 1000000007;

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn columns(n: u64, m: u64, k: u64) -> u128 {
    let end = n * m - 1;
    let mut total = 0_u128;
    for c in 0..n {
        let lower = c * m;
        let upper = lower + m;
        let first = lower / k + 1;
        let last = upper.min(end) / k;
        if last < first {
            continue;
        }
        let count = last - first + 1;
        let (a, b) = if c % 2 == 0 {
            (first * k - lower, last * k - lower)
        } else {
            (upper - first * k, upper - last * k)
        };
        if c % 2 != 0 && b == 0 {
            total += 1;
        }
        total += count as u128 * (a + b) as u128 / 2;
    }
    total
}

fn residues(n: u64, m: u64, k: u64) -> u128 {
    let period = 2 * m;
    let g = gcd(k, period);
    let length = period / g;
    let refills = (n * m - 1) / k;
    let remainder = refills % length;
    let reverse = length - remainder - 1;
    let work = remainder.min(reverse);
    let half = length / 2;
    let cycle = g as u128 * half as u128 * (length - half) as u128 + 1;
    let (mut at, step, mut prefix) = (0, k % period, 0_u64);
    for _ in 0..work {
        at += step;
        if at >= period {
            at -= period;
        }
        prefix += at.min(period - at);
    }
    let tail = if reverse < remainder {
        cycle - 1 - prefix as u128
    } else {
        prefix as u128
    };
    (refills / length) as u128 * cycle + tail
}

fn solve(n: u64, m: u64, k: u64) -> u64 {
    let base = n * m - 1;
    if k > base {
        return base % MOD;
    }
    let length = 2 * m / gcd(k, 2 * m);
    let remainder = base / k % length;
    let work = remainder.min(length - remainder - 1);
    let extra = if n < work {
        columns(n, m, k)
    } else {
        residues(n, m, k)
    };
    ((base as u128 + 2 * extra) % MOD as u128) as u64
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..count {
        let n = tokens.next().unwrap().parse().unwrap();
        let m = tokens.next().unwrap().parse().unwrap();
        let k = tokens.next().unwrap().parse().unwrap();
        out.push_str(&format!("{}\n", solve(n, m, k)));
    }
    print!("{}", out);
}
