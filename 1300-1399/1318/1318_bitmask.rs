use std::io::{self, Read};

const BITS: usize = 128;
const WORD: u32 = 32;
const PARTS: usize = 4;
const DECIMAL: u128 = 10;

fn bit_length(x: u128) -> usize {
    BITS - x.leading_zeros() as usize
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u128>().unwrap());
    let n = it.next().unwrap() as usize;
    let a: Vec<u128> = (0..n)
        .map(|_| (0..PARTS).fold(0, |v, _| v << WORD | it.next().unwrap()))
        .collect();
    // a number of bit length L is at least every power of ten that is
    // shorter, and at least the one power of length L only if it reaches it
    let mut base = [0i64; BITS + 1];
    let mut limit: [Option<u128>; BITS + 1] = [None; BITS + 1];
    let mut p = Some(DECIMAL);
    while let Some(power) = p {
        let len = bit_length(power);
        limit[len] = Some(power);
        for b in base.iter_mut().skip(len + 1) {
            *b += 1;
        }
        p = power.checked_mul(DECIMAL);
    }
    let mut total = 0i64;
    for i in 0..n {
        for j in i + 1..n {
            let x = a[i] ^ a[j];
            let len = bit_length(x);
            total += base[len];
            if limit[len].map_or(false, |l| x >= l) {
                total += 1;
            }
        }
    }
    println!("{}", 2 * total); // every pair counts in both orders
}
