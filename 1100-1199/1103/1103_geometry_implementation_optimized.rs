#![no_main]

use std::io;

type Point = (i64, i64);

fn cross(o: Point, a: Point, b: Point) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

fn solve_entry() {
    let input = TokenInput::new();
    let mut values = input.map(|word| parse_integer::<i64>(word));
    let n = values.next().unwrap() as usize;
    let mut pts: Vec<Point> = (0..n)
        .map(|_| (values.next().unwrap(), values.next().unwrap()))
        .collect();
    // A is the lowest point and B the next one on the hull, so every other
    // point lies on the left of AB and sees it under an angle below 180
    let first = (0..n).min_by_key(|&i| (pts[i].1, pts[i].0)).unwrap();
    pts.swap(0, first);
    let a = pts[0];
    let mut second = 1;
    for i in 2..n {
        let p = pts[i];
        let b = pts[second];
        if cross(a, b, p) < 0 {
            second = i;
        }
    }
    pts.swap(1, second);
    let b = pts[1];
    // the angle APB grows as its cotangent dot / cross falls; the products
    // reach 10^33, hence 128 bits
    let key = |p: Point| -> (i128, i128) {
        let dot = (a.0 - p.0) * (b.0 - p.0) + (a.1 - p.1) * (b.1 - p.1);
        (dot as i128, cross(p, a, b) as i128)
    };
    let others = &mut pts[2..];
    let mid = others.len() / 2;
    others.select_nth_unstable_by(mid, |&x, &y| {
        let ((dx, cx), (dy, cy)) = (key(x), key(y));
        (dy * cx).cmp(&(dx * cy))
    });
    // points seeing AB under a larger angle than C lie inside the circle ABC
    let c = others[mid];
    println!("{} {}\n{} {}\n{} {}", a.0, a.1, b.0, b.1, c.0, c.1);
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

const INLINE_TOKEN_BYTES: usize = 32;

struct InputWord {
    inline: [u8; INLINE_TOKEN_BYTES],
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
            inline: [0; INLINE_TOKEN_BYTES],
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
