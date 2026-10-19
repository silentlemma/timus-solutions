use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let m = it.next().unwrap() as usize;
    let v: Vec<i64> = it.by_ref().take(n).collect();
    let h: Vec<i64> = it.take(m).collect();
    let max_v = *v.iter().max().unwrap();
    let max_h = *h.iter().max().unwrap();
    // one turn: down the left street and along the bottom, or along the top and down the right
    let mut best = v[0].min(h[m - 1]).max(h[0].min(v[n - 1]));
    // two turns: the middle street is the best one of its kind
    best = best.max(h[0].min(max_v).min(h[m - 1]));
    best = best.max(v[0].min(max_h).min(v[n - 1]));
    println!("{}", best);
}
