#![no_main]
#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn scanf(format: *const std::ffi::c_char, ...) -> i32;
    fn printf(format: *const std::ffi::c_char, ...) -> i32;
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const FIELDS: i32 = 7;
    let (mut ax, mut ay, mut bx, mut by, mut cx, mut cy, mut rope) =
        (0.0f64, 0.0f64, 0.0f64, 0.0f64, 0.0f64, 0.0f64, 0.0f64);
    // SAFETY: the static format supplies exactly seven live f64 pointers.
    let read = unsafe {
        scanf(
            b"%lf%lf%lf%lf%lf%lf%lf\0".as_ptr().cast(),
            &mut ax as *mut f64,
            &mut ay as *mut f64,
            &mut bx as *mut f64,
            &mut by as *mut f64,
            &mut cx as *mut f64,
            &mut cy as *mut f64,
            &mut rope as *mut f64,
        )
    };
    if read != FIELDS {
        return 1;
    }
    let (dx, dy) = (bx - ax, by - ay);
    let length = dx * dx + dy * dy;
    let t = if length == 0.0 {
        0.0
    } else {
        (((cx - ax) * dx + (cy - ay) * dy) / length).clamp(0.0, 1.0)
    };
    let nearest = (ax + t * dx - cx).hypot(ay + t * dy - cy);
    let farthest = (ax - cx).hypot(ay - cy).max((bx - cx).hypot(by - cy));
    // SAFETY: the static format consumes the two promoted double values.
    unsafe {
        printf(
            b"%.2f\n%.2f\n\0".as_ptr().cast(),
            (nearest - rope).max(0.0),
            (farthest - rope).max(0.0),
        );
    }
    0
}
