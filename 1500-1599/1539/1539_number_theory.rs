use std::io::{self, Read};

const BASE: i64 = 10;

/// The decimal text times 10^d, as an integer.
fn scaled(text: &str, d: usize) -> i64 {
    let (whole, frac) = text.split_once('.').unwrap_or((text, ""));
    let mut v = whole.bytes().fold(0, |v, c| v * BASE + (c - b'0') as i64);
    for i in 0..d {
        v = v * BASE + frac.as_bytes().get(i).map_or(0, |&c| (c - b'0') as i64);
    }
    v
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let d: usize = it.next().unwrap().parse().unwrap();
    let n: usize = it.next().unwrap().parse().unwrap();
    let one = BASE.pow(d as u32);
    // only the fractional parts matter, and a whole number fits any group
    let mut values: Vec<i64> = Vec::new();
    for _ in 0..n {
        let v = scaled(it.next().unwrap(), d) % one;
        if v != 0 && !values.contains(&v) {
            values.push(v);
        }
    }
    let den = 2 * one;
    // an average v (times 10^d) over q goblins comes from a total p when
    // (2v - 1) q <= den p < (2v + 1) q; q = 10^d always works, as the
    // interval is then at least 1 long
    for q in 1..=one {
        let failed = values.iter().position(|&v| {
            let low = ((2 * v - 1) * q + den - 1) / den; // the smallest total allowed
            low * den >= (2 * v + 1) * q
        });
        match failed {
            // the average that failed is likely to fail again: try it first
            Some(i) => values[..=i].rotate_right(1),
            None => {
                println!("{}", q);
                return;
            }
        }
    }
}
