#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads the standard stream.
    unsafe { getchar() }
}

fn read_number() -> Option<i64> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    if byte < 0 {
        return None;
    }
    let negative = byte == b'-' as i32;
    if negative || byte == b'+' as i32 {
        byte = read_byte();
    }
    let mut value = 0i64;
    while (b'0' as i32..=b'9' as i32).contains(&byte) {
        let digit = i64::from(byte - b'0' as i32);
        // Accumulating negatives directly also accepts i64::MIN.
        value = if negative {
            value * 10 - digit
        } else {
            value * 10 + digit
        };
        byte = read_byte();
    }
    Some(value)
}

fn number() -> i64 {
    read_number().unwrap()
}

fn write_byte(byte: u8) {
    // SAFETY: putchar accepts a byte promoted to int and has no pointers.
    unsafe {
        putchar(i32::from(byte));
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const LETTERS: usize = 26;
    let (rows, _columns, words) = (number(), number(), number());
    let mut counts = [0i32; LETTERS];
    for i in 0..rows + words {
        let mut byte = read_byte();
        while byte >= 0 && byte <= b' ' as i32 {
            byte = read_byte();
        }
        while byte > b' ' as i32 {
            counts[(byte - b'A' as i32) as usize] += if i < rows { 1 } else { -1 };
            byte = read_byte();
        }
    }
    for (letter, &count) in counts.iter().enumerate() {
        for _ in 0..count {
            write_byte(b'A' + letter as u8);
        }
    }
    write_byte(b'\n');

    0
}
