use std::fmt::Write;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let mut read = || {
        let n = tok.next().unwrap() as usize;
        (0..n)
            .map(|_| {
                (
                    tok.next().unwrap(),
                    tok.next().unwrap(),
                    tok.next().unwrap(),
                )
            })
            .collect::<Vec<_>>()
    };
    let (first, second) = (read(), read());
    let mut out = Vec::new();
    let mut j = 0;
    for &(a, b, y) in &first {
        let mut cur = a;
        // walk through [a, b) and keep what no interval of the second covers
        while cur < b {
            while j < second.len() && second[j].1 <= cur {
                j += 1;
            }
            if j < second.len() && second[j].0 <= cur {
                cur = second[j].1;
                continue;
            }
            let end = if j < second.len() {
                b.min(second[j].0)
            } else {
                b
            };
            out.push((cur, end, y));
            cur = end;
        }
    }
    let mut s = out.len().to_string();
    for (a, b, y) in out {
        write!(s, " {} {} {}", a, b, y).unwrap();
    }
    println!("{}", s);
}
