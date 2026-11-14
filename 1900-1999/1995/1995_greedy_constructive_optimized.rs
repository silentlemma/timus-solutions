use std::io::{self, BufWriter, Read, Write};

const PERCENT_SCALE: usize = 100;
const DECIMAL: usize = 10;
const DECIMAL_BUFFER: usize = 6;

fn plateaus(size: usize, kept: usize, percentage: usize) -> impl Iterator<Item = (usize, usize)> {
    std::iter::successors(Some((0, size - kept)), move |&(_, end)| {
        // The next block can use ranks below end up to floor(100 * end / p).
        (end < size).then(|| (end, (PERCENT_SCALE * end / percentage + 1).min(size)))
    })
    .enumerate()
    .map(|(index, (start, end))| (end - start, index + 1))
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let size = tokens.next().unwrap();
    let kept = tokens.next().unwrap();
    let percentage = tokens.next().unwrap();
    let total: u64 = plateaus(size, kept, percentage)
        .map(|(count, weight)| count as u64 * weight as u64)
        .sum();
    let mut output = BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", total)?;
    let mut separator = b"".as_slice();
    for (count, mut weight) in plateaus(size, kept, percentage) {
        let mut digits = [0; DECIMAL_BUFFER];
        let mut start = digits.len();
        while weight != 0 {
            start -= 1;
            digits[start] = b'0' + (weight % DECIMAL) as u8;
            weight /= DECIMAL;
        }
        for _ in 0..count {
            output.write_all(separator)?;
            output.write_all(&digits[start..])?;
            separator = b" ";
        }
    }
    output.write_all(b"\n")?;
    output.flush()
}
