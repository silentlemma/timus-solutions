#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

const ASCII_SPACE: i32 = b' ' as i32;
const ASCII_ZERO: i32 = b'0' as i32;
const ASCII_NINE: i32 = b'9' as i32;
const FIRST_ODD_DIVISOR: u64 = 3;
const MAX_SQUARE_ROOT: u64 = 1000000000;
const MAX_DIGITS: usize = 20;

fn byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads the process's standard input.
    unsafe { getchar() }
}

fn number() -> u64 {
    let mut c = byte();
    while c >= 0 && c <= ASCII_SPACE {
        c = byte();
    }
    let mut value = 0;
    while (ASCII_ZERO..=ASCII_NINE).contains(&c) {
        value = value * 10 + (c - ASCII_ZERO) as u64;
        c = byte();
    }
    value
}

fn square_root(value: u64) -> u64 {
    let (mut low, mut high) = (0, MAX_SQUARE_ROOT + 1);
    while high - low > 1 {
        let middle = (low + high) / 2;
        if middle * middle <= value {
            low = middle;
        } else {
            high = middle;
        }
    }
    low
}

fn square_part(mut value: u64) -> u64 {
    let mut root = square_root(value);
    if root * root == value {
        return value;
    }
    let mut answer = 1;
    let mut divisor = FIRST_ODD_DIVISOR;
    while divisor * divisor * divisor <= value {
        let mut power = 0;
        while value % divisor == 0 {
            value /= divisor;
            power += 1;
        }
        for _ in 0..power / 2 {
            answer *= divisor * divisor;
        }
        if power > 0 {
            root = square_root(value);
            // A square residual is itself its largest square divisor.
            if root * root == value {
                return answer * value;
            }
        }
        divisor += 2;
    }
    root = square_root(value);
    if root * root == value {
        answer *= value;
    }
    answer
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut answer = square_part(number());
    let mut output = [0_u8; MAX_DIGITS];
    let mut first = output.len() - 1;
    output[first] = b'\n';
    loop {
        first -= 1;
        output[first] = (answer % 10) as u8 + b'0';
        answer /= 10;
        if answer == 0 {
            break;
        }
    }
    for &character in &output[first..] {
        // SAFETY: each character is an unsigned byte promoted to an int for putchar.
        unsafe { putchar(character as i32) };
    }
    0
}
