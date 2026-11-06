#![no_main]

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn system_read(fd: i32, buffer: *mut u8, length: u32) -> i32;
    #[link_name = "_write"]
    fn system_write(fd: i32, buffer: *const u8, length: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn system_read(fd: i32, buffer: *mut u8, length: usize) -> isize;
    #[link_name = "write"]
    fn system_write(fd: i32, buffer: *const u8, length: usize) -> isize;
}

fn read_input(buffer: &mut [u8]) -> usize {
    // SAFETY: the writable slice stays live for the call, and its length is at most INPUT_SIZE.
    // Both CRT _read and POSIX read write no more than the supplied length.
    let count = unsafe {
        #[cfg(windows)]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len() as u32)
        }
        #[cfg(not(windows))]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len())
        }
    };
    if count > 0 {
        count as usize
    } else {
        0
    }
}

fn write_all(mut buffer: &[u8]) -> bool {
    while !buffer.is_empty() {
        // SAFETY: the readable slice stays live and has at most OUTPUT_SIZE bytes.
        // Both write functions access at most the specified length and return a byte count.
        let count = unsafe {
            #[cfg(windows)]
            {
                system_write(1, buffer.as_ptr(), buffer.len() as u32)
            }
            #[cfg(not(windows))]
            {
                system_write(1, buffer.as_ptr(), buffer.len())
            }
        };
        if count <= 0 {
            return false;
        }
        buffer = &buffer[count as usize..];
    }
    true
}

use std::cmp::Ordering;

// Signed arbitrary-precision integers, stored in little-endian limbs.
#[derive(Clone)]
struct Integer {
    digits: Vec<u32>,
    negative: bool,
}

impl Integer {
    const BASE: u32 = 1_000_000_000;
    const WIDTH: usize = 9;

    fn new(v: i64) -> Self {
        let mut u = v.abs() as u64;
        let mut digits = Vec::new();
        while u != 0 {
            digits.push((u % u64::from(Self::BASE)) as u32);
            u /= u64::from(Self::BASE);
        }
        Self {
            digits,
            negative: v < 0,
        }
    }

    fn normalize(&mut self) {
        while self.digits.last() == Some(&0) {
            self.digits.pop();
        }
        if self.digits.is_empty() {
            self.negative = false;
        }
    }

    fn magnitude(&self, b: &Self) -> Ordering {
        self.digits
            .len()
            .cmp(&b.digits.len())
            .then_with(|| self.digits.iter().rev().cmp(b.digits.iter().rev()))
    }

    fn cmp(&self, b: &Self) -> Ordering {
        if self.negative != b.negative {
            return if self.negative {
                Ordering::Less
            } else {
                Ordering::Greater
            };
        }
        if self.negative {
            b.magnitude(self)
        } else {
            self.magnitude(b)
        }
    }

    fn add(&self, b: &Self) -> Self {
        let mut out = Self::new(0);
        if self.negative == b.negative {
            out.negative = self.negative;
            let mut carry = 0;
            let mut i = 0;
            while i < self.digits.len().max(b.digits.len()) || carry != 0 {
                let v = carry + self.digits.get(i).unwrap_or(&0) + b.digits.get(i).unwrap_or(&0);
                out.digits.push(v % Self::BASE);
                carry = v / Self::BASE;
                i += 1;
            }
        } else {
            let (hi, lo) = if self.magnitude(b) != Ordering::Less {
                (self, b)
            } else {
                (b, self)
            };
            out.negative = hi.negative;
            let mut borrow = 0;
            for i in 0..hi.digits.len() {
                let v = hi.digits[i] as i64 - borrow - *lo.digits.get(i).unwrap_or(&0) as i64;
                borrow = if v < 0 { 1 } else { 0 };
                out.digits.push(if v < 0 {
                    (v + i64::from(Self::BASE)) as u32
                } else {
                    v as u32
                });
            }
        }
        out.normalize();
        out
    }

    fn sub(&self, b: &Self) -> Self {
        let mut other = b.clone();
        if !other.digits.is_empty() {
            other.negative = !other.negative;
        }
        self.add(&other)
    }

    fn mul(&self, b: &Self) -> Self {
        let mut out = Self {
            digits: vec![0; self.digits.len() + b.digits.len()],
            negative: self.negative != b.negative,
        };
        for i in 0..self.digits.len() {
            let mut carry = 0;
            let mut j = 0;
            while j < b.digits.len() || carry != 0 {
                let v = u64::from(out.digits[i + j])
                    + carry
                    + u64::from(self.digits[i]) * u64::from(*b.digits.get(j).unwrap_or(&0));
                out.digits[i + j] = (v % u64::from(Self::BASE)) as u32;
                carry = v / u64::from(Self::BASE);
                j += 1;
            }
        }
        out.normalize();
        out
    }

    fn scale(&self, v: i64) -> Self {
        let mut out = Self::new(0);
        out.scale_from(self, v);
        out
    }

    // The factors are bounded by the denominator 8 * (dx^2 + dy^2).
    fn scale_from(&mut self, source: &Self, factor: i64) {
        let mut carry = 0;
        let base = u64::from(Self::BASE);
        self.digits.clear();
        for &digit in &source.digits {
            let value = u64::from(digit) * factor.unsigned_abs() + carry;
            self.digits.push((value % base) as u32);
            carry = value / base;
        }
        while carry != 0 {
            self.digits.push((carry % base) as u32);
            carry /= base;
        }
        self.negative = source.negative != (factor < 0);
        self.normalize();
    }

    fn abs(mut self) -> Self {
        self.negative = false;
        self
    }

    fn max0(self) -> Self {
        if self.negative {
            Self::new(0)
        } else {
            self
        }
    }

    fn parse(text: &[u8]) -> Self {
        let mut out = Self::new(0);
        let signed = matches!(text.first(), Some(b'-' | b'+'));
        let digits = &text[usize::from(signed)..];
        // A group of nine decimal digits is already one limb.
        for chunk in digits.rchunks(Self::WIDTH) {
            let value = chunk
                .iter()
                .fold(0, |x, &digit| 10 * x + u32::from(digit - b'0'));
            out.digits.push(value);
        }
        out.negative = text.first() == Some(&b'-');
        out.normalize();
        out
    }
}

// squared distances carry these denominators: a point scaled by 2, a square
// by its projections
const POINT_DEN: i64 = 4;
const SQUARE_DEN: i64 = 8;

// squared distance from P to the square with diagonal (x1, y1)-(x2, y2), as a
// numerator and a denominator
fn distance(x1: i64, y1: i64, x2: i64, y2: i64, px: &Integer, py: &Integer) -> (Integer, i64) {
    // doubled coordinates of P relative to the centre, and the diagonal
    let qx = px.sub(&Integer::new(x1 + x2));
    let qy = py.sub(&Integer::new(y1 + y2));
    let (dx, dy) = (x2 - x1, y2 - y1);
    let h = dx * dx + dy * dy;
    if h == 0 {
        return (qx.mul(&qx).add(&qy.mul(&qy)), POINT_DEN);
    }
    // projections on the two side directions, the diagonal turned by +-45
    // degrees; inside the square both stay within h
    let s1 = qx.scale(dx - dy).add(&qy.scale(dy + dx)).abs();
    let s2 = qx.scale(dx + dy).add(&qy.scale(dy - dx)).abs();
    let a = s1.sub(&Integer::new(h)).max0();
    let b = s2.sub(&Integer::new(h)).max0();
    (a.mul(&a).add(&b.mul(&b)), SQUARE_DEN * h)
}

const MAX_SQUARES: usize = 50;
const OUTPUT_SIZE: usize = MAX_SQUARES * 3;
const DECIMAL_BASE: usize = 10;

fn small_integer(text: &[u8]) -> i64 {
    let signed = matches!(text.first(), Some(b'-' | b'+'));
    let value = text[usize::from(signed)..].iter().fold(0, |value, &digit| {
        value * DECIMAL_BASE as i64 + i64::from(digit - b'0')
    });
    if text.first() == Some(&b'-') {
        -value
    } else {
        value
    }
}

const INPUT_SIZE: usize = 1024;

// The C runtime calls this symbol directly.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Vec::new();
    let mut chunk = [0; INPUT_SIZE];
    loop {
        let count = read_input(&mut chunk);
        if count == 0 {
            break;
        }
        input.extend_from_slice(&chunk[..count]);
    }
    let mut tokens = input
        .split(u8::is_ascii_whitespace)
        .filter(|token| !token.is_empty());
    let n = small_integer(tokens.next().unwrap()) as usize;
    let mut squares = [(0i64, 0i64, 0i64, 0i64); MAX_SQUARES];
    for square in &mut squares[..n] {
        *square = (
            small_integer(tokens.next().unwrap()),
            small_integer(tokens.next().unwrap()),
            small_integer(tokens.next().unwrap()),
            small_integer(tokens.next().unwrap()),
        );
    }
    let px = Integer::parse(tokens.next().unwrap()).scale(2);
    let py = Integer::parse(tokens.next().unwrap()).scale(2);
    let dist: Vec<(Integer, i64)> = squares[..n]
        .iter()
        .map(|&(x1, y1, x2, y2)| distance(x1, y1, x2, y2, &px, &py))
        .collect();
    let mut order = [0usize; MAX_SQUARES];
    for (index, value) in order[..n].iter_mut().enumerate() {
        *value = index;
    }
    let (mut left, mut right) = (Integer::new(0), Integer::new(0));
    order[..n].sort_unstable_by(|&i, &j| {
        left.scale_from(&dist[i].0, dist[j].1);
        right.scale_from(&dist[j].0, dist[i].1);
        left.cmp(&right).then_with(|| i.cmp(&j))
    });
    // Indices 1..50 need at most two decimal digits and one separator.
    let mut output = [0; OUTPUT_SIZE];
    let mut used = 0;
    for (position, &square) in order[..n].iter().enumerate() {
        let index = square + 1;
        if index >= DECIMAL_BASE {
            output[used] = b'0' + (index / DECIMAL_BASE) as u8;
            used += 1;
        }
        output[used] = b'0' + (index % DECIMAL_BASE) as u8;
        output[used + 1] = if position + 1 == n { b'\n' } else { b' ' };
        used += 2;
    }
    i32::from(!write_all(&output[..used]))
}
