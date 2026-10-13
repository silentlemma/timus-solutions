use std::io::{self, Read};

const SCALE: i64 = 100; // coordinates come with two decimals: work in hundredths
const SIZES: usize = 3; // A, B and C

fn hundredths(s: &str) -> i64 {
    let (whole, part) = match s.find('.') {
        Some(i) => (&s[..i], &s[i + 1..]),
        None => (s, ""),
    };
    let part = format!("{}00", part);
    let p: i64 = part[..2].parse().unwrap();
    let w: i64 = whole.parse().unwrap();
    w * SCALE + if s.starts_with('-') { -p } else { p }
}

/// The point of the box for a point of the net: the face A x B in the
/// middle of the column lies at z = 0 with its corner (c, b + c) at the
/// origin, and every other face folds up from it.
fn fold(a: i64, b: i64, c: i64, x: i64, y: i64) -> (i64, i64, i64) {
    if x < c {
        (0, y - b - c, c - x)
    } else if x > c + a {
        (a, y - b - c, x - c - a)
    } else if y < b {
        (x - c, b - y, c)
    } else if y < b + c {
        (x - c, 0, b + c - y)
    } else if y <= 2 * b + c {
        (x - c, y - b - c, 0)
    } else {
        (x - c, b, y - 2 * b - c)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let t: Vec<&str> = input.split_ascii_whitespace().collect();
    let size: Vec<i64> = t[..SIZES]
        .iter()
        .map(|v| v.parse::<i64>().unwrap() * SCALE)
        .collect();
    let (a, b, c) = (size[0], size[1], size[2]);
    let coords: Vec<i64> = t[SIZES..].iter().map(|v| hundredths(v)).collect();
    let points: Vec<(i64, i64, i64)> = coords
        .chunks(2)
        .map(|xy| fold(a, b, c, xy[0], xy[1]))
        .collect();
    let (p, q) = (points[0], points[1]);
    let squared = (p.0 - q.0).pow(2) + (p.1 - q.1).pow(2) + (p.2 - q.2).pow(2);
    println!("{:.10}", (squared as f64).sqrt() / SCALE as f64);
}
