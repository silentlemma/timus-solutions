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

fn word() -> Vec<u8> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    let mut result = Vec::new();
    while byte > b' ' as i32 {
        result.push(byte as u8);
        byte = read_byte();
    }
    result
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

const WRAP: u8 = u8::MAX;
fn pair(a: u8, b: u8) -> bool {
    (a == b'(' && b == b')') || (a == b'[' && b == b']')
}
fn build(text: &[u8], how: &[u8], stride: usize, left: usize, right: usize) {
    if left == right {
        return;
    }
    let way = how[left * stride + right];
    if way == 0 {
        write_text(if text[left] == b'(' || text[left] == b')' {
            b"()"
        } else {
            b"[]"
        });
    } else if way == WRAP {
        write_byte(text[left]);
        build(text, how, stride, left + 1, right - 1);
        write_byte(text[right - 1]);
    } else {
        build(text, how, stride, left, usize::from(way));
        build(text, how, stride, usize::from(way), right);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let text = word();
    let count = text.len();
    let stride = count + 1;
    // At most one insertion per input bracket fits in a byte, as do split indices.
    let (mut cost, mut how) = (vec![0u8; stride * stride], vec![0u8; stride * stride]);
    for length in 1..=count {
        for left in 0..=count - length {
            let right = left + length;
            if length == 1 {
                cost[left * stride + right] = 1;
                continue;
            }
            let (mut best, mut way) = (
                cost[left * stride + left + 1] + cost[(left + 1) * stride + right],
                (left + 1) as u8,
            );
            if pair(text[left], text[right - 1]) && cost[(left + 1) * stride + right - 1] < best {
                best = cost[(left + 1) * stride + right - 1];
                way = WRAP;
            }
            for split in left + 2..right {
                let candidate = cost[left * stride + split] + cost[split * stride + right];
                if candidate < best {
                    best = candidate;
                    way = split as u8;
                }
            }
            cost[left * stride + right] = best;
            how[left * stride + right] = way;
        }
    }
    build(&text, &how, stride, 0, count);
    write_byte(b'\n');

    0
}
