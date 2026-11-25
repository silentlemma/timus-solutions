#![no_main]
fn solve_entry() {
    let mut input = NativeNumbers::new();
    let (a, b, c) = (
        input.next().unwrap() as u32,
        input.next().unwrap() as u32,
        input.next().unwrap() as u32,
    );
    // 2^(C-1) + 2^(C-1) = 2^C, and A and B both divide C - 1
    // SAFETY: both shifts fit u64, whose representation matches C unsigned long long.
    unsafe {
        printf(
            b"%llu\n%llu\n2\n\0".as_ptr(),
            1_u64 << ((c - 1) / a),
            1_u64 << ((c - 1) / b),
        );
    }
}

// MSVC import libraries expose newer CRT shims; bind the legacy DLL exports directly.
#[cfg_attr(
    all(windows, target_env = "msvc"),
    link(name = "msvcrt", kind = "raw-dylib")
)]
#[cfg_attr(all(windows, not(target_env = "msvc")), link(name = "msvcrt"))]
extern "C" {
    fn scanf(format: *const u8, ...) -> i32;
    fn printf(format: *const u8, ...) -> i32;
    fn fflush(stream: *mut core::ffi::c_void) -> i32;
    fn _exit(status: i32) -> !;
}

struct NativeNumbers;
impl NativeNumbers {
    fn new() -> Self {
        Self
    }
}
impl Iterator for NativeNumbers {
    type Item = i64;
    fn next(&mut self) -> Option<i64> {
        // Input bounds guarantee that each decimal token fits its destination integer.
        let mut value = 0_i64;
        // SAFETY: %lld writes one live i64, and scanf consumes ordinary whitespace.
        let count = unsafe { scanf(b"%lld\0".as_ptr(), &mut value) };
        if count == 1 {
            Some(value)
        } else {
            None
        }
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    solve_entry();
    // SAFETY: flush all C output before terminating the standalone process.
    unsafe {
        fflush(core::ptr::null_mut());
        _exit(0)
    }
}
