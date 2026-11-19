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
    let (count, readings) = (number() as usize, number());
    let mut frequencies = vec![0u8; count + 1];
    for _ in 0..readings {
        let value = number() as usize;
        frequencies[value] += 1;
        if frequencies[value] > 2 {
            write_text(b"NO\n");
            return 0;
        }
    }
    let mut used_before = false;
    for (value, &frequency) in frequencies.iter().enumerate() {
        let mut need = frequency;
        if value > 0 && !used_before && need > 0 {
            need -= 1;
        }
        let take_next = value < count && need > 0;
        if take_next {
            need -= 1;
        }
        if need != 0 {
            write_text(b"NO\n");
            return 0;
        }
        used_before = take_next;
    }
    write_text(b"YES\n");

    0
}
