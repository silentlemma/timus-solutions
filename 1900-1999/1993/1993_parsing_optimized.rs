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

fn write_byte(byte: u8) {
    // SAFETY: putchar accepts a byte promoted to int and has no pointers.
    unsafe {
        putchar(i32::from(byte));
    }
}

const ROLES: usize = 3;
fn emit(bytes: &[u8], first: &mut bool) {
    for &byte in bytes {
        write_byte(if *first {
            *first = false;
            byte.to_ascii_uppercase()
        } else {
            byte
        });
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const OPENING: &[u8] = b"{([";
    const CLOSING: &[u8] = b"})]";
    let mut data = Vec::new();
    loop {
        let byte = read_byte();
        if byte < 0 {
            break;
        }
        data.push((byte as u8).to_ascii_lowercase());
    }
    let begin = data
        .iter()
        .position(|byte| !byte.is_ascii_whitespace())
        .unwrap_or(data.len());
    let end = data
        .iter()
        .rposition(|byte| !byte.is_ascii_whitespace())
        .map_or(begin, |i| i + 1);
    let mut first = true;
    for (clause_index, clause) in data[begin..end].split(|&byte| byte == b',').enumerate() {
        if clause_index != 0 {
            emit(b", ", &mut first);
        }
        let mut roles = [(0usize, 0usize); ROLES];
        let mut prefix = (0, 0);
        let mut at = 0;
        while at < clause.len() {
            if let Some(role) = OPENING.iter().position(|&byte| byte == clause[at]) {
                let mut finish = at + 1;
                while finish < clause.len() && clause[finish] != CLOSING[role] {
                    finish += 1;
                }
                roles[role] = (at + 1, finish);
                at = finish + 1;
            } else if clause[at].is_ascii_lowercase() {
                let start = at;
                while at < clause.len() && clause[at].is_ascii_lowercase() {
                    at += 1;
                }
                prefix = (start, at);
            } else {
                at += 1;
            }
        }
        if prefix.0 != prefix.1 {
            emit(&clause[prefix.0..prefix.1], &mut first);
            emit(b" ", &mut first);
        }
        for (role, &(start, finish)) in roles.iter().enumerate() {
            if role != 0 {
                emit(b" ", &mut first);
            }
            emit(&clause[start..finish], &mut first);
        }
    }
    write_byte(b'\n');

    0
}
