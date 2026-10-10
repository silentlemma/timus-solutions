use std::io;

// little-endian digits in base 10^9
type Big = Vec<u64>;
const BASE: u64 = 1_000_000_000;
const ISLANDS: usize = 3;

fn add(x: &Big, y: &Big) -> Big {
    let mut r = Vec::new();
    let mut carry = 0;
    let mut k = 0;
    while k < x.len() || k < y.len() || carry > 0 {
        carry += x.get(k).unwrap_or(&0) + y.get(k).unwrap_or(&0);
        r.push(carry % BASE);
        carry /= BASE;
        k += 1;
    }
    r
}

fn mul_small(x: &mut Big, m: u64) {
    let mut carry = 0;
    for d in x.iter_mut() {
        carry += *d * m;
        *d = carry % BASE;
        carry /= BASE;
    }
    while carry > 0 {
        x.push(carry % BASE);
        carry /= BASE;
    }
}

fn div_small(x: &mut Big, m: u64) {
    let mut rest = 0;
    for d in x.iter_mut().rev() {
        let cur = *d + rest * BASE;
        *d = cur / m;
        rest = cur % m;
    }
    while x.len() > 1 && *x.last().unwrap() == 0 {
        x.pop();
    }
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    // plane[b][c][i]: sequences of islands that start on the tourist's island
    // 0, use a, b and c cities of the islands (a fixed per plane), never
    // repeat an island twice in a row and end on island i
    let mut prev: Vec<Vec<Vec<Big>>> = Vec::new();
    for a in 1..=n {
        let mut cur = vec![vec![vec![Big::new(); ISLANDS]; n + 1]; n + 1];
        for b in 0..=n {
            for c in 0..=n {
                if a == 1 && b == 0 && c == 0 {
                    cur[b][c][0] = vec![1];
                }
                if a > 1 {
                    cur[b][c][0] = add(&prev[b][c][1], &prev[b][c][2]);
                }
                if b > 0 {
                    cur[b][c][1] = add(&cur[b - 1][c][0], &cur[b - 1][c][2]);
                }
                if c > 0 {
                    cur[b][c][2] = add(&cur[b][c - 1][0], &cur[b][c - 1][1]);
                }
            }
        }
        prev = cur;
    }
    // the trip closes back on island 0, so it must not end there
    let mut total = add(&prev[n][n][1], &prev[n][n][2]);
    if total.is_empty() {
        total.push(0);
    }
    // cities fill the island slots in any order, except the fixed start, and
    // every trip is counted once in each direction; (n-1)! n!^2 is the
    // product of k^2 (k-1) over k from 2 to n
    for k in 2..=n as u64 {
        mul_small(&mut total, k * k * (k - 1));
    }
    div_small(&mut total, 2);
    let mut out = total.last().unwrap().to_string();
    for d in total.iter().rev().skip(1) {
        out += &format!("{:09}", d);
    }
    println!("{}", out);
}
