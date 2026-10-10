use std::io::{self, Read};

const SIDE: f64 = 100.0;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let (n, m, k) = (
        tok.next().unwrap(),
        tok.next().unwrap(),
        tok.next().unwrap() as usize,
    );
    let mut blocks: Vec<(i64, i64)> = (0..k)
        .map(|_| (tok.next().unwrap(), tok.next().unwrap()))
        .collect();
    blocks.sort_unstable();
    // a route can use a chain of diagonal blocks increasing in both
    // coordinates; each one replaces two sides by one diagonal
    let mut chain = vec![1i64; k];
    let mut best = 0;
    for i in 0..k {
        for j in 0..i {
            if blocks[j].0 < blocks[i].0 && blocks[j].1 < blocks[i].1 {
                chain[i] = chain[i].max(chain[j] + 1);
            }
        }
        best = best.max(chain[i]);
    }
    let length = SIDE * (n + m - 2 * best) as f64 + SIDE * 2f64.sqrt() * best as f64;
    println!("{}", length.round() as i64);
}
