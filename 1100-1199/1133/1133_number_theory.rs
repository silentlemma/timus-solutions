use std::io::{self, Read};

// a prime above the 4e9 + 1 possible answers and below 2^32, so products fit
// in 64 bits; no Fibonacci number with index up to 2000 is divisible by it
const P: u64 = 4294967291;

fn reduce(v: i64) -> u64 {
    v.rem_euclid(P as i64) as u64
}

fn power(mut b: u64, mut e: u64) -> u64 {
    let mut r = 1;
    while e > 0 {
        if e % 2 == 1 {
            r = r * b % P;
        }
        b = b * b % P;
        e /= 2;
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut read = || tok.next().unwrap();
    let (mut i, mut fi, mut j, mut fj, n) = (read(), read(), read(), read(), read());
    if i > j {
        std::mem::swap(&mut i, &mut j);
        std::mem::swap(&mut fi, &mut fj);
    }
    // F(j) = A F(i) + B F(i + 1), with A and B found by stepping coefficients
    let (mut a, mut b, mut na, mut nb) = (1u64, 0u64, 0u64, 1u64);
    for _ in i..j {
        let (sa, sb) = ((a + na) % P, (b + nb) % P);
        a = na;
        b = nb;
        na = sa;
        nb = sb;
    }
    let mut cur = reduce(fi);
    let mut next = (reduce(fj) + P - a * cur % P) % P * power(b, P - 2) % P;
    for _ in i..n {
        let s = (cur + next) % P;
        cur = next;
        next = s;
    }
    for _ in n..i {
        let prev = (next + P - cur) % P;
        next = cur;
        cur = prev;
    }
    let answer = if cur > P / 2 {
        cur as i64 - P as i64
    } else {
        cur as i64
    };
    println!("{}", answer);
}
