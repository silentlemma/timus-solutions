use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;
const EDGE_KINDS: u64 = 3;
const MIDDLE_KINDS: u64 = 4;
const ONE_COLOUR_KINDS: u64 = 2;

fn power(mut a: u64, mut e: u64) -> u64 {
    let mut r = 1;
    a %= MOD;
    while e > 0 {
        if e & 1 == 1 {
            r = r * a % MOD;
        }
        a = a * a % MOD;
        e >>= 1;
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    let (squares, row) = (n * n / 2, n / 2);
    let middle = squares - 2 * row;
    let mut fact = vec![1u64; squares + 1];
    for i in 1..=squares {
        fact[i] = fact[i - 1] * i as u64 % MOD;
    }
    let mut inv = vec![1u64; squares + 1];
    inv[squares] = power(fact[squares], MOD - 2);
    for i in (1..=squares).rev() {
        inv[i - 1] = inv[i] * i as u64 % MOD;
    }
    let choose = |a: usize, b: usize| -> u64 {
        if b > a {
            0
        } else {
            fact[a] * inv[b] % MOD * inv[a - b] % MOD
        }
    };
    // a dark square on the first or last row takes three kinds of piece
    // (the man that would be crowned there is out), any other square four
    let mut total = 0;
    for a in 0..=k.min(2 * row) {
        let edge = choose(2 * row, a) * power(EDGE_KINDS, a as u64) % MOD;
        let rest = choose(middle, k - a) * power(MIDDLE_KINDS, (k - a) as u64) % MOD;
        total = (total + edge * rest) % MOD;
    }
    // positions of one colour: on its last row only the king, elsewhere
    // the man or the king
    let mut one = 0;
    for a in 0..=k.min(row) {
        let rest = choose(middle + row, k - a) * power(ONE_COLOUR_KINDS, (k - a) as u64) % MOD;
        one = (one + choose(row, a) * rest) % MOD;
    }
    println!("{}", (total + 2 * MOD - 2 * one) % MOD);
}
