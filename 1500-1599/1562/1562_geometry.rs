use std::f64::consts::PI;
use std::io::{self, Read};

const QUARTER: f64 = 0.25;
const THIRD: f64 = 1.0 / 3.0;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let a: f64 = words.next().unwrap().parse().unwrap();
    let b: f64 = words.next().unwrap().parse().unwrap();
    let n: usize = words.next().unwrap().parse().unwrap();
    let half = b / 2.0;
    // the volume of the pineapple between its middle and height z: the
    // cross-section at z is a disc of area pi (a / 2)^2 (1 - (z / half)^2)
    let below = |z: f64| PI * a * a * QUARTER * (z - z * z * z * THIRD / (half * half));
    let mut out = String::new();
    for i in 0..n {
        let lo = -half + b * i as f64 / n as f64;
        let hi = -half + b * (i + 1) as f64 / n as f64;
        out.push_str(&format!("{:.6}\n", below(hi) - below(lo)));
    }
    print!("{}", out);
}
