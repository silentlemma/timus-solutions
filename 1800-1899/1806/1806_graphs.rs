use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::io::{self, Read};

const DIGITS: usize = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let cost: Vec<i64> = (0..DIGITS).map(|_| it.next().unwrap().parse().unwrap()).collect();
    let mut place = vec![1i64; DIGITS];
    for p in (0..DIGITS - 1).rev() {
        place[p] = place[p + 1] * DIGITS as i64;
    }
    let number: Vec<i64> = (0..n).map(|_| it.next().unwrap().parse().unwrap()).collect();
    let index: HashMap<i64, usize> = number.iter().enumerate().map(|(i, &v)| (v, i)).collect();
    let mut best: Vec<Option<i64>> = vec![None; n];
    let mut before = vec![usize::MAX; n];
    let mut heap = BinaryHeap::new();
    best[0] = Some(0);
    heap.push(Reverse((0i64, 0usize)));
    while let Some(Reverse((d, u))) = heap.pop() {
        if Some(d) != best[u] {
            continue;
        }
        if u == n - 1 {
            break;
        }
        let value = number[u];
        let digit: Vec<i64> = (0..DIGITS).map(|p| value / place[p] % DIGITS as i64).collect();
        // neighbours with the first change at digit p share a prefix of p
        for p in 0..DIGITS {
            let low = value - digit[p] * place[p];
            let changes = (0..DIGITS as i64).filter(|&o| o != digit[p]).map(|o| low + o * place[p]);
            let swaps = (p + 1..DIGITS)
                .filter(|&q| digit[q] != digit[p])
                .map(|q| value + (digit[q] - digit[p]) * (place[p] - place[q]));
            for next in changes.chain(swaps) {
                if let Some(&v) = index.get(&next) {
                    let time = d + cost[p];
                    if best[v].map_or(true, |b| time < b) {
                        best[v] = Some(time);
                        before[v] = u;
                        heap.push(Reverse((time, v)));
                    }
                }
            }
        }
    }
    match best[n - 1] {
        None => println!("-1"),
        Some(time) => {
            let mut path = vec![n - 1];
            while *path.last().unwrap() != 0 {
                path.push(before[*path.last().unwrap()]);
            }
            let line: Vec<String> = path.iter().rev().map(|v| (v + 1).to_string()).collect();
            println!("{}\n{}\n{}", time, path.len(), line.join(" "));
        }
    }
}
