#![no_main]

use std::io::{self, Write};

const CHARS: usize = 128;

fn solve_entry() {
    let input = TokenInput::new();
    let mut words = input.into_iter();
    let k: usize = parse_integer(words.next().unwrap());
    let last_word = words.next().unwrap();
    let last = last_word.as_bytes();
    // a stable counting sort of the last column: row order[j] ends with
    // the j-th character of the sorted column, the first one of row j
    let mut start = vec![0usize; CHARS + 1];
    for &c in last {
        start[c as usize + 1] += 1;
    }
    for c in 0..CHARS {
        start[c + 1] += start[c];
    }
    let mut order = vec![0u32; last.len()];
    for (i, &c) in last.iter().enumerate() {
        order[start[c as usize]] = i as u32;
        start[c as usize] += 1;
    }
    let mut row = k - 1;
    let mut text = Vec::with_capacity(last.len() + 1);
    for _ in 0..last.len() {
        row = order[row] as usize;
        text.push(last[row]);
    }
    text.push(b'\n');
    io::stdout().write_all(&text).unwrap();
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
    solve_entry();
    std::io::Write::flush(&mut std::io::stdout()).unwrap();
    0
}
