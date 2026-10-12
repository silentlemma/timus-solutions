use std::io::{self, Read};

const STRIPS: usize = 20000;
const PERCENT: f64 = 100.0;
const MIDDLE: f64 = 0.5; // where in its strip the line is taken

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut value = || it.next().unwrap().parse::<f64>().unwrap();
    let bombs: Vec<(f64, f64, f64)> = (0..n).map(|_| (value(), value(), value())).collect();
    // the area is the sum over thin vertical strips of the covered part of
    // the line through the middle of each strip
    let mut covered = 0.0;
    let mut pieces: Vec<(f64, f64)> = Vec::new();
    for k in 0..STRIPS {
        let x = (k as f64 + MIDDLE) / STRIPS as f64;
        pieces.clear();
        for &(cx, cy, r) in &bombs {
            if (x - cx).abs() < r {
                let half = (r * r - (x - cx) * (x - cx)).sqrt();
                let (low, high) = ((cy - half).max(0.0), (cy + half).min(1.0));
                if low < high {
                    pieces.push((low, high));
                }
            }
        }
        pieces.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let mut end = 0.0;
        for &(low, high) in &pieces {
            if high > end {
                covered += high - low.max(end);
                end = high;
            }
        }
    }
    println!("{:.6}", covered / STRIPS as f64 * PERCENT);
}
