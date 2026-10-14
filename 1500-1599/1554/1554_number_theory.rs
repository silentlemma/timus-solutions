use std::io::{self, Read};

const MOD: i64 = 2007;

/// x^-1 modulo MOD by the extended Euclidean algorithm.
fn inverse(x: i64) -> i64 {
    let (mut a, mut b, mut u, mut v) = (x % MOD, MOD, 1i64, 0i64);
    while b != 0 {
        let q = a / b;
        (a, b) = (b, a - q * b);
        (u, v) = (v, u - q * v);
    }
    (u % MOD + MOD) % MOD
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let data: Vec<i64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = data[0] as usize;
    let f: Vec<i64> = std::iter::once(0)
        .chain(data[1..=n].iter().map(|x| x % MOD))
        .collect();
    // (F * G)(n) sums F(n / d) G(d) over the divisors d of n and is 0 for n > 1,
    // so G(n) = -G(1) * (the sum over the proper divisors), with G(1) = 1 / F(1),
    // and a sieve adds G(d) times F to every multiple of d once G(d) is known
    let first = inverse(f[1]);
    let (mut g, mut acc) = (vec![0i64; n + 1], vec![0i64; n + 1]);
    for d in 1..=n {
        g[d] = if d == 1 {
            first
        } else {
            (MOD - first * acc[d] % MOD) % MOD
        };
        for k in 2..=n / d {
            acc[d * k] = (acc[d * k] + f[k] * g[d]) % MOD;
        }
    }
    let parts: Vec<String> = g[1..].iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
