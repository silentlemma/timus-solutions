use std::collections::HashSet;
use std::io::{self, Read};

const LONGEST: usize = 50;
const SHIFT: u32 = 28; // star counts fit in 28 bits

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<u64>().unwrap());
    let n = match it.next() {
        Some(v) => v as usize,
        None => return,
    };
    let stars: Vec<u64> = (0..n).map(|_| it.next().unwrap()).collect();
    let m = it.next().unwrap() as usize;
    let mut wanted: Vec<HashSet<u64>> = vec![HashSet::new(); LONGEST + 1];
    for _ in 0..m {
        let (x, y, d) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap() as usize);
        wanted[d].insert(x << SHIFT | y);
    }
    // a war of d days ending k days ago began k + d - 1 days ago; reach[k]
    // is the oldest day of a matching war that ends k days ago
    let mut reach: Vec<i64> = vec![-1; n];
    for d in 2..=LONGEST.min(n) {
        if wanted[d].is_empty() {
            continue;
        }
        for k in 0..=n - d {
            if wanted[d].contains(&(stars[k + d - 1] << SHIFT | stars[k])) {
                reach[k] = reach[k].max((k + d - 1) as i64);
            }
        }
    }
    let mut cover = -1;
    let out: String = (0..n)
        .map(|k| {
            cover = cover.max(reach[k]);
            if cover >= k as i64 {
                '1'
            } else {
                '0'
            }
        })
        .collect();
    println!("{}", out);
}
