use std::io::{self, BufRead, BufWriter, Write};

const DIVISOR: usize = 7;
const KEY_LENGTH: usize = 4;
const KEY_SHIFT: usize = 10000;
const MAX_DIGITS: usize = 20;
const SUFFIXES: [&[u8; KEY_LENGTH]; DIVISOR] = [
    b"3241", b"1324", b"1234", b"2341", b"1243", b"1342", b"2134",
];

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut line = String::new();
    input.read_line(&mut line)?;
    let count: usize = line.trim().parse().unwrap();
    let mut out = BufWriter::new(io::stdout().lock());
    for _ in 0..count {
        line.clear();
        input.read_line(&mut line)?;
        let mut answer = [b'0'; MAX_DIGITS + 1];
        let mut removed = [false; KEY_LENGTH];
        let (mut size, mut zeros, mut remainder) = (0, 0, 0);
        for digit in line.trim().bytes() {
            match digit {
                b'0' => zeros += 1,
                b'1'..=b'4' if !removed[usize::from(digit - b'1')] => {
                    removed[usize::from(digit - b'1')] = true;
                }
                _ => {
                    answer[size] = digit;
                    size += 1;
                    remainder = (10 * remainder + usize::from(digit - b'0')) % DIVISOR;
                }
            }
        }
        // Choose the four digits that cancel the shifted head remainder.
        let needed = (DIVISOR - remainder * KEY_SHIFT % DIVISOR) % DIVISOR;
        answer[size..size + KEY_LENGTH].copy_from_slice(SUFFIXES[needed]);
        size += KEY_LENGTH + zeros;
        answer[size] = b'\n';
        out.write_all(&answer[..=size])?;
    }
    out.flush()
}
