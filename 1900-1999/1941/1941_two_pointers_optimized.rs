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
}
const SYMBOL_COUNT: usize = 90;
const ALPHABET_SIZE: usize = SYMBOL_COUNT * SYMBOL_COUNT * SYMBOL_COUNT;
const LOWEST_SYMBOL: u8 = b'!';
const MAX_PATTERN: usize = 8000;
const OUTPUT_SIZE: usize = 20;

fn code(input: &mut Input, first: u8) -> usize {
    let second = input.byte();
    let third = input.byte();
    ((first - LOWEST_SYMBOL) as usize * SYMBOL_COUNT + (second - LOWEST_SYMBOL) as usize)
        * SYMBOL_COUNT
        + (third - LOWEST_SYMBOL) as usize
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let mut deficit = vec![0_i16; ALPHABET_SIZE];
    let mut ring = [0_u32; MAX_PATTERN];
    let mut size = 0;
    let mut c = input.byte();
    while c != 0 && c != b'\n' {
        if c > b' ' {
            deficit[code(&mut input, c)] += 1;
            size += 1;
        }
        c = input.byte();
    }
    let (mut missing, mut position, mut filled, mut answer) = (size, 0, 0, 0);
    c = input.byte();
    while c != 0 {
        if c > b' ' {
            if filled == size {
                let old = ring[position] as usize;
                if deficit[old] >= 0 {
                    missing += 1;
                }
                deficit[old] += 1;
            } else {
                filled += 1;
            }
            let letter = code(&mut input, c);
            if deficit[letter] > 0 {
                missing -= 1;
            }
            // A full or partial window has at most size <= 8000 occurrences of any letter.
            deficit[letter] -= 1;
            ring[position] = letter as u32;
            position += 1;
            if position == size {
                position = 0;
            }
            if missing == 0 {
                answer += 1;
            }
        }
        c = input.byte();
    }
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut first = output.len() - 1;
    output[first] = b'\n';
    loop {
        first -= 1;
        output[first] = (answer % 10) as u8 + b'0';
        answer /= 10;
        if answer == 0 {
            break;
        }
    }
    write_all(&output[first..]);
    0
}
