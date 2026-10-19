use std::f64::consts::PI;
use std::io::{self, Read};

// area common to discs of radii a and b with centres d apart
fn lens(d: i64, a: i64, b: i64) -> f64 {
    if d >= a + b {
        return 0.0;
    }
    if d <= (a - b).abs() {
        let small = a.min(b) as f64;
        return PI * small * small;
    }
    let (fd, fa, fb) = (d as f64, a as f64, b as f64);
    // half-angles seen from each centre, by the law of cosines
    let alpha = ((d * d + a * a - b * b) as f64 / (2.0 * fd * fa)).acos();
    let beta = ((d * d + b * b - a * a) as f64 / (2.0 * fd * fb)).acos();
    // the kite between both centres and the two crossing points
    let kite = ((-d + a + b) as f64 * (d + a - b) as f64 * (d - a + b) as f64 * (d + a + b) as f64)
        .sqrt()
        / 2.0;
    fa * fa * alpha + fb * fb * beta - kite
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (d, r1, big1, r2, big2) = (next(), next(), next(), next(), next());
    let ring1 = PI * (big1 * big1 - r1 * r1) as f64;
    let ring2 = PI * (big2 * big2 - r2 * r2) as f64;
    // a ring is a disc minus a smaller one, so their overlap follows by
    // inclusion and exclusion over the four pairs of discs
    let common = lens(d, big1, big2) - lens(d, r1, big2) - lens(d, big1, r2) + lens(d, r1, r2);
    println!("{:.6}", ring1 + ring2 - common);
}
