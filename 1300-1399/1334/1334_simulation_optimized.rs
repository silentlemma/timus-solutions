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

const BOARD_SIZE: usize = 8;
const PADDING: usize = 2;
const SIDE: usize = BOARD_SIZE + 2 * PADDING;
const WALL: u8 = 255;
const WHITE: u8 = 1;
const BLACK: u8 = 2;
const MOVE_LIMIT: usize = 32;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut board = [WALL; SIDE * SIDE];
    for x in 0..BOARD_SIZE {
        for y in 0..BOARD_SIZE {
            board[(x + PADDING) * SIDE + y + PADDING] = 0;
        }
    }
    let side = SIDE as isize;
    let directions = [side + 1, side - 1, -side + 1, -side - 1];
    let mut color = WHITE;
    for number in 1..=MOVE_LIMIT {
        let mut file = byte();
        while file >= 0 && file <= b' ' as i32 {
            file = byte();
        }
        if file < 0 {
            break;
        }
        let rank = byte() as u8;
        let file = (file as u8).to_ascii_lowercase();
        let cell = ((usize::from(file - b'a') + PADDING) * SIDE
            + usize::from(rank - b'1')
            + PADDING) as isize;
        board[cell as usize] = color;
        let opposite = WHITE + BLACK - color;
        for direction in directions {
            if board[(cell + direction) as usize] == opposite
                && (board[(cell + 2 * direction) as usize] == 0
                    || board[(cell - direction) as usize] == 0)
            {
                write_number(number as u64);
                // SAFETY: putchar takes a newline byte promoted to int, without pointers.
                unsafe {
                    putchar(b'\n' as i32);
                }
                return 0;
            }
        }
        color = opposite;
    }
    for &c in b"Draw\n" {
        // SAFETY: putchar takes a byte promoted to int, without pointers.
        unsafe {
            putchar(i32::from(c));
        }
    }
    0
}
