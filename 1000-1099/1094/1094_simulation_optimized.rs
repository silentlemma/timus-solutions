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

const WIDTH: usize = 80;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut screen = [b' '; WIDTH];
    let mut cursor = 0_usize;
    loop {
        let key = byte();
        if key < 0 || key == b'\n' as i32 || key == b'\r' as i32 {
            break;
        }
        if key == b'<' as i32 {
            cursor = cursor.saturating_sub(1);
        } else {
            if key != b'>' as i32 {
                screen[cursor] = key as u8;
            }
            cursor += 1;
            if cursor == WIDTH {
                cursor = 0;
            }
        }
    }
    for cell in screen {
        // SAFETY: each stored ASCII byte is passed to putchar without pointers.
        unsafe {
            putchar(cell as i32);
        }
    }
    // SAFETY: the newline is a valid unsigned character promoted to int.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
