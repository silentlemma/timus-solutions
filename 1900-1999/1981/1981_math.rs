use std::io::{self, Read, Write};

const FORBIDDEN_CHOICES: u64 = 3;

fn count(n: u64) -> (u64, u64) {
    if n % 2 != 0 {
        let size = (n - FORBIDDEN_CHOICES) / 2;
        return (if size >= 2 { n * size } else { 0 }, 0);
    }
    let half = n / 2;
    let first = half - 1;
    let second = half - 2;
    (
        half * ((if first >= 2 { first } else { 0 }) + (if second >= 2 { second } else { 0 })),
        half * (n - FORBIDDEN_CHOICES),
    )
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: u64 = match text.split_whitespace().next() {
        Some(s) => s.parse().unwrap(),
        None => return,
    };
    let (parallel, perpendicular) = count(n);
    let mut out = io::BufWriter::new(io::stdout().lock());
    writeln!(out, "{} {}", parallel, perpendicular).unwrap();
}
