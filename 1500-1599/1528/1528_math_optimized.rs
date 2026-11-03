use std::io::{self, BufWriter, Read, Write};

const BUFFER_SIZE: usize = 4096;

fn main() {
    let mut raw = String::new();
    io::stdin().read_to_string(&mut raw).unwrap();
    let mut input = raw
        .split_ascii_whitespace()
        .map(|token| token.parse::<u64>().unwrap());
    let stdout = io::stdout();
    let mut out = BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    while let Some(n) = input.next() {
        let p = input.next().unwrap();
        if n == 0 && p == 0 {
            break;
        }
        let mut result = if n >= p { 0 } else { 1 };
        let mut i = 2;
        // u64 safely holds (p-1)*i*(i+1), which is less than2e17.
        while i + 1 <= n && result != 0 {
            result = result * i * (i + 1) % p;
            i += 2;
        }
        if i <= n && result != 0 {
            result = result * i % p;
        }
        writeln!(out, "{}", result).unwrap();
    }
}
