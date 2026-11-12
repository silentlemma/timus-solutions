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

const MAX_TEAMS: usize = 100;
const NAME_CAPACITY: usize = 11;
const ALPHABET: usize = 26;
const SHORT_NAMES: usize = ALPHABET + ALPHABET * ALPHABET;
type Name = [u8; NAME_CAPACITY];

fn read_name() -> Name {
    let mut name = [0; NAME_CAPACITY];
    let mut c = byte();
    while c >= 0 && c <= b' ' as i32 {
        c = byte();
    }
    let mut i = 0;
    while c > b' ' as i32 {
        name[i] = c as u8;
        i += 1;
        c = byte();
    }
    name
}

fn write_byte(c: u8) {
    // SAFETY: putchar accepts an unsigned character promoted to int, without pointers.
    unsafe {
        putchar(c as i32);
    }
}

fn write_name(name: &Name) {
    for &c in name {
        if c == 0 {
            break;
        }
        write_byte(c);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let n = number() as usize;
    let mut names = [[0; NAME_CAPACITY]; MAX_TEAMS];
    for name in &mut names[..n] {
        *name = read_name();
    }
    names[..n].sort_unstable();
    let duplicate = names[..n].windows(2).any(|pair| pair[0] == pair[1]);
    if duplicate || n == 1 {
        let text: &[u8] = if duplicate && n > 2 {
            b"Impossible\n"
        } else {
            b"0\n"
        };
        for &c in text {
            write_byte(c);
        }
        return 0;
    }
    if n == 2 {
        write_byte(b'1');
        write_byte(b'\n');
        write_name(&names[0]);
        write_byte(b'-');
        write_name(&names[1]);
        write_byte(b'\n');
        return 0;
    }
    let mut occupied = [false; SHORT_NAMES];
    for name in &names[..n] {
        if name[1] == 0 {
            occupied[(name[0] - b'a') as usize] = true;
        } else if name[2] == 0 {
            occupied[ALPHABET + (name[0] - b'a') as usize * ALPHABET + (name[1] - b'a') as usize] =
                true;
        }
    }
    let mut id = occupied.iter().position(|&used| !used).unwrap();
    let mut hub = [0; NAME_CAPACITY];
    if id < ALPHABET {
        hub[0] = b'a' + id as u8;
    } else {
        id -= ALPHABET;
        hub[0] = b'a' + (id / ALPHABET) as u8;
        hub[1] = b'a' + (id % ALPHABET) as u8;
    }
    write_number(n as u64);
    write_byte(b'\n');
    for name in &names[..n] {
        write_name(name);
        write_byte(b'-');
        write_name(&hub);
        write_byte(b'\n');
    }
    0
}
