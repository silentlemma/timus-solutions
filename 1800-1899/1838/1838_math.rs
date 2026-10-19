use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    if v.is_empty() {
        return;
    }
    let (length, n) = (v[0], v[1] as usize);
    let s = &v[2..2 + n];
    // a cut at x between supports s[i] and s[i + 1] leaves both parts
    // standing when the left centre x/2 lies in [s[0], s[i]] and the right
    // centre (x + length)/2 lies in [s[i + 1], s[n - 1]]
    let (lo_all, hi_all) = (2 * s[0], 2 * s[n - 1] - length);
    let safe: i64 = s
        .windows(2)
        .map(|w| {
            let lo = w[0].max(lo_all).max(2 * w[1] - length);
            let hi = w[1].min(hi_all).min(2 * w[0]);
            (hi - lo).max(0)
        })
        .sum();
    println!("{}", length - safe);
}
