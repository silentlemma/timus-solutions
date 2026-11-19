#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn printf(format: *const std::ffi::c_char, ...) -> i32;
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

fn word() -> Vec<u8> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    let mut result = Vec::new();
    while byte > b' ' as i32 {
        result.push(byte as u8);
        byte = read_byte();
    }
    result
}
const MIDPOINT: f64 = 0.5;
const PERCENT: f64 = 100.0;
const STRIPS: usize = 20000;
const BOMBS: usize = 10;
#[derive(Clone, Copy, Default)]
struct Bomb {
    x: f64,
    y: f64,
    squared: f64,
}
fn real() -> f64 {
    let token = word();
    std::str::from_utf8(&token).unwrap().parse().unwrap()
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number() as usize;
    let mut bombs = [Bomb::default(); BOMBS];
    for bomb in bombs.iter_mut().take(count) {
        bomb.x = real();
        bomb.y = real();
        let radius = real();
        bomb.squared = radius * radius;
    }
    let mut covered = 0.0;
    for strip in 0..STRIPS {
        let x = (strip as f64 + MIDPOINT) / STRIPS as f64;
        let mut intervals = [(0.0, 0.0); BOMBS];
        let mut size = 0;
        for bomb in bombs.iter().take(count) {
            let squared = bomb.squared - (x - bomb.x) * (x - bomb.x);
            if squared > 0.0 {
                let half = squared.sqrt();
                let interval = ((bomb.y - half).max(0.0), (bomb.y + half).min(1.0));
                if interval.0 < interval.1 {
                    let mut at = size;
                    while at > 0 && intervals[at - 1].0 > interval.0 {
                        intervals[at] = intervals[at - 1];
                        at -= 1;
                    }
                    intervals[at] = interval;
                    size += 1;
                }
            }
        }
        let mut end = 0.0f64;
        for &(low, high) in intervals.iter().take(size) {
            if high > end {
                covered += high - low.max(end);
                end = high;
            }
        }
    }
    // SAFETY: the static format expects the promoted double supplied here.
    unsafe {
        printf(
            b"%.6f\n\0".as_ptr().cast(),
            covered / STRIPS as f64 * PERCENT,
        );
    }

    0
}
