#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(value: i32) -> i32;
}

const NAME_LIMIT: usize = 50;
// Each of at most 100 historical teams contributes at most one surname.
const CAPACITY: usize = 256;
const FULL: u8 = 1;
const PAIR: u8 = 2;

fn byte() -> i32 {
    // SAFETY: getchar reads the process's standard input stream.
    unsafe { getchar() }
}

fn non_space() -> i32 {
    let mut c = byte();
    while (0..=i32::from(b' ')).contains(&c) {
        c = byte();
    }
    c
}

fn number() -> i32 {
    const BASE: i32 = 10;
    let mut c = non_space();
    let mut value = 0;
    while (i32::from(b'0')..=i32::from(b'9')).contains(&c) {
        value = value * BASE + c - i32::from(b'0');
        c = byte();
    }
    value
}

#[derive(Clone, Copy)]
struct Name {
    bytes: [u8; NAME_LIMIT],
    len: usize,
    hash: u32,
}

impl Name {
    const EMPTY: Self = Self {
        bytes: [0; NAME_LIMIT],
        len: 0,
        hash: 0,
    };

    fn read() -> Self {
        const HASH_BASIS: u32 = 2_166_136_261;
        const HASH_PRIME: u32 = 16_777_619;
        let mut name = Self::EMPTY;
        name.hash = HASH_BASIS;
        let mut c = non_space();
        while c > i32::from(b' ') {
            name.bytes[name.len] = c as u8;
            name.len += 1;
            name.hash = (name.hash ^ c as u32).wrapping_mul(HASH_PRIME);
            c = byte();
        }
        name
    }

    fn as_bytes(&self) -> &[u8] {
        &self.bytes[..self.len]
    }
}

#[derive(Clone, Copy)]
struct Entry {
    name: Name,
    teams: u8,
}

fn find(table: &[Entry; CAPACITY], name: &Name) -> usize {
    let mask = CAPACITY - 1;
    let mut index = name.hash as usize & mask;
    while table[index].teams != 0 {
        let stored = &table[index].name;
        if stored.hash == name.hash && stored.as_bytes() == name.as_bytes() {
            break;
        }
        index = (index + 1) & mask;
    }
    index
}

fn output(bytes: &[u8]) {
    for &c in bytes {
        // SAFETY: each byte is promoted to a valid putchar argument.
        unsafe { putchar(i32::from(c)) };
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const LYOSHA: &[u8] = b"Efremov";
    const VADIK: &[u8] = b"Kantorov";
    const FULL_TEAM: i32 = 3;
    let mut table = [Entry {
        name: Name::EMPTY,
        teams: 0,
    }; CAPACITY];
    let n = number();
    for _ in 0..n {
        let size = number();
        for _ in 0..size {
            let name = Name::read();
            if name.as_bytes() == LYOSHA || name.as_bytes() == VADIK {
                continue;
            }
            let index = find(&table, &name);
            let entry = &mut table[index];
            entry.name = name;
            entry.teams |= if size == FULL_TEAM { FULL } else { PAIR };
        }
    }
    let lyosha = number();
    let vadik = number();
    let m = number();
    let mut best = -1;
    let mut chosen = Name::EMPTY;
    for _ in 0..m {
        let name = Name::read();
        let rating = number();
        let teams = table[find(&table, &name)].teams;
        let strength = if teams & FULL == 0 {
            vadik + rating + lyosha
        } else if teams & PAIR == 0 {
            vadik + rating
        } else {
            continue;
        };
        if strength > best {
            best = strength;
            chosen = name;
        }
    }
    if best < 0 {
        output(b"Fail\n");
    } else {
        output(b"Win\n");
        output(chosen.as_bytes());
        output(b"\n");
    }
    0
}
