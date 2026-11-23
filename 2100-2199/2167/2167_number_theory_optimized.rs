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
}

const OUTPUT_SIZE: usize = 4096;
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

const BITS: usize = 20; // every number of the message is below 2^20
const LIMIT: usize = 1 << BITS;

fn prime(value: usize, composite: &[u64]) -> bool {
    value == 2
        || (value > 1 && value & 1 == 1 && composite[value >> 7] >> ((value >> 1) & 63) & 1 == 0)
}

fn sieve() -> Vec<u64> {
    // One bit per odd integer replaces the full prime-prefix trie.
    let mut composite = vec![0_u64; LIMIT / 128];
    let mut divisor = 3;
    while divisor * divisor < LIMIT {
        if prime(divisor, &composite) {
            for multiple in (divisor * divisor..LIMIT).step_by(2 * divisor) {
                composite[multiple >> 7] |= 1 << ((multiple >> 1) & 63);
            }
        }
        divisor += 2;
    }
    composite
}

fn minimum_key(value: usize, composite: &[u64]) -> usize {
    // Increasing keys give the minimum exactly; XOR permutes the finite domain,
    // so a key reaching prime 2 always exists. No precomputed search bound is used.
    let mut key = 0;
    while !prime(value ^ key, composite) {
        key += 1;
    }
    key
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let composite = sieve();
    let mut input = Input::new();
    let count = input.number() as usize;
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut used = 0;
    for _ in 0..count {
        let key = minimum_key(input.number() as usize, &composite);
        if used + MAX_DIGITS + 1 > OUTPUT_SIZE {
            if !write_all(&output[..used]) {
                return 1;
            }
            used = 0;
        }
        write_number(&mut output, &mut used, key);
        output[used] = b'\n';
        used += 1;
    }
    if write_all(&output[..used]) {
        0
    } else {
        1
    }
}
