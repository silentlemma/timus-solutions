#![no_main]

fn solve_entry() {
    let mut words = NativeNumbers::new();
    let n = words.next().unwrap() as usize;
    let m = words.next().unwrap() as usize;
    let mut plan: Vec<i64> = words.by_ref().take(m).collect();
    let mut first = 0;
    let mut output = NativeOutput::new();
    let mut stock = 0i64;
    for i in 0..n {
        // after t months of the same change x the stock is stock + t x, which
        // must reach the plan of that month; x is rounded up, also below zero
        let x = plan[first..]
            .iter()
            .chain(&plan[..first])
            .enumerate()
            .map(|(t, &target)| -(stock - target).div_euclid((t + 1) as i64))
            .max()
            .unwrap();
        if i != 0 {
            output.bytes(b" ");
        }
        output.integer(x);
        stock += x;
        if i + 1 < n {
            plan[first] = words.next().unwrap();
            first = (first + 1) % m;
        }
    }
    output.bytes(b"\n");
    output.flush();
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
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let negative = byte == b'-';
        if negative || byte == b'+' {
            byte = self.byte().expect("incomplete integer");
        }
        assert!(byte.is_ascii_digit());
        let mut value = 0_i64;
        loop {
            let digit = i64::from(byte - b'0');
            value = if negative {
                value * 10 - digit
            } else {
                value * 10 + digit
            };
            match self.byte() {
                Some(next) if next.is_ascii_digit() => byte = next,
                Some(next) => {
                    assert!(next.is_ascii_whitespace());
                    break;
                }
                None => break,
            }
        }
        Some(value)
    }
}

const NATIVE_OUTPUT_BYTES: usize = 8192;

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
    fn integer(&mut self, value: i64) {
        if value < 0 {
            self.bytes(b"-");
        }
        self.unsigned(value.unsigned_abs());
    }
}
