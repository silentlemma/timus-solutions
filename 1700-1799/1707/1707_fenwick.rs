use std::fmt::Write;
use std::io::{self, Read};

const MOD: i64 = 200_904_040_963; // the modulus of the hash printed for long experiments
const BASE: i64 = 7;
const SHORT: usize = 20; // experiments up to this length are printed digit by digit
const CORNERS: usize = 4;
const OPPOSITE: usize = 3; // the corner (a - 1, c - 1) among the four of a step

fn wrap(v: i64, n: usize) -> usize {
    v.rem_euclid(n as i64) as usize
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let n = next() as usize;
    let m = next() as usize;
    // the eyes' states are points (s, t); an experiment step asks whether a
    // rectangle holds one, answered by four prefix counts of a sweep over t
    let mut xs_by_y: Vec<Vec<usize>> = vec![Vec::new(); n];
    for _ in 0..m {
        let (s0, t0, ds, dt, k) = (next(), next(), next(), next(), next());
        for i in 0..k {
            xs_by_y[wrap(t0 + i * dt, n)].push(wrap(s0 + i * ds, n));
        }
    }
    let p = next() as usize;
    let mut asks_by_y: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n];
    // count 0 is a fixed zero for the corners outside the grid
    let mut count = 1;
    let mut experiments: Vec<Vec<usize>> = Vec::with_capacity(p);
    for _ in 0..p {
        let (a0, b0, c0, d0) = (next(), next(), next(), next());
        let (da, db, dc, dd) = (next(), next(), next(), next());
        let q = next();
        let mut ids = Vec::with_capacity(q as usize * CORNERS);
        for j in 0..q {
            let (mut a, mut b) = (wrap(a0 + j * da, n) as i64, wrap(b0 + j * db, n) as i64);
            let (mut c, mut d) = (wrap(c0 + j * dc, n) as i64, wrap(d0 + j * dd, n) as i64);
            if a > b {
                std::mem::swap(&mut a, &mut b);
            }
            if c > d {
                std::mem::swap(&mut c, &mut d);
            }
            for &(x, y) in &[(b, d), (a - 1, d), (b, c - 1), (a - 1, c - 1)] {
                if x < 0 || y < 0 {
                    ids.push(0);
                } else {
                    asks_by_y[y as usize].push((x as usize, count));
                    ids.push(count);
                    count += 1;
                }
            }
        }
        experiments.push(ids);
    }
    let mut below = vec![0i32; count]; // points with s <= x and t <= y for each asked corner
    let mut tree = vec![0i32; n + 1];
    for y in 0..n {
        for &x in &xs_by_y[y] {
            let mut i = x + 1;
            while i <= n {
                tree[i] += 1;
                i += i & i.wrapping_neg();
            }
        }
        for &(x, id) in &asks_by_y[y] {
            let mut i = x + 1;
            let mut total = 0;
            while i > 0 {
                total += tree[i];
                i -= i & i.wrapping_neg();
            }
            below[id] = total;
        }
    }
    let mut out = String::new();
    for ids in &experiments {
        let bits: Vec<u8> = ids
            .chunks(CORNERS)
            .map(|c| (below[c[0]] - below[c[1]] - below[c[2]] + below[c[OPPOSITE]] > 0) as u8)
            .collect();
        if bits.len() <= SHORT {
            let line: String = bits.iter().map(|&b| (b'0' + b) as char).collect();
            writeln!(out, "{}", line).unwrap();
        } else {
            let value = bits.iter().rev().fold(0, |v, &b| (v * BASE + b as i64) % MOD);
            writeln!(out, "{}", value).unwrap();
        }
    }
    print!("{}", out);
}
