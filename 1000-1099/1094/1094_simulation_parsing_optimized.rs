#![no_main]

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn system_read(fd: i32, buffer: *mut u8, length: u32) -> i32;
    #[link_name = "_write"]
    fn system_write(fd: i32, buffer: *const u8, length: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn system_read(fd: i32, buffer: *mut u8, length: usize) -> isize;
    #[link_name = "write"]
    fn system_write(fd: i32, buffer: *const u8, length: usize) -> isize;
}

fn read_input(buffer: &mut [u8]) -> usize {
    // SAFETY: the writable slice stays live for the call, and its length is bounded by INPUT_SIZE.
    // Both CRT _read and POSIX read write no more than the supplied length.
    let count = unsafe {
        #[cfg(windows)]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len() as u32)
        }
        #[cfg(not(windows))]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len())
        }
    };
    if count > 0 {
        count as usize
    } else {
        0
    }
}

fn write_all(mut buffer: &[u8]) -> bool {
    while !buffer.is_empty() {
        // SAFETY: this live slice contains at most OUTPUT_SIZE readable bytes.
        // Both write functions access at most the specified length and return a byte count.
        let count = unsafe {
            #[cfg(windows)]
            {
                system_write(1, buffer.as_ptr(), buffer.len() as u32)
            }
            #[cfg(not(windows))]
            {
                system_write(1, buffer.as_ptr(), buffer.len())
            }
        };
        if count <= 0 {
            return false;
        }
        buffer = &buffer[count as usize..];
    }
    true
}

const INPUT_SIZE: usize = 256;

const OUTPUT_SIZE: usize = WIDTH + 1;
const WIDTH: usize = 80;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut screen = [b' '; WIDTH];
    let mut cursor = 0_usize;
    let mut input = [0; INPUT_SIZE];
    'input: loop {
        let length = read_input(&mut input);
        if length == 0 {
            break;
        }
        for &key in &input[..length] {
            if key == b'\n' || key == b'\r' {
                break 'input;
            }
            if key == b'<' {
                cursor = cursor.saturating_sub(1);
            } else {
                if key != b'>' {
                    screen[cursor] = key;
                }
                cursor += 1;
                if cursor == WIDTH {
                    cursor = 0;
                }
            }
        }
    }
    let mut output = [0; OUTPUT_SIZE];
    output[..WIDTH].copy_from_slice(&screen);
    output[WIDTH] = b'\n';
    if write_all(&output) {
        0
    } else {
        1
    }
}

// Original per-character I/O contract, retained when replacing it with bounded reads/writes:

// SAFETY: getchar reads standard input and has no pointer arguments.
// SAFETY: each stored ASCII byte is passed to putchar without pointers.
// SAFETY: the newline is a valid unsigned character promoted to int.
