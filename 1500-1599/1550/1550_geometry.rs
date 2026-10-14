use std::f64::consts::PI;
use std::io::{self, Read};

const THIRD: f64 = 1.0 / 3.0; // a pyramid is a third of its prism

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s
        .split_ascii_whitespace()
        .map(|x| x.parse::<f64>().unwrap());
    let mut next = || it.next().unwrap();
    let (h, w, x, y, r) = (next(), next(), next(), next(), next());
    // the hole meets no edge, so it lies over a single face, where the height
    // is linear: the cut-out volume is the hole's area times the height at
    // its centre, and that height falls from H to 0 with max(|x|, |y|)
    let centre = h * (1.0 - x.abs().max(y.abs()) / (w / 2.0));
    println!("{:.5}", h * w * w * THIRD - PI * r * r * centre);
}
