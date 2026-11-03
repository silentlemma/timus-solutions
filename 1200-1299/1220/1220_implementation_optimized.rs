#![no_main]

use std::os::raw::c_int;

const IO_BYTES: usize = 512;
const DECIMAL_BYTES: usize = 20;
const RADIX: u64 = 10;

extern "C" {
    fn read(fd: c_int, buffer: *mut u8, length: usize) -> isize;
    fn write(fd: c_int, buffer: *const u8, length: usize) -> isize;
}

struct Input {
    bytes: [u8; IO_BYTES],
    position: usize,
    length: usize,
}
impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; IO_BYTES],
            position: 0,
            length: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            let count = unsafe { read(0, self.bytes.as_mut_ptr(), IO_BYTES) };
            if count <= 0 {
                return 0;
            }
            self.position = 0;
            self.length = count as usize;
        }
        let value = self.bytes[self.position];
        self.position += 1;
        value
    }
    fn number(&mut self) -> i64 {
        let mut ch = self.byte();
        while ch != 0 && !ch.is_ascii_digit() && ch != b'-' {
            ch = self.byte();
        }
        let negative = ch == b'-';
        if negative {
            ch = self.byte();
        }
        let mut value = 0i64;
        while ch.is_ascii_digit() {
            value = value * RADIX as i64 + i64::from(ch - b'0');
            ch = self.byte();
        }
        if negative {
            -value
        } else {
            value
        }
    }
}
struct Output {
    bytes: [u8; IO_BYTES],
    length: usize,
}
impl Output {
    fn new() -> Self {
        Self {
            bytes: [0; IO_BYTES],
            length: 0,
        }
    }
    fn flush(&mut self) {
        let mut start = 0;
        while start < self.length {
            let count = unsafe { write(1, self.bytes[start..].as_ptr(), self.length - start) };
            if count <= 0 {
                break;
            }
            start += count as usize;
        }
        self.length = 0;
    }
    fn byte(&mut self, value: u8) {
        if self.length == IO_BYTES {
            self.flush();
        }
        self.bytes[self.length] = value;
        self.length += 1;
    }
    fn number(&mut self, mut value: u64) {
        let mut digits = [0u8; DECIMAL_BYTES];
        let mut start = DECIMAL_BYTES;
        loop {
            start -= 1;
            digits[start] = b'0' + (value % RADIX) as u8;
            value /= RADIX;
            if value == 0 {
                break;
            }
        }
        for digit in &digits[start..] {
            self.byte(*digit);
        }
    }
}
const MAX_STACKS: usize = 1000;
const MAX_OPERATIONS: usize = 100000;
const PER_BLOCK: usize = 8;
const VALUE_BITS: usize = 30;
const BYTE_BITS: usize = 8;
const BLOCK_BYTES: usize = PER_BLOCK * VALUE_BITS / BYTE_BITS;
const MAX_BLOCKS: usize = MAX_OPERATIONS / PER_BLOCK + MAX_STACKS + 1;
const NONE: u16 = u16::MAX;
const VALUE_MASK: u64 = (1 << VALUE_BITS) - 1;

struct Stacks {
    values: [[u8; BLOCK_BYTES]; MAX_BLOCKS],
    below: [u16; MAX_BLOCKS],
    top: [u16; MAX_STACKS],
    fill: [u8; MAX_STACKS],
    used: usize,
    free: u16,
}
static mut STORAGE: Stacks = Stacks {
    values: [[0; BLOCK_BYTES]; MAX_BLOCKS],
    below: [0; MAX_BLOCKS],
    top: [NONE; MAX_STACKS],
    fill: [0; MAX_STACKS],
    used: 0,
    free: NONE,
};

impl Stacks {
    fn cell(&mut self, block: usize, position: usize, replacement: Option<u32>) -> u32 {
        let bit = position * VALUE_BITS;
        let start = bit / BYTE_BITS;
        let end = (bit + VALUE_BITS + BYTE_BITS - 1) / BYTE_BITS;
        let shift = bit % BYTE_BITS;
        let mut word = 0u64;
        for offset in start..end {
            word |= u64::from(self.values[block][offset]) << ((offset - start) * BYTE_BITS);
        }
        let value = ((word >> shift) & VALUE_MASK) as u32;
        if let Some(new_value) = replacement {
            word = (word & !(VALUE_MASK << shift)) | (u64::from(new_value) << shift);
            for offset in start..end {
                self.values[block][offset] = (word >> ((offset - start) * BYTE_BITS)) as u8;
            }
        }
        value
    }
    fn push(&mut self, stack: usize, value: u32) {
        if self.fill[stack] == 0 || usize::from(self.fill[stack]) == PER_BLOCK {
            let block;
            if self.free == NONE {
                block = self.used as u16;
                self.used += 1;
            } else {
                block = self.free;
                self.free = self.below[usize::from(block)];
            }
            self.below[usize::from(block)] = self.top[stack];
            self.top[stack] = block;
            self.fill[stack] = 0;
        }
        self.cell(
            usize::from(self.top[stack]),
            usize::from(self.fill[stack]),
            Some(value),
        );
        self.fill[stack] += 1;
    }
    fn pop(&mut self, stack: usize) -> u32 {
        self.fill[stack] -= 1;
        let block = usize::from(self.top[stack]);
        let value = self.cell(block, usize::from(self.fill[stack]), None);
        if self.fill[stack] == 0 {
            self.top[stack] = self.below[block];
            self.below[block] = self.free;
            self.free = block as u16;
            if self.top[stack] != NONE {
                self.fill[stack] = PER_BLOCK as u8;
            }
        }
        value
    }
}

// The C ABI entry avoids unused Rust stdio/startup; all IO buffers are bounded.
#[no_mangle]
pub extern "C" fn main() -> c_int {
    let mut input = Input::new();
    let mut output = Output::new();
    // One entry/thread owns this zero-initialized static storage for the whole run.
    let stacks = unsafe { &mut STORAGE };
    let operations = input.number() as usize;
    for _ in 0..operations {
        let mut command = input.byte();
        while command != b'U' && command != b'O' {
            command = input.byte();
        }
        let stack = input.number() as usize - 1;
        if command == b'U' {
            stacks.push(stack, input.number() as u32);
        } else {
            output.number(u64::from(stacks.pop(stack)));
            output.byte(b'\n');
        }
    }
    output.byte(b'\n');
    output.flush();
    0
}
