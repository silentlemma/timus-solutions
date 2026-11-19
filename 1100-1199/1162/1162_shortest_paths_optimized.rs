#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads the standard stream.
    unsafe { getchar() }
}

fn read_number() -> Option<i64> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    if byte < 0 {
        return None;
    }
    let negative = byte == b'-' as i32;
    if negative || byte == b'+' as i32 {
        byte = read_byte();
    }
    let mut value = 0i64;
    while (b'0' as i32..=b'9' as i32).contains(&byte) {
        let digit = i64::from(byte - b'0' as i32);
        // Accumulating negatives directly also accepts i64::MIN.
        value = if negative {
            value * 10 - digit
        } else {
            value * 10 + digit
        };
        byte = read_byte();
    }
    Some(value)
}

fn number() -> i64 {
    read_number().unwrap()
}

fn word() -> Vec<u8> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    let mut result = Vec::new();
    while byte > b' ' as i32 {
        result.push(byte as u8);
        byte = read_byte();
    }
    result
}
fn write_byte(byte: u8) {
    // SAFETY: putchar accepts a byte promoted to int and has no pointers.
    unsafe {
        putchar(i32::from(byte));
    }
}

fn write_text(text: &[u8]) {
    for &byte in text {
        write_byte(byte);
    }
}

use std::cmp::Ordering;

const BASE: u64 = 1_000_000_000;
const CHUNK: usize = 9;
const SCALE: u32 = 100;

#[derive(Clone)]
struct Amount(Vec<u32>);
impl Amount {
    fn trim(&mut self) {
        while self.0.len() > 1 && self.0.last() == Some(&0) {
            self.0.pop();
        }
    }

    fn parse(text: &[u8], places: usize) -> Self {
        let fractional = text
            .iter()
            .position(|&b| b == b'.')
            .map_or(0, |i| text.len() - i - 1);
        let mut digits: Vec<u8> = text.iter().copied().filter(u8::is_ascii_digit).collect();
        digits.resize(digits.len() + places - fractional, b'0');
        let mut result = Vec::with_capacity((digits.len() + CHUNK - 1) / CHUNK);
        let mut end = digits.len();
        while end > 0 {
            let start = end.saturating_sub(CHUNK);
            result.push(
                digits[start..end]
                    .iter()
                    .fold(0, |number, &b| number * 10 + u32::from(b - b'0')),
            );
            end = start;
        }
        let mut amount = Self(result);
        amount.trim();
        amount
    }

    fn compare(&self, other: &Self) -> Ordering {
        self.0
            .len()
            .cmp(&other.0.len())
            .then_with(|| self.0.iter().rev().cmp(other.0.iter().rev()))
    }

    fn multiply_into(&self, factor: u32, target: &mut Self) {
        target.0.clear();
        let mut carry = 0u64;
        for &digit in &self.0 {
            let value = u64::from(digit) * u64::from(factor) + carry;
            target.0.push((value % BASE) as u32);
            carry = value / BASE;
        }
        while carry > 0 {
            target.0.push((carry % BASE) as u32);
            carry /= BASE;
        }
        target.trim();
    }

    fn scale(&mut self, factor: u32) {
        let mut carry = 0u64;
        for digit in &mut self.0 {
            let value = u64::from(*digit) * u64::from(factor) + carry;
            *digit = (value % BASE) as u32;
            carry = value / BASE;
        }
        while carry > 0 {
            self.0.push((carry % BASE) as u32);
            carry /= BASE;
        }
        self.trim();
    }

    fn subtract_into(&self, cost: &Self, target: &mut Self) {
        target.0.clear();
        let mut borrow = 0i64;
        for (i, &digit) in self.0.iter().enumerate() {
            let value = i64::from(digit) - i64::from(cost.0.get(i).copied().unwrap_or(0)) - borrow;
            borrow = i64::from(value < 0);
            target.0.push((value + borrow * BASE as i64) as u32);
        }
        assert_eq!(borrow, 0);
        target.trim();
    }
}

struct Exchange {
    from: u8,
    to: u8,
    rate: u32,
    fee: u32,
}

fn cents() -> u32 {
    let text = word();
    let dot = text.iter().position(|&b| b == b'.');
    let fractional = dot.map_or(0, |i| text.len() - i - 1);
    let mut result = text
        .iter()
        .copied()
        .filter(u8::is_ascii_digit)
        .fold(0, |number, byte| number * 10 + u32::from(byte - b'0'));
    for _ in fractional..2 {
        result *= 10;
    }
    result
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (count, exchanges, start) = (number() as usize, number() as usize, number() as usize - 1);
    let text = word();
    let places = 2.max(
        text.iter()
            .position(|&b| b == b'.')
            .map_or(0, |i| text.len() - i - 1),
    );
    let mut initial = Amount::parse(&text, places);
    let mut unit = Amount(vec![0; (places - 2) / CHUNK + 1]);
    unit.0[(places - 2) / CHUNK] = 10u32.pow(((places - 2) % CHUNK) as u32);
    let mut edges = Vec::with_capacity(2 * exchanges);
    for _ in 0..exchanges {
        let (a, b) = (number() as u8 - 1, number() as u8 - 1);
        let (rate_ab, fee_ab, rate_ba, fee_ba) = (cents(), cents(), cents(), cents());
        edges.push(Exchange {
            from: a,
            to: b,
            rate: rate_ab,
            fee: fee_ab,
        });
        edges.push(Exchange {
            from: b,
            to: a,
            rate: rate_ba,
            fee: fee_ba,
        });
    }
    let mut best: Vec<Option<Amount>> = vec![None; count];
    best[start] = Some(initial.clone());
    let mut after: Vec<Option<Amount>> = vec![None; count];
    let mut cost = Amount(Vec::new());
    let mut candidate = Amount(Vec::new());
    let mut changed = false;
    // All amounts share one exact denominator; each pass multiplies it by 100.
    for _ in 0..count {
        for (source, target) in best.iter().zip(after.iter_mut()) {
            if let Some(amount) = source {
                amount.multiply_into(SCALE, target.get_or_insert_with(|| Amount(Vec::new())));
            } else {
                *target = None;
            }
        }
        changed = false;
        for edge in &edges {
            if let Some(amount) = &best[usize::from(edge.from)] {
                unit.multiply_into(edge.fee, &mut cost);
                if amount.compare(&cost) != Ordering::Less {
                    amount.subtract_into(&cost, &mut candidate);
                    candidate.scale(edge.rate);
                    let target = &mut after[usize::from(edge.to)];
                    if target
                        .as_ref()
                        .map_or(true, |old| candidate.compare(old) == Ordering::Greater)
                    {
                        std::mem::swap(
                            target.get_or_insert_with(|| Amount(Vec::new())),
                            &mut candidate,
                        );
                        changed = true;
                    }
                }
            }
        }
        std::mem::swap(&mut best, &mut after);
        unit.scale(SCALE);
        initial.scale(SCALE);
        if best[start].as_ref().unwrap().compare(&initial) == Ordering::Greater || !changed {
            break;
        }
    }
    let gain = best[start].as_ref().unwrap().compare(&initial) == Ordering::Greater || changed;
    write_text(if gain { b"YES\n" } else { b"NO\n" });

    0
}
