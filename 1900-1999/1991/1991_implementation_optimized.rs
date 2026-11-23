#![no_main]

use std::io::{self, Read, Write};

struct Input<'a> {
    data: &'a [u8],
    position: usize,
}

impl<'a> Input<'a> {
    fn word(&mut self) -> &'a [u8] {
        while self.position < self.data.len() && self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let start = self.position;
        while self.position < self.data.len() && !self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        &self.data[start..self.position]
    }

    fn number(&mut self) -> u64 {
        self.word()
            .iter()
            .fold(0, |value, &digit| value * 10 + u64::from(digit - b'0'))
    }
}

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

fn solve_entry() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Input {
        data: &data,
        position: 0,
    };
    let count = input.number();
    let capacity = input.number() as i64;
    let (mut unused, mut survivors) = (0, 0);
    for _ in 0..count {
        let amount = input.number() as i64;
        if amount > capacity {
            unused += amount - capacity;
        } else {
            survivors += capacity - amount;
        }
    }
    emit(&[unused, survivors]);
}

// Run the algorithm directly and flush Rust's global output before returning to C.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    solve_entry();
    std::io::Write::flush(&mut std::io::stdout()).unwrap();
    0
}
