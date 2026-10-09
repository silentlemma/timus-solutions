use std::f64::consts::PI;
use std::io::{self, Read};

const SIDES: f64 = 4.0;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (a, r) = (v[0], v[1]);
    let half = a / 2.0;
    let area = if r <= half {
        PI * r * r
    } else if r * r >= 2.0 * half * half {
        a * a
    } else {
        // the circle minus the four caps cut off by the sides
        let cap = r * r * (half / r).acos() - half * (r * r - half * half).sqrt();
        PI * r * r - SIDES * cap
    };
    println!("{:.3}", area);
}
