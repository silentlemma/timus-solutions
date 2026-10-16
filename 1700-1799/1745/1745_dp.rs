use std::io::{self, Read};

struct Word {
    change: i64,
    low: i64,
    size: i64,
    id: usize,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    // each word: net change of the depth, lowest depth reached, length
    let (mut rising, mut falling) = (Vec::new(), Vec::new());
    let mut top = 0usize;
    for id in 1..=n {
        let w = it.next().unwrap();
        let (mut depth, mut low) = (0i64, 0i64);
        for c in w.bytes() {
            depth += if c == b'(' { 1 } else { -1 };
            low = low.min(depth);
        }
        top += w.len();
        let word = Word { change: depth, low, size: w.len() as i64, id };
        if depth >= 0 {
            rising.push(word);
        } else {
            falling.push(word);
        }
    }
    // in a best answer the words that open more than they close come first,
    // those that dip least first; the rest go last, those that end highest
    // above their lowest point first
    rising.sort_by_key(|w| -w.low);
    falling.sort_by_key(|w| w.low - w.change);
    let order: Vec<Word> = rising.into_iter().chain(falling).collect();
    // best[d]: longest prefix built so far that ends at depth d
    let mut best = vec![-1i64; top + 1];
    best[0] = 0;
    let mut taken = vec![vec![false; top + 1]; order.len()];
    for (k, w) in order.iter().enumerate() {
        let mut next = best.clone();
        for d in 0..=top {
            if best[d] < 0 || d as i64 + w.low < 0 {
                continue;
            }
            let e = (d as i64 + w.change) as usize;
            if best[d] + w.size > next[e] {
                next[e] = best[d] + w.size;
                taken[k][e] = true;
            }
        }
        best = next;
    }
    let mut used = Vec::new();
    let mut d = 0i64;
    for k in (0..order.len()).rev() {
        if taken[k][d as usize] {
            used.push(order[k].id.to_string());
            d -= order[k].change;
        }
    }
    used.reverse();
    println!("{} {}", best[0], used.len());
    println!("{}", used.join(" "));
}
