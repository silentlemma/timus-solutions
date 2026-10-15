use std::fmt::Write;
use std::io::{self, Read};

const SMALL: i64 = 100; // below this the first candidates are simply tried in turn

fn isqrt(v: i64) -> i64 {
    let mut root = (v as f64).sqrt() as i64;
    while root * root > v {
        root -= 1;
    }
    while (root + 1) * (root + 1) <= v {
        root += 1;
    }
    root
}

fn ceil_sqrt(v: i64) -> i64 {
    let root = isqrt(v);
    if root * root == v {
        root
    } else {
        root + 1
    }
}

fn fits(n: i64, k: i64) -> bool {
    n / k == n / (k + 1)
}

fn least(n: i64) -> i64 {
    // the shares agree exactly when n mod k >= n div k, which needs k > s,
    // s = isqrt(n); with k = s + x and e = n - s^2 the quotient is s - x or
    // s - x + 1, and each case gives the least x in closed form
    if n < SMALL {
        let mut k = 1;
        while !fits(n, k) {
            k += 1;
        }
        return k;
    }
    let s = isqrt(n);
    let e = n - s * s;
    let mut xs = Vec::new();
    let gap = s - e;
    if gap >= 1 {
        // quotient s - x: the least x with x^2 + x >= gap (then x^2 - x < gap)
        let mut x = isqrt(gap);
        while x * x + x < gap {
            x += 1;
        }
        while x > 1 && (x - 1) * (x - 1) + (x - 1) >= gap {
            x -= 1;
        }
        xs.push(x);
    }
    // quotient s - x + 1: x^2 >= 2s - e + 1 > (x - 1)^2
    xs.push(ceil_sqrt(2 * s - e + 1));
    let mut best = -1;
    for &x in &xs {
        for d in -1..=1 {
            let k = s + x + d;
            if x + d >= 1 && fits(n, k) && (best < 0 || k < best) {
                best = k;
            }
        }
    }
    best
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let t: usize = words.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for w in words.take(t) {
        writeln!(out, "{}", least(w.parse().unwrap())).unwrap();
    }
    print!("{}", out);
}
