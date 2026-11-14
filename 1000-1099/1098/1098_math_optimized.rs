#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const STEP: usize = 1999;
const MAX_LENGTH: usize = 30_000;
const BUFFER: usize = 1024;
const BITS: usize = u8::BITS as usize;
const BITSET_SIZE: usize = (MAX_LENGTH + BITS - 1) / BITS;

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

const STRIDE: usize = 128;
const CHECKPOINT_COUNT: usize = MAX_LENGTH / STRIDE + 1;

const fn checkpoints() -> [u16; CHECKPOINT_COUNT] {
    let mut table = [0; CHECKPOINT_COUNT];
    let (mut size, mut survivor) = (2, 0);
    while size <= MAX_LENGTH {
        survivor = (survivor + STEP) % size;
        if size % STRIDE == 0 {
            table[size / STRIDE] = survivor as u16;
        }
        size += 1;
    }
    table
}

static CHECKPOINTS: [u16; CHECKPOINT_COUNT] = checkpoints();

fn survivor(length: usize) -> usize {
    // Carry the recurrence over at most STRIDE - 1 sizes after a checkpoint.
    let checkpoint = length / STRIDE;
    let mut survivor = usize::from(CHECKPOINTS[checkpoint]);
    for size in (checkpoint * STRIDE + 1).max(2)..=length {
        survivor = (survivor + STEP) % size;
    }
    survivor
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut questions = [0u8; BITSET_SIZE];
    let mut spaces = [0u8; BITSET_SIZE];
    let mut input = [0u8; BUFFER];
    let mut length = 0;
    loop {
        // The buffer has room for every byte requested from read.
        let count = unsafe { read(STDIN, input.as_mut_ptr().cast(), input.len() as _) };
        if count < 0 {
            return 1;
        }
        if count == 0 {
            break;
        }
        for &byte in &input[..count as usize] {
            if byte == b'\r' || byte == b'\n' {
                continue;
            }
            let cell = length / BITS;
            let bit = 1 << (length % BITS);
            match byte {
                b'?' => questions[cell] |= bit,
                b' ' => spaces[cell] |= bit,
                _ => {}
            }
            length += 1;
        }
    }
    let index = survivor(length);
    let bit = 1 << (index % BITS);
    let answer: &[u8] = if questions[index / BITS] & bit != 0 {
        b"Yes\n"
    } else if spaces[index / BITS] & bit != 0 {
        b"No\n"
    } else {
        b"No comments\n"
    };
    // The answer is a static byte slice, valid throughout the write.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}
