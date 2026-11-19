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

const FACES: usize = 4;

fn word() -> [u8; FACES] {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    let mut result = [0; FACES];
    for letter in &mut result {
        *letter = byte as u8;
        byte = read_byte();
    }
    result
}

fn equivalent(a: [u8; FACES], b: [u8; FACES]) -> bool {
    let (mut first, mut second) = (a, b);
    first.sort_unstable();
    second.sort_unstable();
    if first != second {
        return false;
    }
    // Equal colours allow swapping two faces to correct the permutation parity.
    if first.windows(2).any(|pair| pair[0] == pair[1]) {
        return true;
    }
    let mut positions = [0; FACES];
    for i in 0..FACES {
        positions[i] = a.iter().position(|&colour| colour == b[i]).unwrap();
    }
    let mut odd = false;
    for i in 0..FACES {
        for j in i + 1..FACES {
            odd ^= positions[i] > positions[j];
        }
    }
    // Tetrahedral rotations are precisely the even permutations of four faces.
    !odd
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (first, second) = (word(), word());
    write_text(if equivalent(first, second) {
        b"equal\n"
    } else {
        b"different\n"
    });

    0
}
