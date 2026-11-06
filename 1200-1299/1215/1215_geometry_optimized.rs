use std::io::{self, Read, Write};

const INPUT_SIZE: usize = 64;
const OUTPUT_SIZE: usize = 32;
const MAX_DIGITS: usize = 20;
const SCALE: u64 = 1000;
const SQUARED_SCALE: u128 = 4 * SCALE as u128 * SCALE as u128;
const ROUNDING_SCALE: u128 = 4;

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}

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

    fn number(&mut self) -> i64 {
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
            value = value * 10 + i64::from(c - b'0');
            c = self.next_byte();
        }
        if negative {
            -value
        } else {
            value
        }
    }
}

fn edge(p: Point, a: Point, b: Point) -> (bool, u64, u64) {
    let (mut x, mut y) = (p.x - a.x, p.y - a.y);
    let (dx, dy) = (b.x - a.x, b.y - a.y);
    let cross = dx * y - dy * x;
    let (dot, length) = (x * dx + y * dy, dx * dx + dy * dy);
    if dot <= 0 {
        (cross >= 0, (x * x + y * y) as u64, 1)
    } else if dot >= length {
        x = p.x - b.x;
        y = p.y - b.y;
        (cross >= 0, (x * x + y * y) as u64, 1)
    } else {
        (cross >= 0, (cross * cross) as u64, length as u64)
    }
}

fn rounded_diameter(num: u64, den: u64) -> u64 {
    let scaled = u128::from(num) * SQUARED_SCALE;
    let quotient = (scaled / u128::from(den)) as u64;
    let mut root = (quotient as f64).sqrt() as u64;
    while (root + 1) * (root + 1) <= quotient {
        root += 1;
    }
    while root * root > quotient {
        root -= 1;
    }
    // Compare with the half-unit threshold using exact 128-bit products.
    let threshold = u128::from(2 * root + 1);
    if ROUNDING_SCALE * scaled >= u128::from(den) * threshold * threshold {
        root += 1;
    }
    root
}

fn write_number(output: &mut [u8], used: &mut usize, mut value: u64) {
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
    let p = Point {
        x: input.number(),
        y: input.number(),
    };
    let n = input.number();
    let first = Point {
        x: input.number(),
        y: input.number(),
    };
    let mut previous = first;
    let (x, y) = (p.x - first.x, p.y - first.y);
    let (mut best_num, mut best_den) = ((x * x + y * y) as u64, 1u64);
    let mut inside = true;
    for index in 1..=n {
        let next = if index == n {
            first
        } else {
            Point {
                x: input.number(),
                y: input.number(),
            }
        };
        let (left, num, den) = edge(p, previous, next);
        inside &= left;
        if u128::from(num) * u128::from(best_den) < u128::from(best_num) * u128::from(den) {
            (best_num, best_den) = (num, den);
        }
        previous = next;
    }
    if inside {
        (best_num, best_den) = (0, 1);
    }
    let value = rounded_diameter(best_num, best_den);
    let mut output = [0; OUTPUT_SIZE];
    let mut used = 0;
    write_number(&mut output, &mut used, value / SCALE);
    output[used] = b'.';
    used += 1;
    let mut place = SCALE / 10;
    while place > 0 {
        output[used] = b'0' + ((value / place) % 10) as u8;
        used += 1;
        place /= 10;
    }
    output[used] = b'\n';
    used += 1;
    io::stdout().lock().write_all(&output[..used]).ok();
}
