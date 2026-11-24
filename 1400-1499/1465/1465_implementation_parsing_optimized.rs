#![no_main]

const LIMIT: i64 = 200; // the values repeat with PERIOD from 52 on, well below this
const PERIOD: i64 = 34;
const TAKE: usize = 3; // a move takes up to three files out of play

fn solve_entry() {
    let mut n = NativeNumbers::new().next().unwrap();
    // Dawson's chess: a row of n files plays like the octal game 0.137, where
    // a move takes one file (only if it is all), two (leaving one row) or three
    // (leaving up to two rows); White, moving first, wins when the value is not 0
    let limit = LIMIT as usize;
    let mut g = vec![0usize; limit + 1];
    // The mex is bounded by the number of legal moves, hence at most LIMIT.
    // XOR values fit the next power of two; epochs avoid clearing per row.
    let mut seen = vec![0_usize; (limit + 1).next_power_of_two()];
    for size in 1..=limit {
        if size == 1 {
            seen[0] = size;
        }
        if size >= 2 {
            seen[g[size - 2]] = size;
        }
        if size >= TAKE {
            for left in 0..=size - TAKE {
                seen[g[left] ^ g[size - TAKE - left]] = size;
            }
        }
        while seen[g[size]] == size {
            g[size] += 1;
        }
    }
    if n > LIMIT {
        n = LIMIT - PERIOD + (n - LIMIT) % PERIOD;
    }
    native_write_all(if g[n as usize] != 0 {
        b"White\n"
    } else {
        b"Black\n"
    });
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.

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

// SAFETY: the live writable array is passed with its bounded exact size.
