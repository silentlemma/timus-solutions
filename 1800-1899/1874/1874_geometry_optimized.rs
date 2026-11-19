#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn printf(format: *const i8, ...) -> i32;
    fn scanf(format: *const i8, ...) -> i32;
}

fn read_float() -> f64 {
    let mut value = 0.0f64;
    // SAFETY: the static %lf field receives a live pointer to an f64.
    let count = unsafe { scanf(b"%lf\0".as_ptr().cast(), &mut value as *mut f64) };
    assert_eq!(count, 1);
    value
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (a, b) = (read_float(), read_float());
    let (x, y) = (a / 2.0, b / 2.0);
    let area = x * x + y * y + 2.0 * 2f64.sqrt() * x * y;
    // SAFETY: the static format consumes one promoted double.
    unsafe {
        printf(b"%.9f\n\0".as_ptr().cast(), area);
    }
    0
}
