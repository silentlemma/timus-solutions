use std::io::{self, Read};

const ROOT: usize = 31623;

// The inverse of a modulo m by the extended Euclidean algorithm.
fn inverse(a: i64, m: i64) -> i64 {
    let (mut r0, mut r1, mut s0, mut s1) = (m, a % m, 0i64, 1i64);
    while r1 != 0 {
        let t = r0 / r1;
        (r0, r1) = (r1, r0 - t * r1);
        (s0, s1) = (s1, s0 - t * s1);
    }
    (s0 % m + m) % m
}

fn main() {
    let mut composite = vec![false; ROOT + 1];
    let mut primes = Vec::new();
    for i in 2..=ROOT {
        if !composite[i] {
            primes.push(i as i64);
            for j in (i * i..=ROOT).step_by(i) {
                composite[j] = true;
            }
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let mut out = String::new();
    for &n in &v[1..1 + v[0] as usize] {
        let p = *primes.iter().find(|&&d| n % d == 0).unwrap();
        let q = n / p;
        // x = 1 (mod p) and x = 0 (mod q); the other root is n + 1 - x
        let x = q * inverse(q, p) % n;
        let y = n + 1 - x;
        out += &format!("0 1 {} {}\n", x.min(y), x.max(y));
    }
    print!("{}", out);
}
