#![no_main]

use std::collections::BTreeSet;

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
}

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_write"]
    fn system_write(fd: i32, buffer: *const u8, length: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "write"]
    fn system_write(fd: i32, buffer: *const u8, length: usize) -> isize;
}

const MAX_NAME: usize = 20;
const LIMIT: usize = 20;
const OUTPUT_SIZE: usize = 512;
const ASCII_SPACE: i32 = b' ' as i32;

fn byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads standard input.
    unsafe { getchar() }
}

fn write_all(mut buffer: &[u8]) {
    while !buffer.is_empty() {
        // SAFETY: the live slice contains at most OUTPUT_SIZE readable bytes.
        let count = unsafe {
            #[cfg(windows)]
            {
                system_write(1, buffer.as_ptr(), buffer.len() as u32)
            }
            #[cfg(not(windows))]
            {
                system_write(1, buffer.as_ptr(), buffer.len())
            }
        };
        if count <= 0 {
            return;
        }
        buffer = &buffer[count as usize..];
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut names = BTreeSet::new();
    let mut sun = [0_u8; MAX_NAME];
    sun[..b"sun".len()].copy_from_slice(b"sun");
    names.insert(sun);
    loop {
        let mut operation = byte();
        while operation >= 0 && operation <= ASCII_SPACE {
            operation = byte();
        }
        if operation < 0 {
            return 0;
        }
        let mut argument = [0_u8; MAX_NAME];
        let mut length = 0;
        let mut c = byte();
        while c > ASCII_SPACE {
            argument[length] = c as u8;
            length += 1;
            c = byte();
        }
        if operation == b'+' as i32 {
            names.insert(argument);
            continue;
        }
        let mut output = [0_u8; OUTPUT_SIZE];
        output[..length].copy_from_slice(&argument[..length]);
        output[length] = b'\n';
        let mut used = length + 1;
        // Zero padding sorts before every valid character, preserving ordinary lexicographic order.
        for name in names.range(argument..).take(LIMIT) {
            if name[..length] != argument[..length] {
                break;
            }
            let size = name.iter().position(|&c| c == 0).unwrap_or(MAX_NAME);
            output[used..used + 2].copy_from_slice(b"  ");
            used += 2;
            output[used..used + size].copy_from_slice(&name[..size]);
            used += size;
            output[used] = b'\n';
            used += 1;
        }
        // At most 21 + 20*23 = 481 bytes, regardless of the total number of queries.
        write_all(&output[..used]);
    }
}
