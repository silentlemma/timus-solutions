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

fn read_number() -> Option<i64> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    if byte < 0 {
        return None;
    }
    let negative = byte == b'-' as i32;
    if negative || byte == b'+' as i32 {
        byte = read_byte();
    }
    let mut value = 0i64;
    while (b'0' as i32..=b'9' as i32).contains(&byte) {
        let digit = i64::from(byte - b'0' as i32);
        // Accumulating negatives directly also accepts i64::MIN.
        value = if negative {
            value * 10 - digit
        } else {
            value * 10 + digit
        };
        byte = read_byte();
    }
    Some(value)
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

const VERTICES: usize = 1000;

fn find(parent: &mut [u16], mut vertex: usize) -> usize {
    while usize::from(parent[vertex]) != vertex {
        parent[vertex] = parent[usize::from(parent[vertex])];
        vertex = usize::from(parent[vertex]);
    }
    vertex
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut parent = [0u16; VERTICES + 1];
    let mut odd = [0u8; VERTICES + 1];
    for (vertex, slot) in parent.iter_mut().enumerate() {
        *slot = vertex as u16;
    }
    while let Some(first) = read_number() {
        let Some(second) = read_number() else {
            break;
        };
        let a = find(&mut parent, first as usize);
        let b = find(&mut parent, second as usize);
        if a != b {
            parent[a] = b as u16;
            odd[b] ^= odd[a];
        }
        odd[b] ^= 1;
    }
    // Only the parity of each component's edge count is required.
    let even = (1..=VERTICES).all(|v| usize::from(parent[v]) != v || odd[v] == 0);
    write_text(if even { b"1\n" } else { b"0\n" });

    0
}
