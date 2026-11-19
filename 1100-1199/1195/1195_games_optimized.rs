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

const CELLS: usize = 9;
const LINES: [u16; 8] = [7, 56, 448, 73, 146, 292, 273, 84];
fn play(own: u16, other: u16) -> i8 {
    let mut available = !(own | other) & ((1 << CELLS) - 1);
    if available == 0 {
        return 0;
    }
    let mut best = -1;
    while available != 0 {
        let bit = available & available.wrapping_neg();
        available ^= bit;
        let next = own | bit;
        if LINES.iter().any(|&line| next & line == line) {
            return 1;
        }
        best = best.max(-play(other, next));
        if best == 1 {
            return 1;
        }
    }
    best
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (mut crosses, mut ouths) = (0u16, 0u16);
    for cell in 0..CELLS {
        let mut byte = read_byte();
        while byte <= b' ' as i32 {
            byte = read_byte();
        }
        if byte == b'X' as i32 {
            crosses |= 1 << cell;
        }
        if byte == b'O' as i32 {
            ouths |= 1 << cell;
        }
    }
    write_text(match play(crosses, ouths) {
        1 => b"Crosses win\n",
        0 => b"Draw\n",
        _ => b"Ouths win\n",
    });

    0
}
