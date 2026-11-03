use std::io::{self, Read, Write};

const MAX_COORD: usize = 32000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let n = numbers.next().unwrap();
    // Each counter is bounded by the15000 stars. Parse tokens lazily and
    // keep16-bit counters, without a whole coordinate vector or output string.
    let mut tree = vec![0u16; MAX_COORD + 2];
    let mut count = vec![0u16; n];
    for _ in 0..n {
        let start = numbers.next().unwrap() + 1;
        numbers.next();
        let (mut j, mut level) = (start, 0);
        while j > 0 {
            level += tree[j] as usize;
            j &= j - 1;
        }
        count[level] += 1;
        let mut j = start;
        while j <= MAX_COORD + 1 {
            tree[j] += 1;
            j += j & j.wrapping_neg();
        }
    }
    let stdout = io::stdout();
    let mut output = io::BufWriter::new(stdout.lock());
    for value in count {
        writeln!(output, "{}", value).unwrap();
    }
}
