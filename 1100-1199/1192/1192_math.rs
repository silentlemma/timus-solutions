use std::io;

const GRAVITY: f64 = 10.0;
const PI: f64 = 3.1415926535; // the value the statement fixes
const HALF_TURN: f64 = 180.0;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let v: Vec<f64> = line
        .split_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (speed, angle, k) = (v[0], v[1], v[2]);
    // one flight covers v^2 sin(2a) / g; every bounce keeps the angle and
    // divides v^2 by k, so the flights form a geometric series with ratio 1/k
    let flight = speed * speed * (2.0 * angle * PI / HALF_TURN).sin() / GRAVITY;
    println!("{:.2}", flight * k / (k - 1.0));
}
