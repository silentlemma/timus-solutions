use std::io::{self, BufWriter, Read, Write};

const COLUMNS: usize = 100;

fn number(input: &mut impl Iterator<Item = u8>) -> usize {
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut value = usize::from(first - b'0');
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + usize::from(byte - b'0');
    }
    value
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let (rows, cols) = (number(&mut input), number(&mut input));
    let mut out = BufWriter::new(io::stdout().lock());
    let mut standing = [false; COLUMNS / 2];
    for row in (0..rows).step_by(2) {
        let blocks = &mut standing[..cols / 2];
        for block in blocks.iter_mut() {
            *block = number(&mut input) == number(&mut input);
        }
        for block in blocks.iter_mut() {
            let (left, right) = (number(&mut input), number(&mut input));
            *block |= left == right;
        }
        // Both output rows share the same block orientations and labels.
        for upper in [true, false] {
            for (col, &vertical) in blocks.iter().enumerate() {
                let a = row * (cols / 2) + 2 * col + 1;
                let b = a + 1;
                let (left, right) = if vertical {
                    (a, b)
                } else if upper {
                    (a, a)
                } else {
                    (b, b)
                };
                if col != 0 {
                    out.write_all(b" ").unwrap();
                }
                write!(out, "{} {}", left, right).unwrap();
            }
            writeln!(out).unwrap();
        }
    }
    out.flush().unwrap();
}
