use std::io::{self, Read};

const KM: f64 = 1000.0; // input distances are in thousands of kilometres

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    // a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
    // inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
    let (a, b, c, d) = (next(), next(), next(), next());
    let den = a * b - c * d;
    let diff = a * a + b * b - c * c - d * d;
    if den == 0 || diff.abs() > 2 * den.abs() {
        println!("Impossible.");
        return;
    }
    let num = a * b * (c * c + d * d) - c * d * (a * a + b * b);
    let km = (KM * (num as f64 / den as f64).sqrt()).round();
    println!("Distance is {} km.", km as i64);
}
