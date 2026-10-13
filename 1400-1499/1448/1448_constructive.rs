use std::io::{self, Read, Write};

const FULL: usize = 100; // brightness is given in percent

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (n, b) = (v[0], v[1]);
    // lamp i is on when floor((i + 1) b / 100) grows: every stretch then holds
    // less than one lamp more or less than L b / 100, and the pattern repeats
    let mut row: Vec<u8> = (0..n)
        .map(|i| {
            if (i % FULL + 1) * b / FULL > i % FULL * b / FULL {
                b'1'
            } else {
                b'0'
            }
        })
        .collect();
    row.push(b'\n');
    io::stdout().write_all(&row).unwrap();
}
