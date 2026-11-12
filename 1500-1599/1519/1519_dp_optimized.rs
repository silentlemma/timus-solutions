#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn byte() -> i32 {
    // SAFETY: getchar reads standard input and has no pointer arguments.
    unsafe { getchar() }
}

fn number() -> u64 {
    const SPACE: i32 = b' ' as i32;
    const ZERO: i32 = b'0' as i32;
    const NINE: i32 = b'9' as i32;
    let mut c = byte();
    while c >= 0 && c <= SPACE {
        c = byte();
    }
    let mut n = 0;
    while (ZERO..=NINE).contains(&c) {
        n = n * 10 + (c - ZERO) as u64;
        c = byte();
    }
    n
}

fn write_number(mut n: u64) {
    const MAX_DIGITS: usize = 20;
    let mut digits = [0_u8; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (n % 10) as u8;
        n /= 10;
        if n == 0 {
            break;
        }
    }
    for &digit in &digits[first..] {
        // SAFETY: putchar accepts the byte promoted to int, with no pointers.
        unsafe {
            putchar(digit as i32);
        }
    }
}

const MAX_SIDE: usize = 12;
const MAX_STATES: usize = 41835;
const INITIAL_CAPACITY: usize = 16384;
const TABLE_BITS: usize = 16;
const TABLE_SIZE: usize = 1 << TABLE_BITS;
const KEY_BITS: usize = 32;
const HASH_MULTIPLIER: u32 = 2654435761;

struct Layer {
    keys: Vec<u32>,
    counts: Vec<u64>,
}

impl Layer {
    fn new() -> Self {
        Self {
            keys: Vec::with_capacity(INITIAL_CAPACITY),
            counts: Vec::with_capacity(INITIAL_CAPACITY),
        }
    }
    fn add(&mut self, state: u32, count: u64, table: &mut [u16]) {
        let mut slot = (state.wrapping_mul(HASH_MULTIPLIER) >> (KEY_BITS - TABLE_BITS)) as usize;
        while table[slot] != 0 {
            let index = table[slot] as usize - 1;
            if self.keys[index] == state {
                self.counts[index] += count;
                return;
            }
            slot = (slot + 1) & (TABLE_SIZE - 1);
        }
        assert!(self.keys.len() < MAX_STATES);
        self.keys.push(state);
        self.counts.push(count);
        table[slot] = self.keys.len() as u16;
    }
}

const OPEN: u32 = 1; // the ends of a path piece, matched like brackets
const CLOSE: u32 = 2;
const FLIP: u32 = OPEN ^ CLOSE; // turns one end into the other
const BITS: usize = 2; // bits per plug
const MASK: u32 = 3; // one plug

// the plug matching the bracket at pos, searching towards step
fn partner(state: u32, mut pos: i32, step: i32) -> i32 {
    let mut depth = 0;
    loop {
        match state >> (BITS as i32 * pos) & MASK {
            OPEN => depth += step,
            CLOSE => depth -= step,
            _ => {}
        }
        if depth == 0 {
            return pos;
        }
        pos += step;
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (mut n, mut m) = (number() as usize, number() as usize);
    let transpose = m > n;
    let mut free = [[false; MAX_SIDE + 1]; MAX_SIDE + 1];
    for i in 0..n {
        for j in 0..m {
            let mut c = byte();
            while c >= 0 && c <= b' ' as i32 {
                c = byte();
            }
            if transpose {
                free[j][i] = c == b'.' as i32;
            } else {
                free[i][j] = c == b'.' as i32;
            }
        }
    }
    if transpose {
        std::mem::swap(&mut n, &mut m);
    }
    let mut last = 0;
    for (i, row) in free[..n].iter().enumerate() {
        for (j, &cell) in row[..m].iter().enumerate() {
            if cell {
                last = i * m + j;
            }
        }
    }
    let (mut ways, mut next) = (Layer::new(), Layer::new());
    ways.keys.push(0);
    ways.counts.push(1);
    let mut table = [0_u16; TABLE_SIZE];
    let mut total = 0_u64;
    for i in 0..n {
        for j in 0..m {
            next.keys.clear();
            next.counts.clear();
            table.fill(0);
            let (sl, su) = (BITS * j, BITS * (j + 1));
            let clear = !(MASK << sl) & !(MASK << su);
            let (down, right) = (free[i + 1][j], free[i][j + 1]);
            for (index, &state) in ways.keys.iter().enumerate() {
                let count = ways.counts[index];
                let (left, up, base) = (state >> sl & MASK, state >> su & MASK, state & clear);
                let mut add = |s: u32| next.add(s, count, &mut table);
                if !free[i][j] {
                    if left == 0 && up == 0 {
                        add(state);
                    }
                } else if left == 0 && up == 0 {
                    if down && right {
                        add(base | OPEN << sl | CLOSE << su);
                    }
                } else if left == 0 || up == 0 {
                    let end = left | up;
                    if down {
                        add(base | end << sl);
                    }
                    if right {
                        add(base | end << su);
                    }
                } else if left == up {
                    // two openings or two closings: the far end of one of the
                    // joined pieces changes its kind
                    let far = if left == OPEN {
                        partner(state, j as i32 + 1, 1)
                    } else {
                        partner(state, j as i32, -1)
                    };
                    add(base ^ FLIP << (BITS as i32 * far));
                } else if left == CLOSE {
                    add(base);
                } else if i * m + j == last && base == 0 {
                    total += count; // the loop closes on the last free cell
                }
            }
            std::mem::swap(&mut ways, &mut next);
        }
        // the next row starts with an empty left plug
        for state in &mut ways.keys {
            *state <<= BITS;
        }
    }
    write_number(total);
    // SAFETY: putchar accepts an ASCII newline without pointer arguments.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
