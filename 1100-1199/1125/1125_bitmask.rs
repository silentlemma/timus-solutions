use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let m: i64 = tok.next().unwrap().parse().unwrap();
    let n: i64 = tok.next().unwrap().parse().unwrap();
    if m == 0 || n == 0 {
        print!("{}", "\n".repeat(m as usize));
        return;
    }
    let fin: Vec<&[u8]> = (0..m).map(|_| tok.next().unwrap().as_bytes()).collect();
    // row r as a bit mask of its cells visited an odd number of times
    let odd: Vec<u64> = (0..m)
        .map(|_| {
            (0..n).fold(0u64, |mask, c| {
                let visits: u64 = tok.next().unwrap().parse().unwrap();
                mask | (visits & 1) << c
            })
        })
        .collect();
    // the offsets of integer length, the cell itself included
    let mut offsets = Vec::new();
    for dr in 1 - m..m {
        for dc in 1 - n..n {
            let q = dr * dr + dc * dc;
            let root = (q as f64).sqrt().round() as i64;
            if root * root == q {
                offsets.push((dr, dc));
            }
        }
    }
    let full = (1u64 << n) - 1;
    let mut out = String::new();
    for r in 0..m {
        // bit c is set when cell (r, c) was flipped an odd number of times
        let mut flips = 0u64;
        for &(dr, dc) in &offsets {
            if r + dr >= 0 && r + dr < m {
                let row = odd[(r + dr) as usize];
                let shifted = if dc >= 0 { row >> dc } else { row << -dc };
                flips ^= shifted & full;
            }
        }
        for c in 0..n {
            let black = (fin[r as usize][c as usize] == b'B') ^ (flips >> c & 1 == 1);
            out.push(if black { 'B' } else { 'W' });
        }
        out.push('\n');
    }
    print!("{}", out);
}
