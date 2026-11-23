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

fn solve_entry() {
    let input = String::from_utf8(native_read_all()).unwrap();
    let mut lines = input.split('\n');
    let first: Vec<usize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| parse_integer(x))
        .collect();
    let (n, m) = (first[0], first[1]);
    // read whole: the text may start with spaces
    let text = lines.next().unwrap_or("").trim_end_matches('\r').as_bytes();
    // run[i]: how many letters and spaces start at position i
    let mut run = vec![0u32; text.len() + 1];
    for i in (0..text.len()).rev() {
        if text[i].is_ascii_alphabetic() || text[i] == b' ' {
            run[i] = run[i + 1] + 1;
        }
    }
    // the farthest reach never moves back, so the longest message each time is best
    let (mut pos, mut count) = (0, 0);
    while pos < text.len() {
        pos += n.max(m.min(run[pos] as usize));
        count += 1;
    }
    native_println!("{}", count);
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
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

fn native_read_all() -> Vec<u8> {
    let mut data = Vec::new();
    let mut block = [0_u8; NATIVE_INPUT_BYTES];
    loop {
        // SAFETY: the live writable array is passed with its bounded exact size.
        let count = unsafe {
            #[cfg(windows)]
            {
                native_read(0, block.as_mut_ptr(), block.len() as u32)
            }
            #[cfg(not(windows))]
            {
                native_read(0, block.as_mut_ptr(), block.len())
            }
        };
        if count == 0 {
            break;
        }
        if count < 0 {
            #[cfg(not(windows))]
            if std::io::Error::last_os_error().kind() == std::io::ErrorKind::Interrupted {
                continue;
            }
            panic!("input read failed");
        }
        data.extend_from_slice(&block[..count as usize]);
    }
    data
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
