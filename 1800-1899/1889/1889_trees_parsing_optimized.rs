#![no_main]

use std::collections::BTreeMap;

const UNKNOWN: &str = "unknown";

// every block of size phrases is one language, and no language is used in
// two blocks
fn fits(phrases: &[usize], size: usize, seen: &mut [usize], epoch: usize) -> bool {
    for block in phrases.chunks(size) {
        let mut language = 0;
        for &word in block {
            if word == 0 {
                continue;
            }
            if language == 0 {
                language = word;
            } else if language != word {
                return false;
            }
        }
        if language != 0 {
            if seen[language] == epoch {
                return false;
            }
            seen[language] = epoch;
        }
    }
    true
}

fn solve_entry() {
    let input = String::from_utf8(native_read_all()).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = parse_integer(words.next().unwrap());
    let mut languages = BTreeMap::new();
    let mut next_id = 1;
    let phrases: Vec<usize> = words
        .take(n)
        .map(|word| {
            if word == UNKNOWN {
                0
            } else {
                *languages.entry(word).or_insert_with(|| {
                    let id = next_id;
                    next_id += 1;
                    id
                })
            }
        })
        .collect();
    let mut seen = vec![0; next_id];
    let mut out = NativeOutput::new();
    let mut first = true;
    for k in divisors(n) {
        if fits(&phrases, n / k, &mut seen, k) {
            if !first {
                out.bytes(b" ");
            }
            first = false;
            out.unsigned(k as u64);
        }
    }
    if first {
        out.bytes(b"Igor is wrong.");
    }
    out.bytes(b"\n");
    out.flush();
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
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

// Return after all native output writes have completed.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    native_setup();
    solve_entry();
    0
}

const NATIVE_INPUT_BYTES: usize = 4096;

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn native_read(fd: i32, data: *mut u8, size: u32) -> i32;
    #[link_name = "_write"]
    fn native_write(fd: i32, data: *const u8, size: u32) -> i32;
    fn _setmode(fd: i32, mode: i32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn native_read(fd: i32, data: *mut u8, size: usize) -> isize;
    #[link_name = "write"]
    fn native_write(fd: i32, data: *const u8, size: usize) -> isize;
}

fn native_setup() {
    #[cfg(windows)]
    {
        const BINARY_MODE: i32 = 0x8000;
        // SAFETY: descriptors zero/one are the inherited standard streams.
        unsafe {
            assert!(_setmode(0, BINARY_MODE) != -1);
            assert!(_setmode(1, BINARY_MODE) != -1);
        }
    }
}

fn native_read_all() -> Vec<u8> {
    let mut data = Vec::new();
    let mut block = [0_u8; NATIVE_INPUT_BYTES];
    loop {
        // SAFETY: the live writable array is passed with its bounded exact size.
        let count = unsafe {
            #[cfg(windows)]
            {
                native_read(0, block.as_mut_ptr(), block.len() as u32)
            }
            #[cfg(not(windows))]
            {
                native_read(0, block.as_mut_ptr(), block.len())
            }
        };
        if count == 0 {
            break;
        }
        if count < 0 {
            #[cfg(not(windows))]
            if std::io::Error::last_os_error().kind() == std::io::ErrorKind::Interrupted {
                continue;
            }
            panic!("input read failed");
        }
        data.extend_from_slice(&block[..count as usize]);
    }
    data
}

fn native_write_all(mut data: &[u8]) {
    while !data.is_empty() {
        // SAFETY: the live readable slice is bounded by the documented output size.
        let count = unsafe {
            #[cfg(windows)]
            {
                native_write(1, data.as_ptr(), data.len() as u32)
            }
            #[cfg(not(windows))]
            {
                native_write(1, data.as_ptr(), data.len())
            }
        };
        if count < 0 {
            #[cfg(not(windows))]
            if std::io::Error::last_os_error().kind() == std::io::ErrorKind::Interrupted {
                continue;
            }
            panic!("output write failed");
        }
        assert!(count > 0);
        data = &data[count as usize..];
    }
}

const NATIVE_OUTPUT_BYTES: usize = 8192;

fn divisors(n: usize) -> Vec<usize> {
    let mut values = Vec::new();
    let mut d = 1;
    while d <= n / d {
        if n % d == 0 {
            values.push(d);
            if d != n / d {
                values.push(n / d);
            }
        }
        d += 1;
    }
    values.sort_unstable();
    values
}

struct NativeOutput {
    data: [u8; NATIVE_OUTPUT_BYTES],
    size: usize,
}
impl NativeOutput {
    fn new() -> Self {
        Self {
            data: [0; NATIVE_OUTPUT_BYTES],
            size: 0,
        }
    }
    fn flush(&mut self) {
        native_write_all(&self.data[..self.size]);
        self.size = 0;
    }
    fn bytes(&mut self, mut text: &[u8]) {
        while !text.is_empty() {
            let count = (self.data.len() - self.size).min(text.len());
            self.data[self.size..self.size + count].copy_from_slice(&text[..count]);
            self.size += count;
            text = &text[count..];
            if self.size == self.data.len() {
                self.flush();
            }
        }
    }
    fn unsigned(&mut self, mut value: u64) {
        let mut digits = [0_u8; 20];
        let mut first = digits.len();
        loop {
            first -= 1;
            digits[first] = b'0' + (value % 10) as u8;
            value /= 10;
            if value == 0 {
                break;
            }
        }
        self.bytes(&digits[first..]);
    }
}
