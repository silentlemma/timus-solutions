use std::f64::consts::TAU;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let values: Vec<f64> = tokens.map(|t| t.parse().unwrap()).collect();
    let r = values[0];
    let points: Vec<(f64, f64)> = values[1..]
        .chunks(2)
        .take(n)
        .map(|p| (p[0], p[1]))
        .collect();
    // the straight parts are the sides of the polygon, the arcs around the
    // nails turn by 2*pi in total: one full circle of radius r
    let mut length = TAU * r;
    if n > 1 {
        for i in 0..n {
            let (a, b) = (points[i], points[(i + 1) % n]);
            length += (b.0 - a.0).hypot(b.1 - a.1);
        }
    }
    println!("{:.2}", length);
}
