#![no_main]

macro_rules! native_println {
    () => { native_write_all(b"\n") };
    ($($argument:tt)*) => {{
        let mut output = NativeOutput::new();
        std::fmt::Write::write_fmt(&mut output, format_args!($($argument)*)).unwrap();
        std::fmt::Write::write_str(&mut output, "\n").unwrap();
        output.flush();
    }};
}

// the sum of |a_i - a_j| over all pairs: in sorted order the i-th value
// is larger than the i values before it
fn pair_sum(a: &mut [i32]) -> i64 {
    a.sort_unstable();
    let (mut total, mut before) = (0i64, 0i64);
    for (i, &v) in a.iter().enumerate() {
        total += i64::from(v) * i as i64 - before;
        before += i64::from(v);
    }
    total
}

fn solve_entry() {
    let mut it = NativeNumbers::new();
    let n = it.next().unwrap();
    let mut x = Vec::with_capacity(n as usize);
    let mut y = Vec::with_capacity(n as usize);
    for _ in 0..n {
        x.push(it.next().unwrap() as i32);
        y.push(it.next().unwrap() as i32);
    }
    // walking along the streets, a visit covers |dx| + |dy|
    let pairs = n * (n - 1) / 2;
    native_println!("{}", (pair_sum(&mut x) + pair_sum(&mut y)) / pairs);
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

const NATIVE_OUTPUT_BYTES: usize = 256;

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
}

impl std::fmt::Write for NativeOutput {
    fn write_str(&mut self, text: &str) -> std::fmt::Result {
        let bytes = text.as_bytes();
        if bytes.len() > self.data.len() - self.size {
            self.flush();
        }
        if bytes.len() >= self.data.len() {
            native_write_all(bytes);
        } else {
            self.data[self.size..self.size + bytes.len()].copy_from_slice(bytes);
            self.size += bytes.len();
        }
        Ok(())
    }
}
