#![no_main]

const LEGS: i64 = 40;

// At most two bounded integers fit in the stack buffer, including signs and separators.
fn emit(values: &[i64]) {
    let mut buffer = [0_u8; 64];
    let mut position = buffer.len();
    for (index, &value) in values.iter().enumerate().rev() {
        position -= 1;
        buffer[position] = if index + 1 == values.len() {
            b'\n'
        } else {
            b' '
        };
        let mut digits = value.unsigned_abs();
        loop {
            position -= 1;
            buffer[position] = b'0' + (digits % 10) as u8;
            digits /= 10;
            if digits == 0 {
                break;
            }
        }
        if value < 0 {
            position -= 1;
            buffer[position] = b'-';
        }
    }
    native_write_all(&buffer[position..]);
}

fn solve_entry() {
    let mut input = NativeNumbers::new();
    let a = input.next().unwrap() as i64;
    let b = input.next().unwrap() as i64;
    // either every right slipper turns up while the left legs are dressed,
    // or 39 rights do, and then every spare left slipper is thrown away
    // before the last right leg is dressed
    emit(&[(2 * b + LEGS).max(2 * a + LEGS - 1)]);
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

// SAFETY: the live writable array is passed with its bounded exact size.
