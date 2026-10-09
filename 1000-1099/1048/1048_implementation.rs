use std::io::{self, Read, Write};

const BASE: u8 = 10;

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    // the first line holds N; the rest is the digits a1 b1 a2 b2 ...
    let line_end = input
        .iter()
        .position(|&c| c == b'\n')
        .unwrap_or(input.len());
    let (head, rest) = input.split_at(line_end);
    let n: usize = std::str::from_utf8(head).unwrap().trim().parse().unwrap();
    let mut digits = rest
        .iter()
        .filter(|c| c.is_ascii_digit())
        .map(|&c| c - b'0');
    // column sums from 0 to 18, then the carries from the last column up
    let mut out = vec![b'\n'; n + 1];
    for slot in out.iter_mut().take(n) {
        let a = digits.next().unwrap();
        *slot = a + digits.next().unwrap();
    }
    let mut carry = 0;
    for slot in out.iter_mut().take(n).rev() {
        let t = *slot + carry;
        carry = t / BASE;
        *slot = b'0' + t % BASE;
    }
    io::stdout().write_all(&out).unwrap();
}
