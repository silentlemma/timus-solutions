use std::io::{self, Write};

struct Charges {
    size: usize,
    initial: Vec<i64>,
    tree: Vec<i64>,
    offsets: Vec<u32>,
    divisors: Vec<u16>,
}

impl Charges {
    fn new(initial: Vec<i64>) -> Self {
        let size = initial.len() - 1;
        let mut offsets = vec![0u32; size + 2];
        let mut divisor = 1;
        while divisor * divisor <= size {
            for multiple in (divisor * divisor..=size).step_by(divisor) {
                offsets[multiple + 1] += 1;
            }
            divisor += 1;
        }
        for index in 1..=size + 1 {
            offsets[index] += offsets[index - 1];
        }
        let mut divisors = vec![0; offsets[size + 1] as usize];
        let mut cursor = offsets.clone();
        divisor = 1;
        while divisor * divisor <= size {
            for multiple in (divisor * divisor..=size).step_by(divisor) {
                divisors[cursor[multiple] as usize] = divisor as u16;
                cursor[multiple] += 1;
            }
            divisor += 1;
        }
        Self {
            size,
            initial,
            tree: vec![0; size + 1],
            offsets,
            divisors,
        }
    }

    fn irradiate(&mut self, left: usize, right: usize, power: i64) {
        let mut index = left;
        while index <= self.size {
            self.tree[index] += power;
            index += index & index.wrapping_neg();
        }
        index = right + 1;
        while index <= self.size {
            self.tree[index] -= power;
            index += index & index.wrapping_neg();
        }
    }

    fn point(&self, mut index: usize) -> i64 {
        let mut result = 0;
        while index > 0 {
            result += self.tree[index];
            index &= index - 1;
        }
        result
    }

    fn measure(&self, index: usize) -> i64 {
        let mut result = self.initial[index];
        for at in self.offsets[index]..self.offsets[index + 1] {
            let divisor = self.divisors[at as usize] as usize;
            let partner = index / divisor;
            result += self.point(divisor);
            if partner != divisor {
                result += self.point(partner);
            }
        }
        result
    }
}

fn main() {
    let input = TokenInput::new();
    let mut words = input.into_iter();
    let size: usize = parse_integer(words.next().unwrap());
    let mut initial = vec![0];
    for _ in 0..size {
        initial.push(parse_integer::<i64>(words.next().unwrap()));
    }
    let mut charges = Charges::new(initial);
    let count: usize = parse_integer(words.next().unwrap());
    let mut output = io::BufWriter::new(io::stdout().lock());
    for _ in 0..count {
        let kind: usize = parse_integer(words.next().unwrap());
        if kind == 1 {
            let index = parse_integer(words.next().unwrap());
            writeln!(output, "{}", charges.measure(index)).unwrap();
        } else {
            let left = parse_integer(words.next().unwrap());
            let right = parse_integer(words.next().unwrap());
            let power = parse_integer(words.next().unwrap());
            charges.irradiate(left, right, power);
        }
    }
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
