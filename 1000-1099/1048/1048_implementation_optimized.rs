use std::io::{self, Read, Write};

const BASE: usize = 10;

fn main() {
    let stdin = io::stdin();
    let mut bytes = stdin.lock().bytes().map(Result::unwrap);
    let first = bytes.by_ref().find(|&c| c > b' ').unwrap();
    let mut n = (first - b'0') as usize;
    for c in bytes.by_ref() {
        if c <= b' ' {
            break;
        }
        n = n * BASE + (c - b'0') as usize;
    }
    // Discard input immediately; the column-sum buffer becomes the output.
    let mut out = vec![b'\n'; n + 1];
    let mut digits = bytes.filter(|c| c.is_ascii_digit()).map(|c| c - b'0');
    for slot in out.iter_mut().take(n) {
        let a = digits.next().unwrap();
        *slot = a + digits.next().unwrap();
    }
    let mut carry = 0;
    for slot in out.iter_mut().take(n).rev() {
        let value = *slot + carry;
        carry = value / BASE as u8;
        *slot = b'0' + value % BASE as u8;
    }
    io::stdout().write_all(&out).unwrap();
}
