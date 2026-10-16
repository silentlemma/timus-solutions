use std::cmp::Reverse;
use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u32> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = v[0] as usize;
    let mut pieces: Vec<(u32, u32)> =
        (0..n).map(|i| (v[1 + 2 * i].min(v[2 + 2 * i]), v[1 + 2 * i].max(v[2 + 2 * i]))).collect();
    // a domino is a range [low, high]; standing upright as (low, high) or
    // flipped as (high, low), two of a kind fit together when nested, and
    // one of each when they overlap; the two kinds are nested chains
    pieces.sort_by_key(|&(low, high)| (low, Reverse(high)));
    let mut upright: Vec<(u32, u32)> = Vec::new();
    let mut flipped: Vec<(u32, u32)> = Vec::new();
    for &p in &pieces {
        if upright.last().map_or(true, |q| p.1 <= q.1) {
            upright.push(p);
        } else if flipped.last().map_or(true, |q| p.1 <= q.1) {
            flipped.push(p);
        } else {
            println!("NO");
            return;
        }
    }
    // the innermost ranges of the two chains meet in the middle
    if let (Some(a), Some(b)) = (upright.last(), flipped.last()) {
        if a.1 < b.0 || b.1 < a.0 {
            println!("NO");
            return;
        }
    }
    let mut out = String::from("YES\n");
    for &(low, high) in &upright {
        writeln!(out, "{} {}", low, high).unwrap();
    }
    for &(low, high) in flipped.iter().rev() {
        writeln!(out, "{} {}", high, low).unwrap();
    }
    print!("{}", out);
}
