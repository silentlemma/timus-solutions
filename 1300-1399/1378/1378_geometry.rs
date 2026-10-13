use std::f64::consts::PI;
use std::io::{self, Read};

// from the centre, r1 reaches the farthest point and r2 reaches across it:
// area / (pi r1 r2) is 1 for any oval and 2 / pi for a square, and
// area / (pi r1^2) is 2 / pi for a square, at most 0.41 for a triangle
const OVAL: f64 = 0.8;
const SQUARE: f64 = 0.5;
const HALF: f64 = 0.5; // a pixel reaches half a pixel beyond its centre

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let w: usize = words.next().unwrap().parse().unwrap();
    let h: usize = words.next().unwrap().parse().unwrap();
    let pic: Vec<u8> = words.flat_map(|t| t.bytes()).collect();
    let mut ends: Vec<(f64, f64)> = Vec::new(); // the first and last pixel of each row
    let (mut count, mut sx, mut sy) = (0.0, 0.0, 0.0);
    for y in 0..h {
        let row = &pic[y * w..(y + 1) * w];
        let mut first = None;
        let mut last = 0;
        for (x, &ch) in row.iter().enumerate() {
            if ch == b'1' {
                first.get_or_insert(x);
                last = x;
                count += 1.0;
                sx += x as f64;
                sy += y as f64;
            }
        }
        if let Some(f) = first {
            ends.push((f as f64, y as f64));
            ends.push((last as f64, y as f64));
        }
    }
    let (cx, cy) = (sx / count, sy / count);
    let dist = |p: &(f64, f64)| (p.0 - cx).hypot(p.1 - cy);
    let far = *ends
        .iter()
        .max_by(|a, b| dist(a).partial_cmp(&dist(b)).unwrap())
        .unwrap();
    let r1 = dist(&far);
    let (ux, uy) = ((far.0 - cx) / r1, (far.1 - cy) / r1);
    let r2 = ends
        .iter()
        .map(|p| ((p.1 - cy) * ux - (p.0 - cx) * uy).abs())
        .fold(0.0, f64::max);
    let answer = if count / (PI * (r1 + HALF) * (r2 + HALF)) > OVAL {
        "circle"
    } else if count / (PI * (r1 + HALF) * (r1 + HALF)) > SQUARE {
        "square"
    } else {
        "triangle"
    };
    println!("{}", answer);
}
