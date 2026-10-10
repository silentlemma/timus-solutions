use std::io::{self, Read};

const CENTS: i64 = 100;
const PEAK: i64 = 2 * CENTS;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let t: Vec<&str> = input.split_ascii_whitespace().collect();
    let a = (t[0].parse::<f64>().unwrap() * CENTS as f64).round() as i64;
    let b = (t[1].parse::<f64>().unwrap() * CENTS as f64).round() as i64;
    let k: i64 = t[2].parse().unwrap();
    // everything is in kopecks: x horns earn a * x - 100 * x^2
    let (mut best, mut best_x, mut best_y) = (-1, 0, 0);
    let y_peak = b.max(0) / PEAK;
    for x in 0..=k {
        let (room, gain_x) = (k - x, a * x - CENTS * x * x);
        // the hoof profit is concave in y, so the best y is next to its peak
        for y in [y_peak.min(room), (y_peak + 1).min(room)] {
            let total = gain_x + b * y - CENTS * y * y;
            if total > best {
                best = total;
                best_x = x;
                best_y = y;
            }
        }
    }
    println!(
        "{}.{:02}\n{} {}",
        best / CENTS,
        best % CENTS,
        best_x,
        best_y
    );
}
