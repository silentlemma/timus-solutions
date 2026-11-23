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

const DIGIT: u32 = 9; // the largest digit

fn solve_entry() {
    let mut s = native_read_all();
    let start = s
        .iter()
        .position(|c| !c.is_ascii_whitespace())
        .unwrap_or(s.len());
    if start != 0 {
        s.drain(..start);
    }
    while s.last().is_some_and(u8::is_ascii_whitespace) {
        s.pop();
    }
    // the rightmost digit that can grow by one while the digits after it give
    // one back; the smallest such change gives the next number
    let mut after = 0u32; // the sum of the digits after position i
    for i in (0..s.len()).rev() {
        let d = (s[i] - b'0') as u32;
        if d < DIGIT && after > 0 {
            s[i] += 1;
            let mut rest = after - 1;
            // the smallest tail with this sum: the digits pushed to the right
            for j in (i + 1..s.len()).rev() {
                let put = rest.min(DIGIT);
                s[j] = b'0' + put as u8;
                rest -= put;
            }
            s.push(b'\n');
            native_write_all(&s);
            return;
        }
        after += d;
    }
    native_println!("-1");
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
