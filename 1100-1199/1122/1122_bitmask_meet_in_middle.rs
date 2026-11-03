use std::collections::HashMap;
use std::io::{self, Read};

const SIZE: usize = 4;
const PATTERN: usize = 3;
const CELLS: usize = SIZE * SIZE;
const ALL: usize = (1 << CELLS) - 1;
const HALF: usize = CELLS / 2;

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
    // Split the commuting moves in half and match their XOR effects.
    // Duplicate left effects retain only the cheapest number of moves.
    let mut left = HashMap::<usize, u32>::new();
    let mut effect = 0;
    for step in 0..(1usize << HALF) {
        if step > 0 {
            effect ^= moves[step.trailing_zeros() as usize];
        }
        let count = (step ^ (step >> 1)).count_ones();
        left.entry(effect)
            .and_modify(|old| *old = (*old).min(count))
            .or_insert(count);
    }
    let mut best = CELLS as u32 + 1;
    effect = 0;
    for step in 0..(1usize << HALF) {
        if step > 0 {
            effect ^= moves[HALF + step.trailing_zeros() as usize];
        }
        let count = (step ^ (step >> 1)).count_ones();
        for target in [board ^ effect, board ^ ALL ^ effect] {
            if let Some(&other) = left.get(&target) {
                best = best.min(count + other);
            }
        }
    }
    if best > CELLS as u32 {
        println!("Impossible");
    } else {
        println!("{}", best);
    }
}
