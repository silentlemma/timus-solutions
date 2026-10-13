use std::fmt::Write as _;
use std::io::{self, Read};

const BITS: usize = 61; // every n is below 2^60, and a lowered bit leaves at most 60 free ones
const ENDINGS: usize = 4; // per first bit: as is, last bit 1, last two 11, last two 01

/// (a_m, a_m+1) -> (a_2m+bit, a_2m+bit+1)
fn step((x, y): (i64, i64), bit: usize) -> (i64, i64) {
    if bit == 0 {
        (x, x + y)
    } else {
        (x + y, y)
    }
}

fn main() {
    // maps[r]: (p, q) with a = p a_m + q a_m+1 after each candidate suffix of
    // r free bits: alternating bits with the last one or two changed
    let mut maps: Vec<Vec<(i64, i64)>> = vec![Vec::new(); BITS];
    for (r, list) in maps.iter_mut().enumerate() {
        for first in 0..2 {
            for e in 0..ENDINGS {
                let mut pattern: Vec<usize> = (0..r).map(|k| (first + k) % 2).collect();
                if e == 1 && r >= 1 {
                    pattern[r - 1] = 1;
                }
                if e >= 2 && r >= 2 {
                    pattern[r - 2] = usize::from(e == 2);
                    pattern[r - 1] = 1;
                }
                let (mut p, mut q) = ((1, 0), (0, 1));
                for &b in &pattern {
                    p = step(p, b);
                    q = step(q, b);
                }
                list.push((p.0, q.0));
            }
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut out = String::new();
    for token in input.split_ascii_whitespace() {
        let n: i64 = token.parse().unwrap();
        if n == 0 {
            break;
        }
        let length = (i64::BITS - n.leading_zeros()) as usize;
        let mut best = 0i64;
        let mut v = (0i64, 1i64); // (a_0, a_1) for the empty prefix
        for k in (0..length).rev() {
            let bit = (n >> k & 1) as usize;
            if bit == 1 {
                // lower this bit to 0: the k bits below are free
                let low = step(v, 0);
                for &(p, q) in &maps[k] {
                    best = best.max(p * low.0 + q * low.1);
                }
            }
            v = step(v, bit);
        }
        writeln!(out, "{}", best.max(v.0)).unwrap();
    }
    print!("{}", out);
}
