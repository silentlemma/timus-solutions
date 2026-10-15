use std::collections::HashMap;
use std::io::{self, Read};

// enough for a deterministic test below 3.2 * 10^9
const WITNESSES: [u64; 4] = [2, 3, 5, 7];

fn power(mut base: u64, mut exp: u64, modulus: u64) -> u64 {
    let mut result = 1;
    base %= modulus;
    while exp > 0 {
        if exp & 1 == 1 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exp >>= 1;
    }
    result
}

/// Miller-Rabin with fixed witnesses, exact for these sizes.
fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    for &p in &WITNESSES {
        if n % p == 0 {
            return n == p;
        }
    }
    let (mut d, mut s) = (n - 1, 0);
    while d % 2 == 0 {
        d /= 2;
        s += 1;
    }
    'outer: for &a in &WITNESSES {
        let mut x = power(a, d, n);
        if x == 1 || x == n - 1 {
            continue;
        }
        for _ in 1..s {
            x = x * x % n;
            if x == n - 1 {
                continue 'outer;
            }
        }
        return false;
    }
    true
}

/// The smallest product of powers of primes[start..] whose totient is
/// rest, or 0 if there is none.
fn least(rest: u64, start: usize, primes: &[u64], memo: &mut HashMap<(u64, usize), u64>) -> u64 {
    if rest == 1 {
        return 1;
    }
    if let Some(&v) = memo.get(&(rest, start)) {
        return v;
    }
    let mut best = 0;
    for i in start..primes.len() {
        let p = primes[i];
        if p - 1 > rest {
            break;
        }
        if rest % (p - 1) != 0 {
            continue;
        }
        let (mut part, mut pw) = (rest / (p - 1), p);
        loop {
            let sub = least(part, i + 1, primes, memo);
            if sub != 0 && (best == 0 || pw * sub < best) {
                best = pw * sub;
            }
            if part % p != 0 {
                break;
            }
            part /= p;
            pw *= p;
        }
    }
    memo.insert((rest, start), best);
    best
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let k: u64 = text.trim().parse().unwrap();
    // student j is admitted exactly when gcd(j, N) = 1, so K = phi(N); every
    // p - 1 over the primes of N divides K, so the candidates are d + 1, d | K
    let mut divs: Vec<u64> = vec![1];
    let mut rest = k;
    let mut p = 2;
    while p * p <= rest {
        if rest % p == 0 {
            let size = divs.len();
            let mut pw = 1;
            while rest % p == 0 {
                rest /= p;
                pw *= p;
                for i in 0..size {
                    let d = divs[i] * pw;
                    divs.push(d);
                }
            }
        }
        p += 1;
    }
    if rest > 1 {
        let more: Vec<u64> = divs.iter().map(|d| d * rest).collect();
        divs.extend(more);
    }
    divs.sort_unstable();
    let primes: Vec<u64> = divs.iter().map(|d| d + 1).filter(|&q| is_prime(q)).collect();
    println!("{}", least(k, 0, &primes, &mut HashMap::new()));
}
