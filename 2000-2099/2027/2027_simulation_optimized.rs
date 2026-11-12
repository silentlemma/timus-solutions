#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(c: i32) -> i32;
}

const MAX_SIDE: usize = 102;
const ALPHABET: usize = 26;
const VALUE_LIMIT: i32 = 100000;
const TICK_LIMIT: usize = 1000000;
const DIRECTIONS: usize = 4;
const DIRECTION_MASK: usize = DIRECTIONS - 1;
const DECIMAL_BASE: i32 = 10;
const NUMBER_RESERVE: usize = 16;
const OP_OUTSIDE: u8 = 0;
const OP_RIGHT: u8 = 1;
const OP_DOWN: u8 = 2;
const OP_LEFT: u8 = 3;
const OP_UP: u8 = 4;
const OP_NOP: u8 = 5;
const OP_HALT: u8 = 6;
const OP_INPUT: u8 = 7;
const OP_OUTPUT: u8 = 8;
const OP_INCREMENT: u8 = 9;
const OP_DECREMENT: u8 = 10;
const OP_TURN: u8 = 11;
const OP_REGISTER: u8 = 12;

fn byte() -> i32 {
    // SAFETY: getchar reads stdin without pointer arguments.
    unsafe { getchar() }
}

fn character() -> i32 {
    let mut c = byte();
    while c >= 0 && c <= b' ' as i32 {
        c = byte();
    }
    c
}

fn number() -> i32 {
    let mut c = character();
    let negative = c == b'-' as i32;
    if c == b'-' as i32 || c == b'+' as i32 {
        c = byte();
    }
    let mut value = 0;
    while (b'0' as i32..=b'9' as i32).contains(&c) {
        value = value * DECIMAL_BASE + c - b'0' as i32;
        c = byte();
    }
    if negative {
        -value
    } else {
        value
    }
}

fn text(bytes: &[u8]) {
    for &c in bytes {
        // SAFETY: putchar takes a byte promoted to int, without pointers.
        unsafe {
            putchar(i32::from(c));
        }
    }
}

fn write_number(mut value: i32) {
    if value < 0 {
        text(b"-");
        value = -value;
    }
    let mut digits = [0_u8; NUMBER_RESERVE];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % DECIMAL_BASE) as u8;
        value /= DECIMAL_BASE;
        if value == 0 {
            break;
        }
    }
    text(&digits[first..]);
    text(b"\n");
}

fn instruction(c: u8) -> u8 {
    match c {
        b'>' => OP_RIGHT,
        b'v' => OP_DOWN,
        b'<' => OP_LEFT,
        b'^' => OP_UP,
        b'#' => OP_HALT,
        b'?' => OP_INPUT,
        b'!' => OP_OUTPUT,
        b'+' => OP_INCREMENT,
        b'-' => OP_DECREMENT,
        b'@' => OP_TURN,
        b'A'..=b'Z' => OP_REGISTER + c - b'A',
        _ => OP_NOP,
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (height, width) = (number() as usize, number() as usize);
    let stride = width + 2;
    let mut program = [OP_OUTSIDE; MAX_SIDE * MAX_SIDE];
    for row in 1..=height {
        for col in 1..=width {
            program[row * stride + col] = instruction(character() as u8);
        }
    }
    let mut remaining = number();
    let (mut last, mut current) = (0, 0);
    let mut memory = [0_i32; ALPHABET];
    let (mut position, mut direction) = ((stride + 1) as isize, 0);
    let moves: [isize; DIRECTIONS] = [1, stride as isize, -1, -(stride as isize)];
    for _ in 0..TICK_LIMIT {
        let op = program[position as usize];
        if op == OP_HALT {
            return 0;
        }
        if op <= OP_UP {
            direction = usize::from(op - OP_RIGHT);
        } else if op >= OP_REGISTER {
            std::mem::swap(&mut current, &mut memory[usize::from(op - OP_REGISTER)]);
        } else {
            match op {
                OP_INPUT => {
                    if remaining > 0 {
                        last = number();
                        remaining -= 1;
                    }
                    current = last;
                }
                OP_OUTPUT => {
                    write_number(current);
                    current = 0;
                }
                OP_INCREMENT => current += 1,
                OP_DECREMENT => current -= 1,
                OP_TURN => {
                    direction =
                        (direction + if current == 0 { DIRECTION_MASK } else { 1 }) & DIRECTION_MASK
                }
                _ => {}
            }
        }
        if current < -VALUE_LIMIT || current > VALUE_LIMIT {
            text(b"OVERFLOW ERROR\n");
            return 0;
        }
        position += moves[direction];
        if program[position as usize] == OP_OUTSIDE {
            text(b"RUNTIME ERROR\n");
            return 0;
        }
    }
    text(b"TIME LIMIT EXCEEDED\n");
    0
}
