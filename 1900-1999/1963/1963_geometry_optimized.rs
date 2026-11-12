#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn byte() -> i32 {
    // SAFETY: getchar reads standard input and has no pointer arguments.
    unsafe { getchar() }
}

fn number() -> i64 {
    const SPACE: i32 = b' ' as i32;
    const ZERO: i32 = b'0' as i32;
    const NINE: i32 = b'9' as i32;
    let mut c = byte();
    while c >= 0 && c <= SPACE {
        c = byte();
    }
    let negative = c == b'-' as i32;
    if negative {
        c = byte();
    }
    let mut n = 0;
    while (ZERO..=NINE).contains(&c) {
        n = n * 10 + (c - ZERO) as u64;
        c = byte();
    }
    if negative {
        -(n as i64)
    } else {
        n as i64
    }
}

fn write_number(mut n: u64) {
    const MAX_DIGITS: usize = 20;
    let mut digits = [0_u8; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (n % 10) as u8;
        n /= 10;
        if n == 0 {
            break;
        }
    }
    for &digit in &digits[first..] {
        // SAFETY: putchar accepts the byte promoted to int, with no pointers.
        unsafe {
            putchar(digit as i32);
        }
    }
}

const VERTEX_COUNT: usize = 4;
type Point = (i64, i64);

fn boundary_count(points: &[Point; VERTEX_COUNT]) -> usize {
    let mut boundary = [(0, 0); 2 * VERTEX_COUNT];
    let mut count = 0;
    for shift in 0..VERTEX_COUNT {
        let (a, b);
        if shift % 2 == 0 {
            let first = shift / 2;
            let opposite = (first + 2) % VERTEX_COUNT;
            a = (2 * points[first].0, 2 * points[first].1);
            b = (2 * points[opposite].0, 2 * points[opposite].1);
        } else {
            a = (points[0].0 + points[shift].0, points[0].1 + points[shift].1);
            let first = if shift == 1 { 2 } else { 1 };
            b = (
                points[first].0 + points[first + 1].0,
                points[first].1 + points[first + 1].1,
            );
        }
        let (dx, dy) = (b.0 - a.0, b.1 - a.1);
        if dx == 0 && dy == 0 {
            continue;
        }
        let mut valid = true;
        for (i, &p) in points.iter().enumerate() {
            let q = points[(shift + VERTEX_COUNT - i) % VERTEX_COUNT];
            if (p.0 + q.0 - a.0) * dy != (p.1 + q.1 - a.1) * dx
                || (p.0 - q.0) * dx + (p.1 - q.1) * dy != 0
            {
                valid = false;
                break;
            }
        }
        if valid {
            for point in [a, b] {
                if !boundary[..count].contains(&point) {
                    boundary[count] = point;
                    count += 1;
                }
            }
        }
    }
    count
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut points = [(0, 0); VERTEX_COUNT];
    for point in &mut points {
        *point = (number(), number());
    }
    write_number(boundary_count(&points) as u64);
    // SAFETY: putchar accepts the newline byte promoted to int, without pointers.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
