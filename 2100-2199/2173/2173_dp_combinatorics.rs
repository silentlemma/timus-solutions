use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

fn power(mut base: u64, mut exponent: u64) -> u64 {
    let mut result = 1;
    base %= MOD;
    while exponent > 0 {
        if exponent & 1 == 1 {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent >>= 1;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let m = it.next().unwrap();
    let wishes: Vec<usize> = it.take(n).collect();
    let mut fact = vec![1u64; m + 1];
    for i in 1..=m {
        fact[i] = fact[i - 1] * i as u64 % MOD;
    }
    let mut inv = vec![1u64; m + 1];
    inv[m] = power(fact[m], MOD - 2);
    for i in (1..=m).rev() {
        inv[i - 1] = inv[i] * i as u64 % MOD;
    }

    // ways[j]: the sponsors so far fill exactly j problems once; with t
    // mentions placed, (t - j) / 2 problems hold two sponsors and the rest none
    let mut ways = vec![0u64; m + 1];
    ways[0] = 1;
    let mut placed = 0;
    for &s in &wishes {
        let mut next = vec![0u64; m + 1];
        for j in (placed % 2..=m).step_by(2) {
            if ways[j] == 0 {
                continue;
            }
            let empty = m - j - (placed - j) / 2;
            // a of the new mentions go to problems with one sponsor, the
            // other s - a to empty problems
            let base = ways[j] * fact[j] % MOD * fact[empty] % MOD;
            let from = s.saturating_sub(empty);
            for a in from..=s.min(j) {
                let rest = s - a;
                let mut term = base * inv[a] % MOD * inv[j - a] % MOD;
                term = term * inv[rest] % MOD * inv[empty - rest] % MOD;
                let target = j - a + rest;
                next[target] = (next[target] + term) % MOD;
            }
        }
        ways = next;
        placed += s;
    }
    println!("{}", ways.iter().fold(0, |acc, w| (acc + w) % MOD));
}
