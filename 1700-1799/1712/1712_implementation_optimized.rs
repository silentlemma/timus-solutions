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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const SIDE: usize = 4;
    let mut grille = [[false; SIDE]; SIDE];
    let mut square = [[0u8; SIDE]; SIDE];
    for row in &mut grille {
        for cell in row {
            let mut byte = read_byte();
            while byte >= 0 && byte <= b' ' as i32 {
                byte = read_byte();
            }
            *cell = byte == b'X' as i32;
        }
    }
    for row in &mut square {
        for cell in row {
            let mut byte = read_byte();
            while byte >= 0 && byte <= b' ' as i32 {
                byte = read_byte();
            }
            *cell = byte as u8;
        }
    }
    for _ in 0..SIDE {
        for row in 0..SIDE {
            for column in 0..SIDE {
                if grille[row][column] {
                    write_byte(square[row][column]);
                }
            }
        }
        let mut turned = [[false; SIDE]; SIDE];
        for row in 0..SIDE {
            for column in 0..SIDE {
                turned[row][column] = grille[SIDE - 1 - column][row];
            }
        }
        grille = turned;
    }
    write_byte(b'\n');
    0
}
