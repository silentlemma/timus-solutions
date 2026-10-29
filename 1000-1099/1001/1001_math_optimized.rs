use std::io::{self, BufWriter, Read, Write};

const MAX_INPUT: usize = 256 * 1024;
const SCALE: u64 = 10000;
const ROUNDING_OFFSET: f64 = 0.5;

fn main() {
    let mut input = String::with_capacity(MAX_INPUT);
    io::stdin().read_to_string(&mut input).unwrap();
    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());
    for token in input.split_ascii_whitespace().rev() {
        let value: u64 = token.parse().unwrap();
        // four decimals by hand: the root times 10^4, rounded, printed as the
        // integer part and the fraction, faster than formatting the float
        let scaled = ((value as f64).sqrt() * SCALE as f64 + ROUNDING_OFFSET) as u64;
        writeln!(out, "{}.{:04}", scaled / SCALE, scaled % SCALE).unwrap();
    }
    out.flush().unwrap();
}
