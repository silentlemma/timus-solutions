use std::io::{self, Read};

const TENTHS: f64 = 10.0;
const BRICK_SIDES: usize = 3;

// whether a p x q rectangle (p >= q) fits into an a x b one (a >= b); a
// turned fit (p > a, q <= b) needs ((a+b)/(p+q))^2 + ((a-b)/(p-q))^2 >= 2
// by Carver's criterion, multiplied out here to stay in integers
fn fits(p: i64, q: i64, a: i64, b: i64) -> bool {
    if q > b {
        return false;
    }
    if p <= a {
        return true;
    }
    let (s, d) = ((p + q) * (p + q), (p - q) * (p - q));
    (a + b) * (a + b) * d + (a - b) * (a - b) * s >= 2 * s * d
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| (x.parse::<f64>().unwrap() * TENTHS).round() as i64)
        .collect();
    let (mut brick, mut hole) = (v[..BRICK_SIDES].to_vec(), v[BRICK_SIDES..].to_vec());
    brick.sort();
    hole.sort();
    // the face of the two shorter sides is the easiest to put through
    let ok = fits(brick[1], brick[0], hole[1], hole[0]);
    println!("{}", if ok { "YES" } else { "NO" });
}
