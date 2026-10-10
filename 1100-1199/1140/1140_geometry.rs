use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let n: usize = tok.next().unwrap().parse().unwrap();
    let (mut sx, mut sy, mut sz) = (0i64, 0i64, 0i64);
    for _ in 0..n {
        let d = tok.next().unwrap();
        let len: i64 = tok.next().unwrap().parse().unwrap();
        match d {
            "X" => sx += len,
            "Y" => sy += len,
            _ => sz += len,
        }
    }
    // a step along Y is a step along X and one along Z, so the walk ends at
    // a X + b Z; going back with m steps along Y costs |a - m| + |m| + |b - m|,
    // which is smallest at the median of a, 0 and b
    let (a, b) = (sx + sy, sz + sy);
    let m = a.min(b).max(a.max(b).min(0));
    let back: Vec<(&str, i64)> = [("X", m - a), ("Y", -m), ("Z", m - b)]
        .into_iter()
        .filter(|&(_, len)| len != 0)
        .collect();
    println!("{}", back.len());
    for (d, len) in back {
        println!("{} {}", d, len);
    }
}
