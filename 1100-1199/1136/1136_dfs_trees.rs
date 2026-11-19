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

fn number() -> i64 {
    read_number().unwrap()
}

fn write_byte(byte: u8) {
    // SAFETY: putchar accepts a byte promoted to int and has no pointers.
    unsafe {
        putchar(i32::from(byte));
    }
}

fn write_number(value: i64) {
    const DIGITS: usize = 20;
    let mut remaining = value.unsigned_abs();
    if value < 0 {
        write_byte(b'-');
    }
    let mut buffer = [0u8; DIGITS];
    let mut start = buffer.len();
    loop {
        start -= 1;
        buffer[start] = b'0' + (remaining % 10) as u8;
        remaining /= 10;
        if remaining == 0 {
            break;
        }
    }
    for &digit in &buffer[start..] {
        write_byte(digit);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const NONE: u16 = u16::MAX;
    const VISITED: u16 = 1 << (u16::BITS - 1);
    let count = number() as usize;
    if count == 0 {
        return 0;
    }
    let mut values: Vec<u16> = (0..count).map(|_| number() as u16).collect();
    values.reverse();
    let (mut left, mut right) = (vec![NONE; count], vec![NONE; count]);
    let mut stack = Vec::with_capacity(count);
    stack.push(0u16);
    // Reversed postorder is root-right-left preorder: a monotone stack rebuilds it.
    for node in 1..count {
        let top = usize::from(*stack.last().unwrap());
        if values[node] >= values[top] {
            right[top] = node as u16;
        } else {
            let mut parent = usize::from(stack.pop().unwrap());
            while let Some(&old) = stack.last() {
                if values[node] >= values[usize::from(old)] {
                    break;
                }
                parent = usize::from(stack.pop().unwrap());
            }
            left[parent] = node as u16;
        }
        stack.push(node as u16);
    }
    stack.clear();
    stack.push(0);
    // Node indices use fewer than fifteen bits, leaving one bit for postorder state.
    while let Some(entry) = stack.pop() {
        let node = usize::from(entry & !VISITED);
        if entry & VISITED != 0 {
            write_number(i64::from(values[node]));
            write_byte(b'\n');
        } else {
            stack.push(entry | VISITED);
            if left[node] != NONE {
                stack.push(left[node]);
            }
            if right[node] != NONE {
                stack.push(right[node]);
            }
        }
    }

    0
}
