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

fn number() -> u64 {
    const SPACE: i32 = b' ' as i32;
    const ZERO: i32 = b'0' as i32;
    const NINE: i32 = b'9' as i32;
    let mut c = byte();
    while c >= 0 && c <= SPACE {
        c = byte();
    }
    let mut n = 0;
    while (ZERO..=NINE).contains(&c) {
        n = n * 10 + (c - ZERO) as u64;
        c = byte();
    }
    n
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

const MAX_SIZE: usize = 100;
const CAP: u16 = 100;

fn text(bytes: &[u8]) {
    for &c in bytes {
        // SAFETY: putchar takes a byte promoted to int and no pointers.
        unsafe {
            putchar(i32::from(c));
        }
    }
}

fn taken(columns: &[u16], level: u16) -> u32 {
    columns
        .iter()
        .map(|&value| u32::from(value.saturating_sub(level).min(CAP)))
        .sum()
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let n = number() as usize;
    let mut rows = [0_u16; MAX_SIZE];
    let mut columns = [0_u16; MAX_SIZE];
    for value in &mut rows[..n] {
        *value = number() as u16;
    }
    for value in &mut columns[..n] {
        *value = number() as u16;
    }
    let maximum = usize::from(CAP) * n;
    if rows[..n]
        .iter()
        .chain(&columns[..n])
        .any(|&value| usize::from(value) > maximum)
    {
        text(b"NO\n");
        return 0;
    }
    let mut matrix = [0_u8; MAX_SIZE * MAX_SIZE];
    for (row, &need) in rows[..n].iter().enumerate() {
        if need == 0 {
            continue;
        }
        if taken(&columns[..n], 0) < u32::from(need) {
            text(b"NO\n");
            return 0;
        }
        let (mut low, mut high) = (0, *columns[..n].iter().max().unwrap());
        while low < high {
            let middle = low + (high - low) / 2;
            if taken(&columns[..n], middle) <= u32::from(need) {
                high = middle;
            } else {
                low = middle + 1;
            }
        }
        let mut extra = u32::from(need) - taken(&columns[..n], low);
        for (col, value) in columns[..n].iter_mut().enumerate() {
            let mut give = value.saturating_sub(low).min(CAP);
            if extra != 0 && give < CAP && *value - give == low && low != 0 {
                give += 1;
                extra -= 1;
            }
            *value -= give;
            matrix[row * n + col] = give as u8;
        }
    }
    if columns[..n].iter().any(|&value| value != 0) {
        text(b"NO\n");
        return 0;
    }
    text(b"YES\n");
    for row in 0..n {
        for col in 0..n {
            if col != 0 {
                text(b" ");
            }
            write_number(u64::from(matrix[row * n + col]));
        }
        text(b"\n");
    }
    0
}
