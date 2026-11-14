use std::io::{self, Read};

const SIDE_SEATS: usize = 3;
const RIGHT_START: usize = 6;
const STATE_COUNT: usize = 5;
const UNREACHABLE: i32 = -1000;
const MASKS: [u8; STATE_COUNT] = [0, 1, 2, 1 << 2, 1 | (1 << 2)];
const PEOPLE: [i32; STATE_COUNT] = [0, 1, 1, 1, 2];

fn arrange(rows: &mut [u8]) -> i32 {
    let mut previous = vec![[0u8; STATE_COUNT]; rows.len()];
    let mut scores = [UNREACHABLE; STATE_COUNT];
    scores[0] = 0;
    for (row, &free) in rows.iter().enumerate() {
        let mut next = [UNREACHABLE; STATE_COUNT];
        for (state, &mask) in MASKS.iter().enumerate() {
            if mask & free != mask {
                continue;
            }
            let blocked = mask | (mask << 1) | (mask >> 1);
            let mut best = 0;
            for (prior, &other) in MASKS.iter().enumerate() {
                if blocked & other == 0 && scores[prior] > scores[best] {
                    best = prior;
                }
            }
            next[state] = scores[best] + PEOPLE[state];
            previous[row][state] = best as u8;
        }
        scores = next;
    }
    let mut state = (0..STATE_COUNT).max_by_key(|&i| scores[i]).unwrap();
    let count = scores[state];
    for (row, mask) in rows.iter_mut().enumerate().rev() {
        *mask = MASKS[state];
        state = usize::from(previous[row][state]);
    }
    count
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut needed: i32 = words.next().unwrap().parse().unwrap();
    let mut rows = [vec![0u8; n], vec![0u8; n]];
    for (row, layout) in words.take(n).enumerate() {
        for (side, seats) in rows.iter_mut().enumerate() {
            for column in 0..SIDE_SEATS {
                if layout.as_bytes()[side * RIGHT_START + column] == b'.' {
                    seats[row] |= 1 << column;
                }
            }
        }
    }
    let total: i32 = rows.iter_mut().map(|side| arrange(side)).sum();
    if total < needed {
        println!("PORAZHENIE");
        return;
    }
    println!("POBEDA");
    for (side, seats) in rows.iter().enumerate() {
        for (row, &mask) in seats.iter().enumerate() {
            for column in 0..SIDE_SEATS {
                if mask & (1 << column) != 0 {
                    let letter = char::from(b'A' + (side * SIDE_SEATS + column) as u8);
                    println!("{}{letter}", row + 1);
                    needed -= 1;
                    if needed == 0 {
                        return;
                    }
                }
            }
        }
    }
}
