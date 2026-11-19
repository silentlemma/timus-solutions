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
    let count = number() as usize;
    let (mut parent_head, mut child_head) = (vec![-1i32; count + 1], vec![-1i32; count + 1]);
    let (mut parent_to, mut child_to) = (Vec::<u16>::new(), Vec::<u16>::new());
    let (mut parent_next, mut child_next) = (Vec::new(), Vec::new());
    loop {
        let token = word();
        if token == b"BLOOD" || token.is_empty() {
            break;
        }
        let child: usize = std::str::from_utf8(&token).unwrap().parse().unwrap();
        let parent = number() as usize;
        let edge = parent_to.len() as i32;
        parent_to.push(parent as u16);
        parent_next.push(parent_head[child]);
        parent_head[child] = edge;
        child_to.push(child as u16);
        child_next.push(child_head[parent]);
        child_head[parent] = edge;
    }
    let mut victims = Vec::new();
    let mut cleared = vec![false; count + 1];
    while let Some(value) = read_number() {
        victims.push(value as u16);
        cleared[value as usize] = true;
    }
    let mut seen = vec![false; count + 1];
    let mut stack = Vec::new();
    for direction in 0..2 {
        seen.fill(false);
        stack.clear();
        for &victim in &victims {
            seen[usize::from(victim)] = true;
            stack.push(victim);
        }
        let (head, next, to) = if direction == 0 {
            (&parent_head, &parent_next, &parent_to)
        } else {
            (&child_head, &child_next, &child_to)
        };
        // Each direction has its own visited set, independent of the cleared union.
        while let Some(vertex) = stack.pop() {
            let mut edge = head[usize::from(vertex)];
            while edge >= 0 {
                let other = usize::from(to[edge as usize]);
                if !seen[other] {
                    seen[other] = true;
                    cleared[other] = true;
                    stack.push(other as u16);
                }
                edge = next[edge as usize];
            }
        }
    }
    let mut first = true;
    for vertex in 1..=count {
        if !cleared[vertex] {
            if !first {
                write_byte(b' ');
            }
            first = false;
            write_number(vertex as i64);
        }
    }
    if first {
        write_byte(b'0');
    }
    write_byte(b'\n');

    0
}
