use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

fn power(mut base: u64, mut exp: u64) -> u64 {
    let mut result = 1;
    base %= MOD;
    while exp > 0 {
        if exp & 1 == 1 {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    result
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (m, n, k, l) = match v[..] {
        [m, n, k, l] => (m, n, k, l),
        _ => panic!("expected four numbers"),
    };
    let top = m.max(n);
    let mut fact = vec![1u64; top + 1];
    for i in 1..=top {
        fact[i] = fact[i - 1] * i as u64 % MOD;
    }
    let mut inv = vec![1u64; top + 1];
    inv[top] = power(fact[top], MOD - 2);
    for i in (1..=top).rev() {
        inv[i - 1] = inv[i] * i as u64 % MOD;
    }
    let choose = |a: usize, b: usize| fact[a] * inv[b] % MOD * inv[a - b] % MOD;
    // the other a x b cells must leave no row and no column empty. With j of
    // the b columns forced empty, each of the a rows is any nonzero pattern
    // on the rest; inclusion-exclusion over j, along the shorter side
    let (a, b) = ((m - k).min(n - l), (m - k).max(n - l));
    let mut rest = 0;
    for j in 0..=a {
        let term = choose(a, j) * power((power(2, (a - j) as u64) + MOD - 1) % MOD, b as u64) % MOD;
        rest = (rest + if j % 2 == 1 { MOD - term } else { term }) % MOD;
    }
    println!("{}", choose(m, k) * choose(n, l) % MOD * rest % MOD);
}
