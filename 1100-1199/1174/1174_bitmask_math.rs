#![no_main]

use std::ffi::{c_int, c_void};

#[cfg(unix)]
extern "C" {
    fn read(fd: c_int, buffer: *mut c_void, count: usize) -> isize;
    fn write(fd: c_int, buffer: *const c_void, count: usize) -> isize;
}

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn read(fd: c_int, buffer: *mut c_void, count: u32) -> c_int;
    #[link_name = "_write"]
    fn write(fd: c_int, buffer: *const c_void, count: u32) -> c_int;
}

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const BUFFER_SIZE: usize = 128;
const INPUT_RADIX: u32 = 10;

struct Input {
    bytes: [u8; BUFFER_SIZE],
    start: usize,
    end: usize,
}

impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; BUFFER_SIZE],
            start: 0,
            end: 0,
        }
    }

    fn byte(&mut self) -> Option<u8> {
        if self.start == self.end {
            // The runtime receives the pointer and size of the live buffer.
            let size = unsafe { read(STDIN, self.bytes.as_mut_ptr().cast(), BUFFER_SIZE as _) };
            if size <= 0 {
                return None;
            }
            self.start = 0;
            self.end = size as usize;
        }
        let byte = self.bytes[self.start];
        self.start += 1;
        Some(byte)
    }

    fn number(&mut self) -> Option<u32> {
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let mut value = 0;
        while byte.is_ascii_digit() {
            value = value * INPUT_RADIX + u32::from(byte - b'0');
            byte = self.byte().unwrap_or(b' ');
        }
        Some(value)
    }
}

fn send(bytes: &[u8]) -> c_int {
    // The answer slice remains initialized for the duration of the call.
    let written = unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) };
    c_int::from(written as usize != bytes.len())
}

const MAX_SIZE: usize = 100;
const MAX_LIMBS: usize = 18;
const BASE: u64 = 1_000_000_000;
const LIMB_DIGITS: usize = 9;
const DECIMAL: u64 = 10;

fn apply(rank: &mut [u64; MAX_LIMBS], limbs: &mut usize, scale: u64, mut add: u64) {
    for limb in &mut rank[..*limbs] {
        let product = *limb * scale + add;
        *limb = product % BASE;
        add = product / BASE;
    }
    if add != 0 {
        rank[*limbs] = add;
        *limbs += 1;
    }
}

fn rank_at_positions(positions: &[usize]) -> ([u64; MAX_LIMBS], usize) {
    let mut rank = [0; MAX_LIMBS];
    let mut limbs = 1;
    let mut seen = 0u128;
    let (mut scale, mut add, mut parity) = (1, 0, 0);
    for (value, &position) in positions.iter().enumerate().skip(1) {
        let bit = 1u128 << position;
        let left = (seen & (bit - 1)).count_ones() as u64;
        seen |= bit;
        let value = value as u64;
        let step = if parity == 0 { value - 1 - left } else { left };
        if scale * value > BASE {
            apply(&mut rank, &mut limbs, scale, add);
            (scale, add) = (1, 0);
        }
        // Compose several small radices before updating the full rank.
        // The parity of the new rank does not require carrying the limbs.
        scale *= value;
        add = add * value + step;
        parity = (parity * value + step) & 1;
    }
    apply(&mut rank, &mut limbs, scale, add);
    (rank, limbs)
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut input = Input::new();
    let Some(n) = input.number() else {
        return 1;
    };
    let n = n as usize;
    let mut positions = [0; MAX_SIZE + 1];
    for index in 0..n {
        let Some(value) = input.number() else {
            return 1;
        };
        positions[value as usize] = index;
    }

    let (mut rank, mut limbs) = rank_at_positions(&positions[..=n]);

    let mut index = 0;
    while rank[index] == BASE - 1 {
        rank[index] = 0;
        index += 1;
    }
    rank[index] += 1;
    limbs = limbs.max(index + 1);

    let mut output = [0; MAX_LIMBS * LIMB_DIGITS + 1];
    let mut end = output.len() - 1;
    output[end] = b'\n';
    for limb in &rank[..limbs - 1] {
        let mut number = *limb;
        for _ in 0..LIMB_DIGITS {
            end -= 1;
            output[end] = b'0' + (number % DECIMAL) as u8;
            number /= DECIMAL;
        }
    }
    let mut number = rank[limbs - 1];
    loop {
        end -= 1;
        output[end] = b'0' + (number % DECIMAL) as u8;
        number /= DECIMAL;
        if number == 0 {
            break;
        }
    }
    send(&output[end..])
}
