use std::io::{self, Read, Write};

const DWARFS: u32 = 7;

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    // the number has up to 51 digits, so take it modulo 7 digit by digit
    let mut rest = 0;
    for digit in data.into_iter().filter(u8::is_ascii_digit) {
        rest = (rest * 10 + u32::from(digit - b'0')) % DWARFS;
    }
    io::stdout()
        .lock()
        .write_all(&[b'0' + rest as u8, b'\n'])
        .unwrap();
}
