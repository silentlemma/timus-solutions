use std::io::{self, Read, Write};

const MAX_SEGMENTS: usize = 500;
const INPUT_SIZE: usize = 128;
const OUTPUT_SIZE: usize = MAX_SEGMENTS * 4 + 8;
const MAX_DIGITS: usize = 5;
const NONE: u16 = u16::MAX;

struct Input<R> {
    reader: R,
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn next_byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.reader.read(&mut self.bytes).unwrap_or(0);
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let value = self.bytes[self.position];
        self.position += 1;
        value
    }

    fn next_int(&mut self) -> i32 {
        let mut c = self.next_byte();
        while c != 0 && c <= b' ' {
            c = self.next_byte();
        }
        let negative = c == b'-';
        if negative || c == b'+' {
            c = self.next_byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.next_byte();
        }
        if negative {
            -value
        } else {
            value
        }
    }
}

fn write_number(output: &mut [u8], used: &mut usize, mut value: usize) {
    let mut digits = [0; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    let length = digits.len() - first;
    output[*used..*used + length].copy_from_slice(&digits[first..]);
    *used += length;
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        reader: stdin.lock(),
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.next_int() as usize;
    let mut segments = [(0i16, 0i16, 0u16); MAX_SEGMENTS];
    for (index, segment) in segments[..n].iter_mut().enumerate() {
        let a = input.next_int() as i16;
        let b = input.next_int() as i16;
        *segment = (a.min(b), a.max(b), (index + 1) as u16);
    }
    // Equal left endpoints have increasing right endpoints, so a strictly
    // decreasing subsequence cannot include two of them.
    segments[..n].sort_unstable();
    let mut tails = [0u16; MAX_SEGMENTS];
    let mut parent = [NONE; MAX_SEGMENTS];
    let mut length = 0;
    for (index, &(_, right, _)) in segments[..n].iter().enumerate() {
        let level = tails[..length].partition_point(|&tail| segments[usize::from(tail)].1 > right);
        if level > 0 {
            parent[index] = tails[level - 1];
        }
        tails[level] = index as u16;
        if level == length {
            length += 1;
        }
    }
    let mut output = [0; OUTPUT_SIZE];
    let mut used = 0;
    write_number(&mut output, &mut used, length);
    output[used] = b'\n';
    used += 1;
    let mut current = tails[length - 1];
    loop {
        let index = usize::from(current);
        write_number(&mut output, &mut used, usize::from(segments[index].2));
        current = parent[index];
        output[used] = if current == NONE { b'\n' } else { b' ' };
        used += 1;
        if current == NONE {
            break;
        }
    }
    io::stdout().lock().write_all(&output[..used]).ok();
}
