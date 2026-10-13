use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    let deadline: Vec<usize> = (0..n).map(|i| v[1 + 2 * i]).collect();
    let reward: Vec<usize> = (0..n).map(|i| v[2 + 2 * i]).collect();
    let mut orders: Vec<usize> = (0..n).collect();
    orders.sort_by_key(|&i| deadline[i]);
    // by deadline: keep the best orders that fit, dropping the cheapest when
    // there are more orders than days so far
    let mut kept = BinaryHeap::new();
    for &i in &orders {
        kept.push(Reverse((reward[i], i)));
        if kept.len() > deadline[i] {
            kept.pop();
        }
    }
    let mut chosen: Vec<usize> = kept.into_iter().map(|Reverse((_, i))| i).collect();
    chosen.sort_by_key(|&i| deadline[i]);
    let parts: Vec<String> = chosen.iter().map(|i| (i + 1).to_string()).collect();
    println!("{}\n{}", chosen.len(), parts.join(" "));
}
