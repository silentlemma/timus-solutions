use std::io::{self, BufWriter, Read, Write};

const LETTERS: usize = 26;

fn repair(drum: &[u8], period: usize, budget: usize, pattern: &mut [u8]) -> bool {
    let per_class = drum.len() / period;
    let mut changes = 0;
    for (offset, letter) in pattern[..period].iter_mut().enumerate() {
        let mut counts = [0u32; LETTERS];
        let mut best = 0;
        for &byte in drum[offset..].iter().step_by(period) {
            let index = usize::from(byte - b'a');
            counts[index] += 1;
            if counts[index] > counts[best] {
                best = index;
            }
        }
        changes += per_class - counts[best] as usize;
        if changes > budget {
            return false;
        }
        *letter = b'a' + best as u8;
    }
    true
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut words = input.split_ascii_whitespace();
    let size: usize = words.next().unwrap().parse().unwrap();
    let budget: usize = words.next().unwrap().parse().unwrap();
    let drum = words.next().unwrap().as_bytes();
    let mut pattern = vec![0; size / 2];
    let mut output = BufWriter::new(io::stdout().lock());

    // A proper divisor is at most half the length. Reuse one output pattern.
    for period in 1..=pattern.len() {
        if size % period == 0 && repair(drum, period, budget, &mut pattern) {
            writeln!(output, "{period}")?;
            for _ in 0..size / period {
                output.write_all(&pattern[..period])?;
            }
            output.write_all(b"\n")?;
            return output.flush();
        }
    }
    writeln!(output, "{size}")?;
    output.write_all(drum)?;
    output.write_all(b"\n")?;
    output.flush()
}
