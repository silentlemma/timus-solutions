use std::io::{self, Read, Write};

const MAX_SIDE: usize = 50;
const MAX_SQUARED: usize = 2 * MAX_SIDE * MAX_SIDE;
const COLOUR_XOR: u8 = b'W' ^ b'B';

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_ascii_whitespace();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    if m == 0 || n == 0 {
        for _ in 0..m {
            out.write_all(b"\n").unwrap();
        }
        return;
    }
    let mut board: Vec<Vec<u8>> = (0..m)
        .map(|_| tokens.next().unwrap().as_bytes().to_vec())
        .collect();
    let mut square = [false; MAX_SQUARED];
    let mut k = 0;
    while k * k < MAX_SQUARED {
        square[k * k] = true;
        k += 1;
    }
    let mut offsets = Vec::new();
    for dr in 1 - (m as isize)..m as isize {
        for dc in 1 - (n as isize)..n as isize {
            if square[(dr * dr + dc * dc) as usize] {
                offsets.push((dr, dc));
            }
        }
    }
    // A flip is its own inverse; visits of even multiplicity cancel.
    for r in 0..m {
        for c in 0..n {
            let visits: u32 = tokens.next().unwrap().parse().unwrap();
            if visits & 1 != 0 {
                for &(dr, dc) in &offsets {
                    let a = r as isize + dr;
                    let b = c as isize + dc;
                    if a >= 0 && a < m as isize && b >= 0 && b < n as isize {
                        board[a as usize][b as usize] ^= COLOUR_XOR;
                    }
                }
            }
        }
    }
    for row in board {
        out.write_all(&row).unwrap();
        out.write_all(b"\n").unwrap();
    }
}
