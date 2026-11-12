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
    // SAFETY: the writable slice stays live for the call, and its length is bounded by INPUT_SIZE.
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
        // SAFETY: this live slice contains at most OUTPUT_SIZE readable bytes.
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

const INPUT_SIZE: usize = 8192;

struct Input {
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; INPUT_SIZE],
            position: 0,
            length: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = read_input(&mut self.bytes);
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let value = self.bytes[self.position];
        self.position += 1;
        value
    }
    fn number(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        let sign = if c == b'-' {
            c = self.byte();
            -1
        } else {
            1
        };
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        sign * value
    }
}

const MAX_LENGTH: usize = 2000;
const OUTPUT_SIZE: usize = 8192;
const HEADER_RESERVE: usize = 16;
const TAIL: &[u8] = b"bcd";
const LABEL: &[u8] = b" : ";
const NO: &[u8] = b"NO";

fn append_number(mut value: usize, output: &mut [u8], used: &mut usize) {
    const MAX_DIGITS: usize = 4;
    let mut digits = [0_u8; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    output[*used..*used + digits.len() - first].copy_from_slice(&digits[first..]);
    *used += digits.len() - first;
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let n = input.number() as usize;
    let prefix = [b'a'; MAX_LENGTH];
    let mut tail = [0_u8; MAX_LENGTH];
    for (i, c) in tail[..n].iter_mut().enumerate() {
        *c = TAIL[i % TAIL.len()];
    }
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut used = 0;
    for count in 1..=n {
        if output.len() - used < n + HEADER_RESERVE {
            if !write_all(&output[..used]) {
                return 1;
            }
            used = 0;
        }
        append_number(count, &mut output, &mut used);
        output[used..used + LABEL.len()].copy_from_slice(LABEL);
        used += LABEL.len();
        if count < n.min(TAIL.len()) {
            output[used..used + NO.len()].copy_from_slice(NO);
            used += NO.len();
        } else if n < TAIL.len() {
            output[used..used + n].copy_from_slice(&prefix[..n]);
            used += n;
        } else {
            let run = count - TAIL.len();
            output[used..used + run].copy_from_slice(&prefix[..run]);
            used += run;
            output[used..used + n - run].copy_from_slice(&tail[..n - run]);
            used += n - run;
        }
        output[used] = b'\n';
        used += 1;
    }
    if write_all(&output[..used]) {
        0
    } else {
        1
    }
}
