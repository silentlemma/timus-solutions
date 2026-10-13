use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    // the soldiers to turn, for an all-W parade
    let turn: Vec<Vec<u8>> = (0..n)
        .map(|_| {
            it.next()
                .unwrap()
                .bytes()
                .map(|c| (c == b'B') as u8)
                .collect()
        })
        .collect();
    // pressing every cell of row a and column b turns only (a, b) when N is
    // even, so (i, j) is pressed when its row, its column and itself add up odd
    let mut row = vec![0u8; n];
    let mut col = vec![0u8; n];
    for i in 0..n {
        for j in 0..n {
            row[i] ^= turn[i][j];
            col[j] ^= turn[i][j];
        }
    }
    let mut total = 0usize;
    for i in 0..n {
        for j in 0..n {
            total += (row[i] ^ col[j] ^ turn[i][j]) as usize;
        }
    }
    // an all-B parade needs exactly the other cells
    let flip = (2 * total > n * n) as u8;
    if flip == 1 {
        total = n * n - total;
    }
    let mut out = String::new();
    writeln!(out, "{}", total).unwrap();
    for i in 0..n {
        for j in 0..n {
            if row[i] ^ col[j] ^ turn[i][j] != flip {
                writeln!(out, "{} {}", i + 1, j + 1).unwrap();
            }
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
