use std::io::{self, BufWriter, Read, Write};

const PERCENT: f64 = 100.0;

// the numbers are parsed by hand from the bytes of the locked standard
// input instead of reading the whole input into a string
fn read_int(input: &mut impl Iterator<Item = io::Result<u8>>) -> usize {
    let mut value = 0;
    let mut started = false;
    for byte in input.by_ref() {
        let c = byte.unwrap();
        if c.is_ascii_digit() {
            value = value * 10 + usize::from(c - b'0');
            started = true;
        } else if started {
            break;
        }
    }
    value
}

fn main() {
    const OUTPUT_BUFFER_SIZE: usize = 1024;
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes();
    let n = read_int(&mut input);
    let m = read_int(&mut input);
    // 16-bit counters: there are at most 10000 votes
    let mut votes = vec![0_u16; n + 1];
    for _ in 0..m {
        votes[read_int(&mut input)] += 1;
    }
    // the percentages go out through a 1 KB buffered writer
    let stdout = io::stdout();
    let mut output = BufWriter::with_capacity(OUTPUT_BUFFER_SIZE, stdout.lock());
    for &count in &votes[1..] {
        writeln!(output, "{:.2}%", PERCENT * f64::from(count) / m as f64).unwrap();
    }
}
