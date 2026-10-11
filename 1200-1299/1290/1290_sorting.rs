use std::io::{self, BufWriter, Read, Write};

const LARGEST: usize = 25000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    // counting each value is a sort in descending order, and printing the
    // conjugate partition twice gives back the sorted array
    let mut count = vec![0usize; LARGEST + 1];
    for p in it.take(n) {
        count[p] += 1;
    }
    let mut out = BufWriter::new(io::stdout().lock());
    for value in (1..=LARGEST).rev() {
        for _ in 0..count[value] {
            writeln!(out, "{}", value).unwrap();
        }
    }
}
