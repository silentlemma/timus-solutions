use std::io::{self, Read, Write};

/// The characters of each key in the order of presses; the space has a key
/// of its own.
const KEYS: [&str; 11] = [
    "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", ".,!", " ",
];

// At most two bounded integers fit in the stack buffer, including signs and separators.
fn emit(values: &[i64]) {
    let mut buffer = [0_u8; 64];
    let mut position = buffer.len();
    for (index, &value) in values.iter().enumerate().rev() {
        position -= 1;
        buffer[position] = if index + 1 == values.len() {
            b'\n'
        } else {
            b' '
        };
        let mut digits = value.unsigned_abs();
        loop {
            position -= 1;
            buffer[position] = b'0' + (digits % 10) as u8;
            digits /= 10;
            if digits == 0 {
                break;
            }
        }
        if value < 0 {
            position -= 1;
            buffer[position] = b'-';
        }
    }
    io::stdout().lock().write_all(&buffer[position..]).unwrap();
}

fn main() {
    // the whole first line, spaces included; anything else costs nothing
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut costs = [0_u8; 256];
    for key in KEYS {
        for (index, byte) in key.bytes().enumerate() {
            costs[byte as usize] = (index + 1) as u8;
        }
    }
    let total: i64 = data
        .into_iter()
        .take_while(|&byte| byte != b'\n')
        .map(|byte| i64::from(costs[byte as usize]))
        .sum();
    emit(&[total]);
}
