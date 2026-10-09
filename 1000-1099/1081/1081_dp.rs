use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, mut k) = (v[0] as usize, v[1]);
    // count[r]: strings of length r without two adjacent ones (Fibonacci)
    let mut count: Vec<u64> = vec![1, 2];
    while count.len() <= n {
        let next = count[count.len() - 1] + count[count.len() - 2];
        count.push(next);
    }
    if k > count[n] {
        println!("-1");
        return;
    }
    let mut out = String::new();
    let mut last = '0';
    for pos in 0..n {
        let rest = count[n - pos - 1];
        // strings with 0 here come first; a 1 is only possible after a 0
        if last == '1' || k <= rest {
            last = '0';
        } else {
            k -= rest;
            last = '1';
        }
        out.push(last);
    }
    println!("{}", out);
}
