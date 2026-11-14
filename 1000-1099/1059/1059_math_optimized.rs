use std::io::{self, Read, Write};

const MAX_DEGREE: usize = 1000;
const INDEX_DIGITS: usize = 4;
const STEP_SIZE: usize = b"X\n*\n\n+\n".len() + INDEX_DIGITS;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let degree = input.trim().parse::<usize>().unwrap();
    let mut output = [0; 2 + MAX_DEGREE * STEP_SIZE];
    let mut cursor = io::Cursor::new(output.as_mut_slice());
    cursor.write_all(b"0\n")?;
    let mut digits = [b'0'; INDEX_DIGITS];
    // Increment the coefficient index in place, including decimal carries.
    let mut first = digits.len() - 1;
    for _ in 0..degree {
        let mut pos = digits.len() - 1;
        while digits[pos] == b'9' {
            digits[pos] = b'0';
            pos -= 1;
        }
        digits[pos] += 1;
        first = first.min(pos);
        cursor.write_all(b"X\n*\n")?;
        cursor.write_all(&digits[first..])?;
        cursor.write_all(b"\n+\n")?;
    }
    let length = cursor.position() as usize;
    io::stdout().lock().write_all(&output[..length])
}
