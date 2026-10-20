use std::io::{self, Read};

const LETTERS: usize = 26;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let k: usize = it.next().unwrap().parse().unwrap();
    let s = it.next().unwrap().as_bytes();
    // On a circle every period can be replaced by its gcd with n, so only the
    // divisors of n are tried, from the smallest.
    for d in (1..=n).filter(|d| n % d == 0) {
        let mut count = vec![0usize; d * LETTERS];
        for (i, &c) in s.iter().enumerate() {
            count[(i % d) * LETTERS + (c - b'a') as usize] += 1;
        }
        let mut best = Vec::with_capacity(d);
        let mut kept = 0;
        for r in 0..d {
            let row = &count[r * LETTERS..(r + 1) * LETTERS];
            let top = (0..LETTERS).rev().max_by_key(|&c| row[c]).unwrap();
            best.push(b'a' + top as u8);
            kept += row[top];
        }
        if n - kept <= k {
            let result: String = (0..n).map(|i| best[i % d] as char).collect();
            println!("{}\n{}", d, result);
            return;
        }
    }
}
