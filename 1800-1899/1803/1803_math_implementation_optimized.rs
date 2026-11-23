#![no_main]

use std::io::{self, BufWriter, Write};

const LIMB_LIMIT: usize = 200_000;
const BINARY_BITS: u32 = 60;
const BINARY_BASE: u64 = 1 << BINARY_BITS;

fn fibonacci_costs(base: u64, digit_sum: impl Fn(u64) -> u32, costs: &mut [u32]) {
    let (mut previous, mut current) = (vec![1u64], vec![1u64]);
    for cost in &mut costs[2..] {
        previous.resize(current.len(), 0);
        let mut carry = 0;
        let mut sum = 0;
        for (a, &b) in previous.iter_mut().zip(&current) {
            let value = *a + b + carry;
            carry = u64::from(value >= base);
            *a = value - carry * base;
            sum += digit_sum(*a);
        }
        if carry != 0 {
            previous.push(carry);
        }
        *cost = sum + carry as u32;
        std::mem::swap(&mut previous, &mut current);
    }
}

fn solve_entry() -> io::Result<()> {
    let input = TokenInput::new();
    let mut fields = input.into_iter();
    let radix: usize = parse_integer(fields.next().unwrap());
    let count: usize = parse_integer(fields.next().unwrap());
    let mut costs = vec![1; count];

    if radix.is_power_of_two() {
        let bits = radix.trailing_zeros();
        // A 60-bit limb contains whole digits in bases 2, 4 and 8.
        let mask = (0..BINARY_BITS)
            .step_by(bits as usize)
            .fold(0u64, |m, i| m | (1 << i));
        fibonacci_costs(
            BINARY_BASE,
            |limb| {
                let mut sum = (limb & mask).count_ones();
                for bit in 1..bits {
                    sum += ((limb >> bit) & mask).count_ones() << bit;
                }
                sum
            },
            &mut costs,
        );
    } else {
        let mut base = 1;
        while base <= LIMB_LIMIT / radix {
            base *= radix;
        }
        // Even the loose bound of 20 digits times 9 fits in one byte.
        let mut sums = vec![0u8; base];
        for i in 1..base {
            sums[i] = sums[i / radix] + (i % radix) as u8;
        }
        fibonacci_costs(
            base as u64,
            |limb| u32::from(sums[limb as usize]),
            &mut costs,
        );
    }

    let mut order: Vec<u32> = (0..count as u32).collect();
    order.sort_unstable_by_key(|&i| (costs[i as usize], i));
    let mut output = BufWriter::new(io::stdout().lock());
    for (position, index) in order.into_iter().enumerate() {
        if position != 0 {
            output.write_all(b" ")?;
        }
        write!(output, "{}", index + 1)?;
    }
    output.write_all(b"\n")?;
    output.flush()
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: impl AsRef<[u8]>) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_ref();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}

const INPUT_BUFFER_BYTES: usize = 4096;

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn input_read(fd: i32, data: *mut u8, size: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn input_read(fd: i32, data: *mut u8, size: usize) -> isize;
}

struct TokenInput {
    buffer: [u8; INPUT_BUFFER_BYTES],
    position: usize,
    length: usize,
}

impl TokenInput {
    fn new() -> Self {
        Self {
            buffer: [0; INPUT_BUFFER_BYTES],
            position: 0,
            length: 0,
        }
    }

    fn byte(&mut self) -> Option<u8> {
        if self.position == self.length {
            loop {
                // SAFETY: the live writable array is passed with its exact bounded length.
                let count = unsafe {
                    #[cfg(windows)]
                    {
                        input_read(0, self.buffer.as_mut_ptr(), INPUT_BUFFER_BYTES as u32)
                    }
                    #[cfg(not(windows))]
                    {
                        input_read(0, self.buffer.as_mut_ptr(), INPUT_BUFFER_BYTES)
                    }
                };
                if count > 0 {
                    self.position = 0;
                    self.length = count as usize;
                    break;
                }
                if count == 0 {
                    return None;
                }
                let error = io::Error::last_os_error();
                if error.kind() != io::ErrorKind::Interrupted {
                    panic!("stdin read failed: {error}");
                }
            }
        }
        let byte = self.buffer[self.position];
        self.position += 1;
        Some(byte)
    }
}

struct InputWord {
    inline: [u8; 32],
    length: usize,
    spill: Vec<u8>,
}

impl InputWord {
    #[inline]
    fn push(&mut self, byte: u8) {
        if self.length < self.inline.len() {
            self.inline[self.length] = byte;
        } else {
            if self.spill.is_empty() {
                self.spill.extend_from_slice(&self.inline);
            }
            self.spill.push(byte);
        }
        self.length += 1;
    }
}

impl AsRef<[u8]> for InputWord {
    fn as_ref(&self) -> &[u8] {
        if self.length <= self.inline.len() {
            &self.inline[..self.length]
        } else {
            &self.spill
        }
    }
}

impl std::ops::Deref for InputWord {
    type Target = str;
    fn deref(&self) -> &str {
        std::str::from_utf8(self.as_ref()).unwrap()
    }
}

impl PartialEq<&str> for InputWord {
    fn eq(&self, other: &&str) -> bool {
        self.as_ref() == other.as_bytes()
    }
}

impl Iterator for TokenInput {
    type Item = InputWord;
    #[inline]
    fn next(&mut self) -> Option<InputWord> {
        let mut first = self.byte()?;
        while first.is_ascii_whitespace() {
            first = self.byte()?;
        }
        let mut word = InputWord {
            inline: [0; 32],
            length: 0,
            spill: Vec::new(),
        };
        word.push(first);
        while let Some(byte) = self.byte() {
            if byte.is_ascii_whitespace() {
                break;
            }
            word.push(byte);
        }
        Some(word)
    }
}

// Run the algorithm directly and flush Rust's global output before returning to C.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    solve_entry().unwrap();
    std::io::Write::flush(&mut std::io::stdout()).unwrap();
    0
}
