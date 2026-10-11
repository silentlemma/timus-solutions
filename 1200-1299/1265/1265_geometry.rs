use std::io::{self, Read};

const DIGITS: usize = 6; // the input has at most six digits after the point
const SCALE: i128 = 1_000_000;

// the number times 10^6 as an exact integer
fn scaled(token: &str) -> i128 {
    let sign = if token.starts_with('-') { -1 } else { 1 };
    let token = token.trim_start_matches(|c| c == '+' || c == '-');
    let (whole, frac) = token.split_once('.').unwrap_or((token, ""));
    let frac: String = frac
        .chars()
        .chain(std::iter::repeat('0'))
        .take(DIGITS)
        .collect();
    let whole: i128 = if whole.is_empty() {
        0
    } else {
        whole.parse().unwrap()
    };
    sign * (whole * SCALE + frac.parse::<i128>().unwrap())
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(scaled);
    let mut next = || it.next().unwrap();
    let (ex, ey, tx, ty) = (next(), next(), next(), next());
    let (ax, ay, bx, by) = (next(), next(), next(), next());
    // mirror from A along s; the eye and the target relative to A
    let (sx, sy) = (bx - ax, by - ay);
    let (ex, ey, tx, ty) = (ex - ax, ey - ay, tx - ax, ty - ay);
    // heights above the mirror line (times |s|), both on one side
    let (he, ht) = (sx * ey - sy * ex, sx * ty - sy * tx);
    if (he > 0) != (ht > 0) {
        println!("INVISIBLE");
        return;
    }
    // the ray to the target's image meets the line at the projections
    // weighted by the heights: u = (pe * ht + pt * he) / ((he + ht) |s|^2)
    let (pe, pt) = (sx * ex + sy * ey, sx * tx + sy * ty);
    let (mut num, mut den) = (pe * ht + pt * he, (he + ht) * (sx * sx + sy * sy));
    if den < 0 {
        num = -num;
        den = -den;
    }
    println!(
        "{}",
        if num >= 0 && num <= den {
            "VISIBLE"
        } else {
            "INVISIBLE"
        }
    );
}
