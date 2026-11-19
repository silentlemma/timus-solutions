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

fn write_text(text: &[u8]) {
    for &byte in text {
        write_byte(byte);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const BASE: usize = 10;
    const LIMIT: usize = BASE * BASE - 1;
    // The digit turns are specified by the statement.
    const TURN: &[u8] = b"01????9?86";
    let count = number() as usize;
    let mut run = 0;
    for value in 1..=LIMIT {
        run = if TURN[value / BASE] != b'?' && TURN[value % BASE] != b'?' {
            run + 1
        } else {
            0
        };
        if run >= count {
            for offset in 0..count {
                if offset != 0 {
                    write_byte(b' ');
                }
                let target = value - offset;
                write_byte(TURN[target % BASE]);
                write_byte(TURN[target / BASE]);
            }
            write_byte(b'\n');
            return 0;
        }
    }
    write_text(b"Glupenky Pierre\n");

    0
}
