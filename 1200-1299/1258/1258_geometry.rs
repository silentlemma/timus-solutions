use std::io::{self, Read};

// the distance along one axis once the room is mirrored at each hit
fn unfolded(start: i64, end: i64, size: i64, low: u8, hits: &[u8]) -> i64 {
    match (hits.first(), hits.last()) {
        (Some(&a), Some(&b)) => {
            let first = if a == low { start } else { size - start };
            let last = if b == low { end } else { size - end };
            first + (hits.len() as i64 - 1) * size + last
        }
        _ => (end - start).abs(),
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut next = || tokens.next().unwrap().parse::<i64>().unwrap();
    let (w, d, x0, y0, x1, y1) = (next(), next(), next(), next(), next(), next());
    let walls: Vec<u8> = tokens.flat_map(|t| t.bytes()).collect();
    let side: Vec<u8> = walls
        .iter()
        .copied()
        .filter(|&c| c == b'L' || c == b'R')
        .collect();
    let ends: Vec<u8> = walls
        .iter()
        .copied()
        .filter(|&c| c == b'F' || c == b'B')
        .collect();
    let dx = unfolded(x0, x1, w, b'L', &side);
    let dy = unfolded(y0, y1, d, b'F', &ends);
    println!("{:.4}", ((dx * dx + dy * dy) as f64).sqrt());
}
