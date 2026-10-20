use std::io::{self, Read};

const SIDE: usize = 3; // seats on each side of the aisle
const MASKS: usize = 1 << SIDE;
const RIGHT_START: usize = 6; // the right seats in a row description
const LETTERS: &[u8] = b"ABCDEF";

// The largest set of free, pairwise non-adjacent seats on one side, as a mask
// per row; seats in a row and in the next row may not share a column or stand
// next to each other.
fn best_side(rows: &[&[u8]], offset: usize) -> Vec<usize> {
    let n = rows.len();
    let mut best = vec![[-1i32; MASKS]; n + 1];
    let mut from = vec![[0usize; MASKS]; n + 1];
    best[0][0] = 0;
    for (r, row) in rows.iter().enumerate() {
        let free = (0..SIDE).filter(|&s| row[offset + s] == b'.').fold(0, |m, s| m | 1 << s);
        for cur in 0..MASKS {
            if cur & !free != 0 || cur & (cur << 1) != 0 {
                continue;
            }
            let count = cur.count_ones() as i32;
            for prev in 0..MASKS {
                if best[r][prev] < 0 || (prev | prev << 1 | prev >> 1) & cur != 0 {
                    continue;
                }
                if best[r][prev] + count > best[r + 1][cur] {
                    best[r + 1][cur] = best[r][prev] + count;
                    from[r + 1][cur] = prev;
                }
            }
        }
    }
    let mut mask = (0..MASKS).max_by_key(|&m| (best[n][m], std::cmp::Reverse(m))).unwrap();
    let mut chosen = vec![0; n];
    for r in (1..=n).rev() {
        chosen[r - 1] = mask;
        mask = from[r][mask];
    }
    chosen
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let k: usize = it.next().unwrap().parse().unwrap();
    let rows: Vec<&[u8]> = it.take(n).map(|t| t.as_bytes()).collect();
    let mut seats = Vec::new();
    for half in 0..2 {
        let chosen = best_side(&rows, half * RIGHT_START);
        for (r, &mask) in chosen.iter().enumerate() {
            for s in 0..SIDE {
                if mask >> s & 1 == 1 {
                    seats.push(format!("{}{}", r + 1, LETTERS[half * SIDE + s] as char));
                }
            }
        }
    }
    if seats.len() < k {
        println!("PORAZHENIE");
        return;
    }
    println!("POBEDA\n{}", seats[..k].join("\n"));
}
