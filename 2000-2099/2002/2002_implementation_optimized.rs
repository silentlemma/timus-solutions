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

fn write_text(text: &[u8]) {
    for &byte in text {
        write_byte(byte);
    }
}

use std::collections::{hash_map::Entry, HashMap};
struct Account {
    password: Vec<u8>,
    online: bool,
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number();
    let mut accounts: HashMap<Vec<u8>, Account> = HashMap::new();
    for _ in 0..count {
        let action = word();
        let name = word();
        let mut password = if action == b"logout" {
            None
        } else {
            Some(word())
        };
        // Keep registered accounts only, not the complete command and reply history.
        let reply: &[u8] = match accounts.entry(name) {
            Entry::Vacant(slot) => {
                if action == b"register" {
                    slot.insert(Account {
                        password: password.take().unwrap(),
                        online: false,
                    });
                    b"success: new user added"
                } else {
                    b"fail: no such user"
                }
            }
            Entry::Occupied(mut slot) => {
                let account = slot.get_mut();
                if action == b"register" {
                    b"fail: user already exists"
                } else if action == b"login" {
                    if account.password.as_slice() != password.as_deref().unwrap() {
                        b"fail: incorrect password"
                    } else if account.online {
                        b"fail: already logged in"
                    } else {
                        account.online = true;
                        b"success: user logged in"
                    }
                } else if !account.online {
                    b"fail: already logged out"
                } else {
                    account.online = false;
                    b"success: user logged out"
                }
            }
        };
        write_text(reply);
        write_byte(b'\n');
    }

    0
}
