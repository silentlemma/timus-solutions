use std::io::{self, BufRead, Write};

const MAX_BITS: usize = 60;

fn number(input: &mut impl BufRead) -> io::Result<u64> {
    let mut value = 0;
    let mut reading = false;
    loop {
        let bytes = input.fill_buf()?;
        if bytes.is_empty() {
            return Ok(value);
        }
        let size = bytes.len();
        for (i, &byte) in bytes.iter().enumerate() {
            if byte.is_ascii_digit() {
                value = value * 10 + u64::from(byte - b'0');
                reading = true;
            } else if reading {
                input.consume(i + 1);
                return Ok(value);
            }
        }
        input.consume(size);
    }
}

fn counts(n: usize) -> [u64; MAX_BITS + 1] {
    let mut count = [0; MAX_BITS + 1];
    let mut combinations = 1;
    for (k, total) in count.iter_mut().enumerate().take(n + 1).skip(1) {
        combinations = combinations * (n - k + 1) as u64 / k as u64;
        *total = 1 + combinations;
    }
    count[1] -= 1;
    // Pass only extra bottles to the smaller box. The originals were counted above.
    for k in (2..=n).rev() {
        count[k.count_ones() as usize] += count[k] - 1;
    }
    count
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let n = number(&mut input)? as usize;
    let q = number(&mut input)? as usize;
    let answers = counts(n).map(|count| count.to_string());
    let mut output = io::BufWriter::new(io::stdout().lock());
    for i in 0..q {
        let index = number(&mut input)?;
        if i != 0 {
            output.write_all(b" ")?;
        }
        if index <= n as u64 {
            output.write_all(answers[index as usize].as_bytes())?;
        } else {
            output.write_all(b"1")?;
        }
    }
    output.write_all(b"\n")?;
    output.flush()
}
