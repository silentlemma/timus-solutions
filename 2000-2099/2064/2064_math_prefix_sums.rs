use std::fmt::Write as _;
use std::io::{self, Read, Write};

const LINE: usize = 8;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut tall: Vec<usize> = (0..n).map(|_| it.next().unwrap()).collect();
    let q = it.next().unwrap();
    let x: Vec<usize> = (0..q).map(|_| it.next().unwrap()).collect();
    let most = *x.iter().max().unwrap();
    // tent of height t at every odd multiple of t; the envelope of all
    // tents is the answer, and centres beyond 2 * most never matter
    let limit = 2 * most;
    let mut height = vec![0i32; limit + 1];
    tall.sort_unstable();
    tall.dedup();
    for &t in &tall {
        if t >= most {
            height[most] = most as i32;
            break;
        }
        let mut c = t;
        while c <= limit {
            height[c] = t as i32;
            c += 2 * t;
        }
    }
    // best[x] = max over c of height[c] - |x - c|, by two sweeps
    for i in 1..=limit {
        height[i] = height[i].max(height[i - 1] - 1);
    }
    for i in (0..limit).rev() {
        height[i] = height[i].max(height[i + 1] - 1);
    }
    let mut out = String::with_capacity(q * LINE);
    for &v in &x {
        writeln!(out, "{}", height[v]).unwrap();
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
