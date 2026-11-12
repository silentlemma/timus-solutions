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
        // SAFETY: the slice stays live and has at most OUTPUT_SIZE bytes.
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

const INPUT_SIZE: usize = 256;

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
    fn word(&mut self) -> u8 {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        let first = c;
        while c > b' ' {
            c = self.byte();
        }
        first
    }
}

const OUTPUT_SIZE: usize = 2048;
const MAX_DIGITS: usize = 20;

fn write_number(output: &mut [u8], used: &mut usize, mut value: usize) {
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
    let count = digits.len() - first;
    output[*used..*used + count].copy_from_slice(&digits[first..]);
    *used += count;
}

const MOST: i32 = 30;
const WORDS_BEFORE_VENUE: usize = 3;
// The C runtime calls this symbol directly.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let tests = input.number();
    let (mut output, mut used) = ([0; OUTPUT_SIZE], 0);
    for _ in 0..tests {
        for _ in 0..WORDS_BEFORE_VENUE {
            input.word();
        }
        let home = input.word() == b'h';
        input.word();
        input.word();
        let x = input.number();
        input.word();
        input.word();
        input.word();
        let y = input.number();
        input.word();
        let (mut lowest, mut highest) = (-1, -1);
        for goals in 0..=MOST {
            let ours = (x + goals, if home { goals } else { x });
            // Equal totals and equal away goals allow either outcome.
            if lowest < 0 && ours >= (y, if home { y } else { 0 }) {
                lowest = goals;
            }
            if ours <= (y + MOST, if home { y } else { MOST }) {
                highest = goals;
            }
        }
        write_number(&mut output, &mut used, lowest as usize);
        output[used] = b' ';
        used += 1;
        write_number(&mut output, &mut used, highest as usize);
        output[used] = b'\n';
        used += 1;
    }
    i32::from(!write_all(&output[..used]))
}
