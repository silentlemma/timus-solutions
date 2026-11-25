#![no_main]

const CHOICES: usize = 3; // names offered for every problem

const MAX_RECORDS: usize = 16;
const MAX_NAME_BYTES: usize = 20;
#[derive(Clone, Copy)]
struct Name {
    data: [u8; MAX_NAME_BYTES],
    size: usize,
}
impl Name {
    const EMPTY: Self = Self {
        data: [0; MAX_NAME_BYTES],
        size: 0,
    };
    fn bytes(&self) -> &[u8] {
        &self.data[..self.size]
    }
}
impl NativeNumbers {
    fn name(&mut self) -> Name {
        let mut result = Name::EMPTY;
        let mut byte = self.byte().expect("missing name");
        while byte.is_ascii_whitespace() {
            byte = self.byte().expect("missing name");
        }
        loop {
            assert!(result.size < MAX_NAME_BYTES);
            result.data[result.size] = byte;
            result.size += 1;
            match self.byte() {
                Some(next) if !next.is_ascii_whitespace() => byte = next,
                _ => break,
            }
        }
        result
    }
}
fn solve_entry() {
    let mut input = NativeNumbers::new();
    let n = input.next().unwrap() as usize;
    assert!(n <= MAX_RECORDS);
    let mut names = [[Name::EMPTY; CHOICES]; MAX_RECORDS];
    for options in &mut names[..n] {
        for name in options {
            *name = input.name();
        }
    }
    // in the given order, the least name above the previous one leaves the
    // most room for the problems still to come
    let mut selected = [Name::EMPTY; MAX_RECORDS];
    let mut last = Name::EMPTY;
    for chosen in &mut selected[..n] {
        let problem = input.next().unwrap() as usize;
        let mut best: Option<Name> = None;
        for &name in &names[problem - 1] {
            if name.bytes() > last.bytes() && best.map_or(true, |old| name.bytes() < old.bytes()) {
                best = Some(name);
            }
        }
        match best {
            Some(name) => {
                last = name;
                *chosen = name;
            }
            None => {
                native_write_all(b"IMPOSSIBLE\n");
                return;
            }
        }
    }
    let mut output = [0_u8; MAX_RECORDS * (MAX_NAME_BYTES + 1)];
    let mut size = 0;
    for name in &selected[..n] {
        output[size..size + name.size].copy_from_slice(name.bytes());
        size += name.size;
        output[size] = b'\n';
        size += 1;
    }
    native_write_all(&output[..size]);
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
