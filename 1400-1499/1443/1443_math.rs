use std::io::{self, Read};

const DIGITS: usize = 4; // lengths are given to a tenth of a millimetre

/// A length in tenths of a millimetre, read exactly.
fn tenths(text: &str) -> i64 {
    let (whole, frac) = text.split_once('.').unwrap_or((text, ""));
    let padded = format!("{:0<width$}", frac, width = DIGITS);
    let w: i64 = if whole.is_empty() {
        0
    } else {
        whole.parse().unwrap()
    };
    let f: i64 = padded[..DIGITS].parse().unwrap();
    w * 10i64.pow(DIGITS as u32) + f
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();
    let n: i64 = it.next().unwrap().parse().unwrap();
    let s = tenths(it.next().unwrap());
    let rail = tenths(it.next().unwrap());
    let (full, rest) = (s / rail, s % rail);
    if rest == 0 {
        println!("{}", n * full);
        return;
    }
    // each line takes its full rails and a short piece; a rail holds rail / rest such pieces
    let per_rail = rail / rest;
    println!("{}", n * full + (n + per_rail - 1) / per_rail);
}
