use std::io::{self, Read, Write};

const INDEX_BITS: u32 = 10;
const INDEX_MASK: u32 = (1 << INDEX_BITS) - 1;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input.split_ascii_whitespace();
    let size: usize = tokens.next().unwrap().parse().unwrap();
    let mut ordered: Vec<u32> = (1..=size)
        .map(|index| {
            let threshold: u32 = tokens.next().unwrap().parse().unwrap();
            (threshold << INDEX_BITS) | index as u32
        })
        .collect();
    ordered.sort_unstable();
    let threshold = |i: usize| (ordered[i] >> INDEX_BITS) as usize;
    let sizes: Vec<_> = (1..=size)
        .filter(|&count| {
            threshold(count - 1) <= count && (count == size || threshold(count) > count + 1)
        })
        .collect();
    let mut output = io::BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", sizes.len())?;
    for count in sizes {
        write!(output, "{count}")?;
        for &entry in &ordered[..count] {
            write!(output, " {}", entry & INDEX_MASK)?;
        }
        writeln!(output)?;
    }
    output.flush()
}
