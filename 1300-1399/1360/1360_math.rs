use std::f64::consts::PI;
use std::io::{self, Read};

const TURN: f64 = 2.0 * PI;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (x0, y0, eps) = (v[0], v[1], v[2]);
    let across = x0.max(-1.0).min(1.0).asin();
    let up = y0.max(-1.0).min(1.0).acos();
    // take sqrt(t) = s0 with sin(s0) = x0 and s0 > 2 pi / eps; within pi of
    // t0 = s0^2 some t has cos(t) = y0, and sqrt(t) moves by less than eps / 4
    let s0 = across + TURN * ((1.0 / eps).ceil() + 1.0);
    let t0 = s0 * s0;
    let t = up + TURN * ((t0 - up) / TURN).round();
    println!("{:.6}", t);
}
