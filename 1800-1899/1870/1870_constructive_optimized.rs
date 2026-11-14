use std::io::{self, BufWriter, Write};

const DIVISOR_THREE: usize = 3;
const DECIMAL: usize = 10;
const MAX_DIGITS: usize = 6;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_line(&mut input)?;
    let size: usize = input.trim().parse().unwrap();
    if size % 2 == 0 || size % DIVISOR_THREE == 0 {
        println!("No");
        return Ok(());
    }

    let mut out = BufWriter::new(io::stdout().lock());
    out.write_all(b"Yes\n")?;
    // The modular sequence is the odd row numbers followed by the even ones.
    for row in (1..=size).step_by(2).chain((2..size).step_by(2)) {
        if row != 1 {
            out.write_all(b" ")?;
        }
        let mut value = row;
        let mut digits = [0; MAX_DIGITS];
        let mut start = digits.len();
        while value > 0 {
            start -= 1;
            digits[start] = b'0' + (value % DECIMAL) as u8;
            value /= DECIMAL;
        }
        out.write_all(&digits[start..])?;
    }
    out.write_all(b"\n")?;
    out.flush()
}
