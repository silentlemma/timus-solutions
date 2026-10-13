use std::fmt::Write as _;
use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, x, y) = (v[0], v[1], v[2]);
    let size = 1usize << n;
    let mut board = vec![vec![0u32; size]; size];
    let mut count = 0u32;
    // each square has one cell that is already taken: the hole or a piece of
    // the tromino in the middle of the square above it; a square is
    // (top, left, side, hole row, hole column)
    let mut stack = vec![(0usize, 0usize, size, x - 1, y - 1)];
    while let Some((top, left, side, hr, hc)) = stack.pop() {
        if side == 1 {
            continue;
        }
        let half = side / 2;
        count += 1;
        for dr in 0..2 {
            for dc in 0..2 {
                let (r0, c0) = (top + dr * half, left + dc * half);
                if (r0..r0 + half).contains(&hr) && (c0..c0 + half).contains(&hc) {
                    stack.push((r0, c0, half, hr, hc));
                } else {
                    // the cell of this quarter next to the middle of the square
                    let (r, c) = (top + half - 1 + dr, left + half - 1 + dc);
                    board[r][c] = count;
                    stack.push((r0, c0, half, r, c));
                }
            }
        }
    }
    let mut out = String::new();
    for row in &board {
        for (c, v) in row.iter().enumerate() {
            write!(out, "{}", v).unwrap();
            out.push(if c + 1 < size { ' ' } else { '\n' });
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
