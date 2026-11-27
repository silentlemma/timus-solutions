use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let (n, m, k) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    let heights: Vec<i64> = it.take((n * m) as usize).collect();
    // Filling the lowest sections raises stacks below the final minimum h to h.
    // Some stacks at h may get one more container; initially taller ones stay put.
    // The answer is the largest h with sum(max(0, h - height)) <= K.
    let mut lo = *heights.iter().min().unwrap();
    let mut hi = lo + k;
    while lo < hi {
        let mid = (lo + hi + 1) / 2;
        let need: i64 = heights.iter().filter(|&&h| h < mid).map(|&h| mid - h).sum();
        if need <= k {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    println!("{}", lo);
}
