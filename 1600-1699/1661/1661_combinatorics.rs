use std::io::{self, Read};

const EDGES: usize = 30;
const COLOURS: usize = 30;
const ROTATIONS: u128 = 60;
// the rotations other than the identity: how many there are and the cycle
// length on the edges; a half-turn also keeps two edges in place
const FACE_TURNS: (u128, usize) = (24, 5);
const VERTEX_TURNS: (u128, usize) = (20, 3);
const HALF_TURNS: (u128, usize) = (15, 2);

/// Colourings of cycles of this length that use each colour counts[c]
/// times, or 0 if some count does not split into whole cycles; 30! < 2^128.
fn cycles(counts: &[usize], length: usize) -> u128 {
    let mut ways: u128 = 1;
    let mut used: u128 = 0;
    for &c in counts {
        if c % length != 0 {
            return 0;
        }
        for i in 1..=(c / length) as u128 {
            used += 1;
            ways = ways * used / i;
        }
    }
    ways
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut counts = vec![0usize; COLOURS + 1];
    for w in text.split_ascii_whitespace().take(EDGES) {
        counts[w.parse::<usize>().unwrap()] += 1;
    }
    let mut total = cycles(&counts, 1);
    for (times, length) in [FACE_TURNS, VERTEX_TURNS] {
        total += times * cycles(&counts, length);
    }
    // a half-turn: colour the two kept edges first, in order
    let (times, length) = HALF_TURNS;
    let mut kept: u128 = 0;
    for a in 0..=COLOURS {
        for b in 0..=COLOURS {
            let mut rest = counts.clone();
            if rest[a] == 0 {
                continue;
            }
            rest[a] -= 1;
            if rest[b] == 0 {
                continue;
            }
            rest[b] -= 1;
            kept += cycles(&rest, length);
        }
    }
    total += times * kept;
    println!("{}", total / ROTATIONS);
}
