#![no_main]

fn isqrt(x: u64) -> u64 {
    let mut r = (x as f64).sqrt() as u64;
    while r * r > x {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= x {
        r += 1;
    }
    r
}

// Sorenson and Webster, arXiv:1509.00864, Theorem 1.1:
// the first twelve prime bases are deterministic throughout the input range.
const PRIME_BASES: [u64; 12] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37];

fn multiply_mod(a: u64, b: u64, modulus: u64) -> u64 {
    (u128::from(a) * u128::from(b) % u128::from(modulus)) as u64
}

fn power_mod(mut a: u64, mut exponent: u64, modulus: u64) -> u64 {
    let mut answer = 1;
    while exponent != 0 {
        if exponent & 1 != 0 {
            answer = multiply_mod(answer, a, modulus);
        }
        a = multiply_mod(a, a, modulus);
        exponent >>= 1;
    }
    answer
}

fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    for p in PRIME_BASES {
        if n % p == 0 {
            return n == p;
        }
    }
    let shifts = (n - 1).trailing_zeros();
    let odd = (n - 1) >> shifts;
    'bases: for base in PRIME_BASES {
        let mut value = power_mod(base, odd, n);
        if value == 1 || value == n - 1 {
            continue;
        }
        for _ in 1..shifts {
            value = multiply_mod(value, value, n);
            if value == n - 1 {
                continue 'bases;
            }
        }
        return false;
    }
    true
}

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let next = a % b;
        a = b;
        b = next;
    }
    a
}

fn rho_factor(n: u64) -> u64 {
    const GCD_BATCH: usize = 64;
    const MAX_SPAN: usize = 262_144;
    let mut constant = 1_u64;
    loop {
        let step = |value| (multiply_mod(value, value, n) + constant) % n;
        let (mut y, mut span, mut divisor) = (2_u64, 1_usize, 1_u64);
        let (mut x, mut saved) = (0, 0);
        while divisor == 1 && span <= MAX_SPAN {
            x = y;
            for _ in 0..span {
                y = step(y);
            }
            let mut offset = 0;
            while offset < span && divisor == 1 {
                saved = y;
                let mut product = 1;
                for _ in 0..GCD_BATCH.min(span - offset) {
                    y = step(y);
                    product = multiply_mod(product, x.abs_diff(y), n);
                }
                divisor = gcd(product, n);
                offset += GCD_BATCH;
            }
            span *= 2;
        }
        if divisor == n {
            // Replay only the last batch when its product hid a proper factor.
            for _ in 0..GCD_BATCH {
                saved = step(saved);
                divisor = gcd(x.abs_diff(saved), n);
                if divisor != 1 {
                    break;
                }
            }
        }
        if divisor > 1 && divisor < n {
            return divisor;
        }
        constant += 1;
        if constant == n {
            constant = 1;
        }
    }
}

fn factor(n: u64, result: &mut Vec<u64>) {
    if n == 1 {
        return;
    }
    for p in PRIME_BASES {
        if n % p == 0 {
            result.push(p);
            factor(n / p, result);
            return;
        }
    }
    if is_prime(n) {
        result.push(n);
        return;
    }
    let square = isqrt(n);
    if square * square == n {
        let start = result.len();
        factor(square, result);
        let count = result.len() - start;
        for index in 0..count {
            result.push(result[start + index]);
        }
        return;
    }
    let divisor = rho_factor(n);
    factor(divisor, result);
    factor(n / divisor, result);
}

fn count_pairs(c: u64) -> u64 {
    if c == 0 {
        return 1;
    }
    let square = isqrt(c);
    if square * square == c {
        return square / 2 + 1;
    }
    let mut factors = Vec::with_capacity(64);
    factor(c, &mut factors);
    factors.sort_unstable();
    let (mut root, mut first) = (1_u64, 0);
    while first < factors.len() {
        let mut end = first + 1;
        while end < factors.len() && factors[end] == factors[first] {
            end += 1;
        }
        for _ in 0..(end - first) / 2 {
            root *= factors[first];
        }
        first = end;
    }
    root / 2 + 1
}

fn solve_entry() {
    let value = NativeNumbers::new().next().unwrap() as u64;
    let mut out = NativeOutput::new();
    out.unsigned(count_pairs(value));
    out.bytes(b"\n");
    out.flush();
}

const NATIVE_INPUT_BYTES: usize = 256;

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn native_read(fd: i32, data: *mut u8, size: u32) -> i32;
    #[link_name = "_write"]
    fn native_write(fd: i32, data: *const u8, size: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn native_read(fd: i32, data: *mut u8, size: usize) -> isize;
    #[link_name = "write"]
    fn native_write(fd: i32, data: *const u8, size: usize) -> isize;
}

fn native_setup() {}

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

const NATIVE_OUTPUT_BYTES: usize = 256;

struct NativeNumbers {
    data: [u8; NATIVE_INPUT_BYTES],
    position: usize,
    length: usize,
}

impl NativeNumbers {
    fn new() -> Self {
        Self {
            data: [0; NATIVE_INPUT_BYTES],
            position: 0,
            length: 0,
        }
    }

    fn refill(&mut self) -> bool {
        loop {
            // SAFETY: the live writable array is passed with its exact bounded length.
            let count = unsafe {
                #[cfg(windows)]
                {
                    native_read(0, self.data.as_mut_ptr(), self.data.len() as u32)
                }
                #[cfg(not(windows))]
                {
                    native_read(0, self.data.as_mut_ptr(), self.data.len())
                }
            };
            if count < 0 {
                #[cfg(not(windows))]
                if std::io::Error::last_os_error().kind() == std::io::ErrorKind::Interrupted {
                    continue;
                }
                panic!("input read failed");
            }
            self.position = 0;
            self.length = count as usize;
            return count != 0;
        }
    }

    #[inline]
    fn byte(&mut self) -> Option<u8> {
        if self.position == self.length && !self.refill() {
            return None;
        }
        let byte = self.data[self.position];
        self.position += 1;
        Some(byte)
    }
}

impl Iterator for NativeNumbers {
    type Item = i64;
    // Input bounds guarantee that each decimal token fits its destination integer.
    // Accumulate negative values directly so the minimum signed integer also fits.
    #[inline]
    fn next(&mut self) -> Option<i64> {
        let mut first = self.byte()?;
        while first.is_ascii_whitespace() {
            first = self.byte()?;
        }
        let negative = first == b'-';
        if negative || first == b'+' {
            first = self.byte().expect("incomplete integer");
        }
        assert!(first.is_ascii_digit());
        let mut value = -i64::from(first - b'0');
        loop {
            let start = self.position;
            // Work inside one checked slice and commit the cursor
            // only at a token or block boundary.
            for (offset, &byte) in self.data[start..self.length].iter().enumerate() {
                if byte.is_ascii_digit() {
                    value = value * 10 - i64::from(byte - b'0');
                } else {
                    assert!(byte.is_ascii_whitespace());
                    self.position = start + offset + 1;
                    return Some(if negative { value } else { -value });
                }
            }
            self.position = self.length;
            if !self.refill() {
                return Some(if negative { value } else { -value });
            }
        }
    }
}

// SAFETY: the live writable array is passed with its bounded exact size.

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

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    #[link_name = "_exit"]
    fn native_exit(code: i32) -> !;
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    native_setup();
    solve_entry();
    // SAFETY: native writes completed; no buffered C output remains to flush.
    unsafe { native_exit(0) }
}
