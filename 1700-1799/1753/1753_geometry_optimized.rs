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
const SCALE: u64 = 1000000;

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

// The C runtime calls this symbol directly.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input {
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let rim = input.number();
    let book = input.number();
    let shift = if book > 2 * rim {
        let ratio = (book as f64 / (2 * rim) as f64).cbrt();
        let factor = (ratio - 1.0) * (ratio + 1.0);
        rim as f64 * factor * factor.sqrt()
    } else {
        0.0
    };
    let value = (shift * SCALE as f64).round() as u64;
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
    i32::from(!write_all(&output[..used]))
}
