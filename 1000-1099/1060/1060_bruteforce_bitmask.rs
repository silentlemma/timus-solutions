use std::io::{self, Read};

const SIZE: i32 = 4;
const CELLS: usize = (SIZE * SIZE) as usize;
const STEPS: [(i32, i32); 5] = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let rows: Vec<&[u8]> = input
        .split_ascii_whitespace()
        .map(|s| s.as_bytes())
        .collect();
    // the board as 16 bits, bit r * 4 + c set for a black piece
    let mut board = 0u32;
    for r in 0..SIZE {
        for c in 0..SIZE {
            if rows[r as usize][c as usize] == b'b' {
                board |= 1 << (r * SIZE + c);
            }
        }
    }
    // the pieces turned by a move at each cell
    let mut moves = Vec::new();
    for r in 0..SIZE {
        for c in 0..SIZE {
            let mut m = 0u32;
            for (dr, dc) in STEPS {
                let (rr, cc) = (r + dr, c + dc);
                if (0..SIZE).contains(&rr) && (0..SIZE).contains(&cc) {
                    m |= 1 << (rr * SIZE + cc);
                }
            }
            moves.push(m);
        }
    }
    // moves commute and a move made twice cancels, so a solution is a set of
    // cells: try all 2^16 sets
    let all = (1u32 << CELLS) - 1;
    let mut best: Option<u32> = None;
    for set in 0..=all {
        let mut b = board;
        for (i, m) in moves.iter().enumerate() {
            if set >> i & 1 == 1 {
                b ^= m;
            }
        }
        if b == 0 || b == all {
            let count = set.count_ones();
            best = Some(best.map_or(count, |x| x.min(count)));
        }
    }
    match best {
        Some(k) => println!("{}", k),
        None => println!("Impossible"),
    }
}
