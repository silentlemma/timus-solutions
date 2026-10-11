use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // with r = N mod K, an s x s corner square is left over, s = min(r, K - r)
    let r = n % k;
    let s = r.min(k - r);
    println!("{}", if n < k { 0 } else { (n * n - s * s) / k });
}
