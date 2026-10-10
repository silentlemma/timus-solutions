use std::io::{self, Read};

// anything that is not a digit acts like a digit too large for every base
const WALL: usize = 36;
const SMALLEST: usize = 2;

fn value(ch: u8) -> usize {
    match ch {
        b'0'..=b'9' => (ch - b'0') as usize,
        b'A'..=b'Z' => (ch - b'A') as usize + 10,
        _ => WALL,
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    // a number in base k starts at every digit below k whose left neighbour
    // is k or more, so each neighbouring pair (left, right) with right < left
    // starts a number in the bases right + 1 .. left
    let mut pairs = [[0i64; WALL + 1]; WALL + 1];
    let mut left = WALL;
    for &ch in &data {
        let right = value(ch);
        pairs[left][right] += 1;
        left = right;
    }
    let mut count = [0i64; WALL + 2];
    for l in 1..=WALL {
        for r in 0..l {
            count[(r + 1).max(SMALLEST)] += pairs[l][r];
            count[l + 1] -= pairs[l][r];
        }
    }
    let (mut best, mut running, mut best_k) = (-1i64, 0i64, SMALLEST);
    for (k, &c) in count.iter().enumerate().take(WALL + 1) {
        running += c;
        if k >= SMALLEST && running > best {
            best = running;
            best_k = k;
        }
    }
    println!("{} {}", best_k, best);
}
