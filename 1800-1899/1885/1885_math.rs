use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input.split_ascii_whitespace().map(|s| s.parse().unwrap()).collect();
    let (h, t, speed, x) = (v[0], v[1], v[2], v[2 + 1]);
    // the least time climbs at x as long as possible and at full speed in
    // the remaining seconds; the most climbs just faster than x, or during
    // all t seconds when that is too slow to reach h
    let least = (h - t * x).max(0.0) / (speed - x);
    let most = t.min(h / x);
    println!("{:.6} {:.6}", least, most);
}
