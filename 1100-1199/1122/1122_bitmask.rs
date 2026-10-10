use std::io::{self, Read};

const SIZE: usize = 4;
const PATTERN: usize = 3;
const CELLS: usize = SIZE * SIZE;
const ALL: usize = (1 << CELLS) - 1;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let lines: Vec<&[u8]> = input
        .split_ascii_whitespace()
        .map(|s| s.as_bytes())
        .collect();
    let mut board = 0;
    for r in 0..SIZE {
        for c in 0..SIZE {
            if lines[r][c] == b'B' {
                board |= 1 << (r * SIZE + c);
            }
        }
    }
    let pattern = &lines[SIZE..SIZE + PATTERN];
    // the flips of a move in each cell, the pattern clipped at the edges
    let mut moves = [0usize; CELLS];
    for r in 0..SIZE {
        for c in 0..SIZE {
            for dr in 0..PATTERN {
                for dc in 0..PATTERN {
                    let (rr, cc) = ((r + dr) as i32 - 1, (c + dc) as i32 - 1);
                    let inside = rr >= 0 && rr < SIZE as i32 && cc >= 0 && cc < SIZE as i32;
                    if pattern[dr][dc] == b'1' && inside {
                        moves[r * SIZE + c] |= 1 << (rr as usize * SIZE + cc as usize);
                    }
                }
            }
        }
    }
    // moves commute and a second move in a cell undoes the first, so a
    // solution is a set of cells; flips[s] is the effect of the set s
    let mut flips = vec![0usize; 1 << CELLS];
    let mut best: Option<u32> = None;
    for s in 0..1usize << CELLS {
        if s > 0 {
            flips[s] = flips[s & (s - 1)] ^ moves[s.trailing_zeros() as usize];
        }
        if flips[s] == board || flips[s] == board ^ ALL {
            let count = s.count_ones();
            if best.map_or(true, |b| count < b) {
                best = Some(count);
            }
        }
    }
    match best {
        Some(b) => println!("{}", b),
        None => println!("Impossible"),
    }
}
