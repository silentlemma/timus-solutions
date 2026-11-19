#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments.
    unsafe { getchar() }
}

fn write_byte(byte: u8) {
    // SAFETY: putchar accepts a byte promoted to int and has no pointers.
    unsafe {
        putchar(i32::from(byte));
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const MAXIMUM: usize = 20000;
    // Input length determines the traversal, so retain the encoded line once.
    let mut encoded = [0u8; MAXIMUM];
    let mut size = 0;
    loop {
        let byte = read_byte();
        if byte < 0 || byte == b'\n' as i32 || byte == b'\r' as i32 {
            break;
        }
        encoded[size] = byte as u8;
        size += 1;
    }
    fn decode(encoded: &[u8], at: &mut usize, output: &mut [u8]) {
        if output.is_empty() {
            return;
        }
        let middle = (output.len() - 1) / 2;
        output[middle] = encoded[*at];
        *at += 1;
        decode(encoded, at, &mut output[..middle]);
        decode(encoded, at, &mut output[middle + 1..]);
    }
    let mut output = [0u8; MAXIMUM];
    decode(&encoded[..size], &mut 0, &mut output[..size]);
    for &byte in &output[..size] {
        write_byte(byte);
    }
    write_byte(b'\n');
    0
}
