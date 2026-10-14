use std::io::{self, Read};

const MOD: u64 = 1_000_000_000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // count values from the top, so that "larger" becomes a prefix
    let flipped: Vec<usize> = v[2..2 + n].iter().map(|&a| n + 1 - a).collect();
    // ends[i]: decreasing runs of the current length that end at position i
    let mut ends = vec![1u64; n];
    for _ in 1..k {
        let mut tree = vec![0u64; n + 1];
        let mut next = vec![0u64; n];
        for (i, &f) in flipped.iter().enumerate() {
            // the runs one shorter that end earlier at a larger value
            let (mut s, mut j) = (0u64, f - 1);
            while j > 0 {
                s += tree[j];
                j &= j - 1;
            }
            next[i] = s % MOD;
            let mut j = f;
            while j <= n {
                tree[j] = (tree[j] + ends[i]) % MOD;
                j += j & j.wrapping_neg();
            }
        }
        ends = next;
    }
    println!("{}", ends.iter().fold(0, |acc, &e| (acc + e) % MOD));
}
