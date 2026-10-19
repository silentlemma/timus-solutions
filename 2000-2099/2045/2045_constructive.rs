use std::io::{self, Read, Write};

const TAIL: &str = "bcd";

fn word_for(n: usize, count: usize, tail: &str) -> String {
    if count < n.min(TAIL.len()) {
        return "NO".to_string();
    }
    if n < TAIL.len() {
        return "a".repeat(n);
    }
    let prefix = count - TAIL.len();
    format!("{}{}", "a".repeat(prefix), &tail[..n - prefix])
}

fn solve(n: usize, out: &mut impl Write) {
    let tail = TAIL.repeat((n + TAIL.len() - 1) / TAIL.len());
    for count in 1..=n {
        writeln!(out, "{} : {}", count, word_for(n, count, &tail)).unwrap();
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n = input.trim().parse().unwrap();
    let mut out = io::BufWriter::new(io::stdout().lock());
    solve(n, &mut out);
}
