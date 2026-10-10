use std::io::{self, Read};

const SQUARE: i64 = 8;

// Whether v is a perfect square, with the floating root corrected exactly.
fn is_square(v: i64) -> bool {
    let mut r = (v as f64).sqrt() as i64;
    while r * r > v {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= v {
        r += 1;
    }
    r * r == v
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let digits: Vec<&str> = v[1..1 + v[0] as usize]
        .iter()
        // the ones stand at 1 + m(m - 1) / 2, that is where 8(k - 1) + 1 is a
        // perfect square
        .map(|&k| {
            if is_square(SQUARE * (k - 1) + 1) {
                "1"
            } else {
                "0"
            }
        })
        .collect();
    println!("{}", digits.join(" "));
}
