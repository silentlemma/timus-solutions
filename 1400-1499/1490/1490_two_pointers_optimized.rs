#![no_main]

use std::os::raw::c_int;

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn scanf(format: *const u8, ...) -> c_int;
    fn printf(format: *const u8, ...) -> c_int;
}

// The C ABI entry avoids unused Rust stdio/startup; all IO buffers are bounded.
#[no_mangle]
pub extern "C" fn main() -> c_int {
    let mut r = 0_i64;
    // SAFETY: %lld receives a live writable i64 pointer and the format is NUL-terminated.
    if unsafe { scanf(b"%lld\0".as_ptr(), &mut r) } != 1 {
        return 1;
    }
    const QUARTERS: i64 = 4;
    let (mut y, mut total) = (r, 0_i64);
    let (mut x_squared, mut y_squared) = (0, (r - 1) * (r - 1));
    let radius_squared = r * r;
    // The monotone boundary decreases at most r times; equality is outside.
    for x in 0..r {
        while y > 0 && x_squared + y_squared >= radius_squared {
            y -= 1;
            y_squared -= 2 * y - 1;
        }
        total += y;
        x_squared += 2 * x + 1;
    }
    // SAFETY: the NUL-terminated %lld conversion receives the matching i64 argument.
    unsafe {
        printf(b"%lld\n\0".as_ptr(), QUARTERS * total);
    }
    0
}
