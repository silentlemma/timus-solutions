use std::io::{self, BufWriter, Write};

const BLOCK: usize = 1024;

fn write_digits(out: &mut impl Write, digit: u8, mut count: usize) {
    let digits = [digit; BLOCK];
    while count >= BLOCK {
        out.write_all(&digits).unwrap();
        count -= BLOCK;
    }
    out.write_all(&digits[..count]).unwrap();
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    let half = n / 2;
    let mut out = BufWriter::new(io::stdout().lock());
    // Stream the decimal runs in 1 + 9 k², where k consists of half ones.
    match half {
        0 => out.write_all(b"1\n").unwrap(),
        1 => out.write_all(b"10\n").unwrap(),
        _ => {
            write_digits(&mut out, b'1', half - 1);
            out.write_all(b"0").unwrap();
            write_digits(&mut out, b'8', half - 2);
            out.write_all(b"90\n").unwrap();
        }
    }
    out.flush().unwrap();
}
