use std::io::{self, Read};

// the distance along one axis once the room is mirrored at each hit
fn unfolded(start: i64, end: i64, size: i64, low: u8, hits: (usize, u8, u8)) -> i64 {
    if hits.0 == 0 {
        return (end - start).abs();
    }
    let first = if hits.1 == low { start } else { size - start };
    let last = if hits.2 == low { end } else { size - end };
    first + (hits.0 as i64 - 1) * size + last
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut next = || tokens.next().unwrap().parse::<i64>().unwrap();
    let (w, d, x0, y0, x1, y1) = (next(), next(), next(), next(), next(), next());
    let (mut side, mut ends) = ((0, 0, 0), (0, 0, 0));
    for c in tokens.flat_map(str::bytes) {
        let hits = match c {
            b'L' | b'R' => &mut side,
            b'F' | b'B' => &mut ends,
            _ => continue,
        };
        if hits.0 == 0 {
            hits.1 = c;
        }
        hits.0 += 1;
        hits.2 = c;
    }
    let dx = unfolded(x0, x1, w, b'L', side);
    let dy = unfolded(y0, y1, d, b'F', ends);
    println!("{:.4}", ((dx * dx + dy * dy) as f64).sqrt());
}
