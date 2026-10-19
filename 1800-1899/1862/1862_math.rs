use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let level: u64 = input.trim().parse().unwrap();
    // the numbers form a perfect binary tree, and the mole walks the tree
    // distance; summing over every edge the nodes below it times the nodes
    // above it gives 2^l ((l - 1)(2^l + 1) - 2 (2^l - 2))
    let (mut power, mut base, mut e) = (1u64, 2u64, level);
    while e > 0 {
        if e & 1 == 1 {
            power = power * base % MOD;
        }
        base = base * base % MOD;
        e >>= 1;
    }
    let l = level % MOD;
    let first = (l + MOD - 1) % MOD * ((power + 1) % MOD) % MOD;
    let second = 2 * ((power + MOD - 2) % MOD) % MOD;
    let inner = (first + MOD - second) % MOD;
    println!("{}", power * inner % MOD);
}
