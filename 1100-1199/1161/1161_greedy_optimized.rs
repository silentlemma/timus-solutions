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
    let count = number() as usize;
    let mut weights = Vec::with_capacity(count);
    for _ in 0..count {
        weights.push(number() as u32);
    }
    weights.sort_unstable_by(|a, b| b.cmp(a));
    let mut total = f64::from(weights[0]);
    for &weight in &weights[1..] {
        total = 2.0 * (total * f64::from(weight)).sqrt();
    }
    // SAFETY: the static format consumes one promoted double.
    unsafe {
        printf(b"%.2f\n\0".as_ptr().cast(), total);
    }
    0
}
