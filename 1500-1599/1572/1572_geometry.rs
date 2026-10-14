use std::io::{self, Read};

/// Four times the square of the shortest longest chord of a cover of side or
/// radius 1: a circle's diameter, a square's side, a triangle's height.
const NARROWEST: [u64; 4] = [0, 16, 4, 3];
/// Four times the square of the longest segment in a hole: a circle's
/// diameter, a square's diagonal, a triangle's side.
const WIDEST: [u64; 4] = [0, 16, 8, 4];
const HEADER: usize = 3; // the well's type and size, and N

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<u64> = text
        .split_ascii_whitespace()
        .map(|w| w.parse().unwrap())
        .collect();
    let hole = WIDEST[v[0] as usize] * v[1] * v[1];
    let n = v[2] as usize;
    // a cover held upright crosses the plane of the hole along parallel chords,
    // so it passes when its longest chord in some direction fits in the hole
    let count = v[HEADER..]
        .chunks(2)
        .take(n)
        .filter(|c| NARROWEST[c[0] as usize] * c[1] * c[1] <= hole)
        .count();
    println!("{}", count);
}
