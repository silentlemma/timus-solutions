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

const INPUT_SIZE: usize = 64;
const OUTPUT_SIZE: usize = 32;
const MAX_DIGITS: usize = 20;

struct Input {
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl Input {
    fn next_byte(&mut self) -> u8 {
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

    fn number(&mut self) -> u64 {
        let mut c = self.next_byte();
        while c != 0 && c <= b' ' {
            c = self.next_byte();
        }
        if c == b'+' {
            c = self.next_byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + u64::from(c - b'0');
            c = self.next_byte();
        }
        value
    }
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

const FIRST_ODD_PRIME: u32 = 3;
const FIRST_WHEEL_CANDIDATE: u32 = 5;
const WHEEL: u32 = 6;

fn remove_factor(factor: u32, rest: &mut u32, phi: &mut u32) {
    if *rest % factor == 0 {
        *phi -= *phi / factor;
        while *rest % factor == 0 {
            *rest /= factor;
        }
    }
}

// The C runtime calls this symbol directly.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input {
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.number() as u32;
    let (mut rest, mut phi) = (n, n);
    remove_factor(2, &mut rest, &mut phi);
    remove_factor(FIRST_ODD_PRIME, &mut rest, &mut phi);
    // The remaining prime factors are 1 or 5 modulo 6.
    let mut factor = FIRST_WHEEL_CANDIDATE;
    let mut step = 2;
    while factor * factor <= rest {
        remove_factor(factor, &mut rest, &mut phi);
        factor += step;
        step = WHEEL - step;
    }
    if rest > 1 {
        phi -= phi / rest;
    }
    let mut output = [0; OUTPUT_SIZE];
    let mut used = 0;
    write_number(&mut output, &mut used, u64::from(phi / 2));
    output[used] = b'\n';
    used += 1;
    i32::from(!write_all(&output[..used]))
}
