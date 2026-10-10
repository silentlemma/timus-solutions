use std::f64::consts::PI;
use std::io::{self, Read};

// halvings of the radius interval; far more than double precision needs
const STEPS: usize = 200;

// the largest area belongs to the polygon inscribed in a circle; a side of
// length l sees the centre at the angle 2 asin(l / 2R)
fn angle(length: f64, r: f64) -> f64 {
    2.0 * (length / (2.0 * r)).min(1.0).asin()
}

fn sum(v: &[i64], r: f64) -> f64 {
    v.iter().map(|&s| angle(s as f64, r)).sum()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = tok.next().unwrap() as usize;
    let mut sides: Vec<i64> = tok.take(n).collect();
    sides.sort();
    let longest = sides[n - 1];
    let rest = &sides[..n - 1];
    if longest >= rest.iter().sum::<i64>() {
        println!("0.00");
        return;
    }
    let mut low = longest as f64 / 2.0;
    let inside = sum(&sides, low) >= 2.0 * PI;
    // with the centre inside, the angles fill the full turn; otherwise the
    // longest side's angle equals the sum of the others
    let surplus = |r: f64| {
        if inside {
            sum(&sides, r) - 2.0 * PI
        } else {
            angle(longest as f64, r) - sum(rest, r)
        }
    };
    let mut high = low;
    while surplus(high) > 0.0 {
        high *= 2.0;
    }
    for _ in 0..STEPS {
        let mid = (low + high) / 2.0;
        if surplus(mid) > 0.0 {
            low = mid;
        } else {
            high = mid;
        }
    }
    let r = (low + high) / 2.0;
    let sign = if inside { 1.0 } else { -1.0 };
    let area: f64 = rest.iter().map(|&s| angle(s as f64, r).sin()).sum::<f64>()
        + sign * angle(longest as f64, r).sin();
    println!("{:.2}", r * r * area / 2.0);
}
