use std::io::{self, BufRead, Write};

const MAX_VALUE: usize = 5000;

fn main() {
    let input = io::stdin();
    let mut input = input.lock();
    let mut line = String::new();
    input.read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    // one value per input line; retain only the bounded-domain frequencies.
    let mut counts = [0u32; MAX_VALUE + 1];
    for _ in 0..n {
        line.clear();
        input.read_line(&mut line).unwrap();
        let value: usize = line.trim().parse().unwrap();
        counts[value] += 1;
    }
    for value in 1..=MAX_VALUE {
        counts[value] += counts[value - 1];
    }
    line.clear();
    input.read_line(&mut line).unwrap();
    line.clear();
    input.read_line(&mut line).unwrap();
    let k: usize = line.trim().parse().unwrap();
    let mut out = io::BufWriter::new(io::stdout().lock());
    for _ in 0..k {
        line.clear();
        input.read_line(&mut line).unwrap();
        let rank: u32 = line.trim().parse().unwrap();
        let (mut low, mut high) = (1, MAX_VALUE);
        while low < high {
            let mid = (low + high) / 2;
            if counts[mid] < rank {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        writeln!(out, "{}", low).unwrap();
    }
}
