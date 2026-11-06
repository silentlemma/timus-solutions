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

const MIN_PAIR: u64 = 4;
const FIRST_ODD_PRIME: u64 = 3;
const INPUT_SIZE: usize = 64;
const OUTPUT_SIZE: usize = 1024;
const MAX_DIGITS: usize = 10;

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

// these bases make Miller-Rabin exact for every n below 3.2 * 10^9
const BASES: [u64; 4] = [2, 3, 5, 7];

fn power(mut b: u64, mut e: u64, m: u64) -> u64 {
    let mut r = 1;
    b %= m;
    while e > 0 {
        if e & 1 == 1 {
            r = r * b % m;
        }
        b = b * b % m;
        e >>= 1;
    }
    r
}

fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    for &b in BASES.iter() {
        if n % b == 0 {
            return n == b;
        }
    }
    let (mut d, mut s) = (n - 1, 0);
    while d % 2 == 0 {
        d /= 2;
        s += 1;
    }
    'bases: for &b in BASES.iter() {
        let mut x = power(b, d, n);
        if x == 1 || x == n - 1 {
            continue;
        }
        for _ in 1..s {
            x = x * x % n;
            if x == n - 1 {
                continue 'bases;
            }
        }
        return false;
    }
    true
}

/// An even n >= 4 as the smallest prime p and n - p.
fn two_primes(n: u64) -> (u64, u64) {
    if n == MIN_PAIR {
        return (2, 2);
    }
    let mut p = FIRST_ODD_PRIME;
    while !(is_prime(p) && is_prime(n - p)) {
        p += 2;
    }
    (p, n - p)
}

fn split(n: u64) -> (u64, u64, u64) {
    if is_prime(n) {
        return (n, 0, 0);
    }
    if n % 2 == 0 {
        let (a, b) = two_primes(n);
        return (a, b, 0);
    }
    if is_prime(n - 2) {
        return (2, n - 2, 0);
    }
    // When three terms are needed, fixing 3 leaves an even number.
    let (a, b) = two_primes(n - FIRST_ODD_PRIME);
    (FIRST_ODD_PRIME, a, b)
}

// The C runtime calls this symbol directly.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input {
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let queries = input.number();
    let mut output = [0; OUTPUT_SIZE];
    let mut used = 0;
    for _ in 0..queries {
        let (a, b, c) = split(input.number());
        write_number(&mut output, &mut used, a);
        for value in [b, c] {
            if value != 0 {
                output[used] = b' ';
                used += 1;
                write_number(&mut output, &mut used, value);
            }
        }
        output[used] = b'\n';
        used += 1;
    }
    i32::from(!write_all(&output[..used]))
}
