use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let n = it.next().unwrap() as usize;
    let seg: Vec<(i32, i32)> = (0..n)
        .map(|_| {
            let (a, b) = (it.next().unwrap(), it.next().unwrap());
            (a.min(b), a.max(b))
        })
        .collect();
    // a segment inside another is strictly shorter, so by length the inner
    // one always comes first
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by_key(|&i| seg[i].1 - seg[i].0);
    let mut best = vec![1; n];
    let mut prev = vec![usize::MAX; n];
    for p in 0..n {
        let i = order[p];
        for &j in &order[..p] {
            if seg[i].0 < seg[j].0 && seg[j].1 < seg[i].1 && best[j] + 1 > best[i] {
                best[i] = best[j] + 1;
                prev[i] = j;
            }
        }
    }
    let mut end = (0..n)
        .max_by_key(|&i| (best[i], std::cmp::Reverse(i)))
        .unwrap();
    let mut chain = Vec::new();
    loop {
        chain.push((end + 1).to_string());
        if prev[end] == usize::MAX {
            break;
        }
        end = prev[end];
    }
    chain.reverse();
    println!("{}\n{}", chain.len(), chain.join(" "));
}
