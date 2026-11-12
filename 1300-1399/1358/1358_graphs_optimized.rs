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

const MAX_VERTICES: usize = 1000;
const STEP: i32 = 2;
const LIMIT: i32 = 999;

fn emit(c: u8) {
    // SAFETY: putchar takes a byte promoted to int and no pointers.
    unsafe {
        putchar(i32::from(c));
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let n = number() as usize;
    let mut head = [0_u16; MAX_VERTICES + 1];
    let mut to = [0_u16; 2 * MAX_VERTICES];
    let mut next = [0_u16; 2 * MAX_VERTICES];
    for index in 1..n {
        let (a, b) = (number() as usize, number() as usize);
        let edge = 2 * index - 1;
        to[edge] = b as u16;
        next[edge] = head[a];
        head[a] = edge as u16;
        to[edge + 1] = a as u16;
        next[edge + 1] = head[b];
        head[b] = (edge + 1) as u16;
    }
    let mut depth = [0_u16; MAX_VERTICES + 1];
    let mut position = [0_u16; MAX_VERTICES + 1];
    let mut stack = [0_u16; MAX_VERTICES];
    stack[0] = 1;
    depth[1] = 1;
    let (mut length, mut order) = (1, 0);
    while length != 0 {
        length -= 1;
        let v = stack[length] as usize;
        position[v] = order;
        order += 1;
        let mut edge = head[v] as usize;
        while edge != 0 {
            let w = to[edge] as usize;
            if depth[w] == 0 {
                depth[w] = depth[v] + 1;
                stack[length] = w as u16;
                length += 1;
            }
            edge = next[edge] as usize;
        }
    }
    for v in 1..=n {
        let mut x = i32::from(position[v]) * STEP - LIMIT;
        if x < 0 {
            emit(b'-');
            x = -x;
        }
        write_number(x as u64);
        emit(b' ');
        write_number(u64::from(depth[v] - 1));
        emit(b'\n');
    }
    0
}
