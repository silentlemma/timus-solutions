#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn printf(format: *const i8, ...) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments.
    unsafe { getchar() }
}

fn number() -> i64 {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
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
    value
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number();
    let radius = if count == 1 {
        1.0
    } else {
        1.0 + 1.0 / (std::f64::consts::PI / count as f64).sin()
    };
    // SAFETY: the static format consumes one promoted double.
    unsafe {
        printf(b"%.10f\n\0".as_ptr().cast(), radius);
    }
    0
}
