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

use std::f64::consts::PI;
const GRAVITY: f64 = 9.81;
const CENTIMETRES: f64 = 100.0;
const SECONDS: f64 = 60.0;
const STEPS: usize = 60;
const TURN: usize = 4;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (length, height, turns) = (number() as f64, number() as f64, number() as f64);
    // Sixty bisections saturate float precision on positive odd-quarter intervals.
    let half = length / CENTIMETRES / 2.0;
    let top = height / CENTIMETRES;
    let omega = turns * 2.0 * PI / SECONDS;
    let quarter = PI / 2.0 / omega;
    // the height of the lowest end of the toast at time t
    let gap = |t: f64| top - GRAVITY * t * t / 2.0 - half * (omega * t).sin().abs();
    // d gap / dt in quarter k, where the angle within the half turn is
    // omega*t - (k / 2)*pi
    let slope =
        |t: f64, k: usize| -GRAVITY * t - half * omega * (omega * t - (k / 2) as f64 * PI).cos();
    // d slope / dt, falling through an odd quarter
    let bend = |t: f64, k: usize| {
        -GRAVITY + half * omega * omega * (omega * t - (k / 2) as f64 * PI).sin()
    };
    let mut k = 0;
    loop {
        let (a, b) = (k as f64 * quarter, (k + 1) as f64 * quarter);
        let mut lowest = gap(b);
        if k % 2 == 1 {
            // the end rises again here: the slope of the gap is concave, so
            // find its peak; where it turns positive, the gap has a minimum
            let (mut lo, mut hi) = (a, b);
            for _ in 0..STEPS {
                let mid = (lo + hi) / 2.0;
                if bend(mid, k) > 0.0 {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }
            if slope(lo, k) > 0.0 {
                hi = lo;
                lo = a;
                for _ in 0..STEPS {
                    let mid = (lo + hi) / 2.0;
                    if slope(mid, k) < 0.0 {
                        lo = mid;
                    } else {
                        hi = mid;
                    }
                }
                lowest = lowest.min(gap(lo));
            }
        }
        if lowest <= 0.0 {
            break;
        }
        k += 1;
    }
    let in_turn = k % TURN;
    write_text(if in_turn == 0 || in_turn == TURN - 1 {
        b"butter\n"
    } else {
        b"bread\n"
    });

    0
}
