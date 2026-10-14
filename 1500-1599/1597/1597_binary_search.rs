use std::fmt::Write as _;
use std::io::{self, Read};

const MOST_DROPS: i64 = 2_000_000_000; // two eggs already cover 10^18 floors with this many

/// Floors that t drops with k eggs can settle, the sum of C(t, i) over
/// i = 1..k, or n + 1 if that is more.
fn covered(t: i64, k: i64, n: i64) -> i64 {
    let (mut total, mut term) = (0i64, 1i64);
    let mut i = 1;
    while i <= k && i <= t {
        // term * (t - i + 1) / i without overflow: split term by i
        let (q, r, f) = (term / i, term % i, t - i + 1);
        if q > n / f {
            return n + 1;
        }
        term = q * f + r * f / i;
        total += term;
        if total > n {
            return n + 1;
        }
        i += 1;
    }
    total
}

fn drops(k: i64, n: i64) -> i64 {
    if k == 1 {
        return n;
    }
    let (mut lo, mut hi) = (1, MOST_DROPS);
    while lo < hi {
        let mid = (lo + hi) / 2;
        if covered(mid, k, n) >= n {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    lo
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<i64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let mut out = String::new();
    for pair in v.chunks(2) {
        if pair.len() < 2 || (pair[0] == 0 && pair[1] == 0) {
            break;
        }
        writeln!(out, "{}", drops(pair[0], pair[1])).unwrap();
    }
    print!("{}", out);
}
