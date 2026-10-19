use std::io::{self, Read};

const FOCAL_SCALE: f64 = 3.0;
const AXIS_SCALE: f64 = 6.0;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let sides: Vec<i64> = text
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    let (x, y, z) = (
        sides[0] * sides[0],
        sides[1] * sides[1],
        sides[2] * sides[2],
    );
    let discriminant = 2 * ((x - y) * (x - y) + (y - z) * (y - z) + (z - x) * (z - x));
    let gap = (discriminant as f64).sqrt();
    let focal_distance = (2.0 * gap).sqrt() / FOCAL_SCALE;
    let radius = ((x + y + z) as f64 + gap).sqrt() / AXIS_SCALE;
    println!("{:.12} {:.12}", focal_distance, radius);
}
