use std::collections::HashSet;
use std::fmt::Write as _;
use std::io::{self, Read, Write};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let n: i64 = match s.trim().parse() {
        Ok(v) => v,
        Err(_) => return,
    };
    let mut used = HashSet::new();
    let mut out = String::new();
    let (mut total, mut length) = (0i64, 0i64); // the sum and the number of terms so far
    for m in 1..=n {
        // put a large x at position k and then m at k + 1: x must make the
        // sum divisible by k, and x + m divisible by k + 1
        let k = length + 1;
        let a = (-total).rem_euclid(k);
        let b = (-total - m).rem_euclid(k + 1);
        // x = a + k t, and k = -1 modulo k + 1, so t = a - b modulo k + 1
        let step = k * (k + 1);
        let mut x = a + k * (a - b).rem_euclid(k + 1);
        if x <= n {
            x += (n - x) / step * step + step;
        }
        while used.contains(&x) {
            x += step;
        }
        used.insert(x);
        write!(out, "{} {}{}", x, m, if m < n { ' ' } else { '\n' }).unwrap();
        total += x + m;
        length += 2;
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
