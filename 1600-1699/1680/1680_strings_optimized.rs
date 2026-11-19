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

fn write_text(text: &[u8]) {
    for &byte in text {
        write_byte(byte);
    }
}

fn line() -> Vec<u8> {
    let mut result = Vec::new();
    loop {
        let byte = read_byte();
        if byte < 0 || byte == b'\n' as i32 {
            break;
        }
        if byte != b'\r' as i32 {
            result.push(byte as u8);
        }
    }
    result
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (_year, count, quota) = (number(), number(), number() as usize);
    let mut taken: Vec<Vec<u8>> = Vec::with_capacity(quota);
    for _ in 0..count {
        let team = loop {
            let next = line();
            if !next.is_empty() {
                break next;
            }
        };
        let end = team
            .iter()
            .rposition(|&byte| byte == b'#')
            .unwrap_or(team.len());
        let mut university = team[..end].to_vec();
        while university.last().is_some_and(u8::is_ascii_whitespace) {
            university.pop();
        }
        university.make_ascii_lowercase();
        if taken.contains(&university) {
            continue;
        }
        if taken.len() == quota {
            write_text(&team);
            write_byte(b'\n');
            return 0;
        }
        taken.push(university);
    }

    0
}
