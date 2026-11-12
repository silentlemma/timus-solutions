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
    const MAX_DIGITS: usize = 6;
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

fn text(bytes: &[u8]) {
    for &c in bytes {
        // SAFETY: putchar takes a byte promoted to int and no pointers.
        unsafe {
            putchar(i32::from(c));
        }
    }
}

const CHOSEN: u32 = 1 << 31;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (n, m) = (number() as usize, number() as usize);
    let mut head = vec![0_u32; n];
    let mut to = vec![0_u32; 2 * m];
    let mut next = vec![0_u32; 2 * m];
    let mut parent_edge = vec![0_u32; n];
    let mut order = vec![0_u32; n];
    for i in 0..m {
        let (a, b) = (number() as usize - 1, number() as usize - 1);
        to[2 * i] = b as u32;
        next[2 * i] = head[a];
        head[a] = (2 * i + 1) as u32;
        to[2 * i + 1] = a as u32;
        next[2 * i + 1] = head[b];
        head[b] = (2 * i + 2) as u32;
    }
    let mut tail = 1;
    let mut position = 0;
    while position < tail {
        let v = order[position] as usize;
        let mut link = head[v];
        while link != 0 {
            let edge = (link - 1) as usize;
            if parent_edge[v] == 0 || edge != ((parent_edge[v] - 1) ^ 1) as usize {
                let u = to[edge] as usize;
                parent_edge[u] = (edge + 1) as u32;
                order[tail] = u as u32;
                tail += 1;
            }
            link = next[edge];
        }
        position += 1;
    }
    let mut used = vec![false; n];
    let mut count = 0;
    for position in (1..n).rev() {
        let v = order[position] as usize;
        let edge = (parent_edge[v] - 1) as usize;
        let parent = to[edge ^ 1] as usize;
        if used[v] || used[parent] {
            continue;
        }
        used[v] = true;
        used[parent] = true;
        count += 1;
        // Links are dead after BFS; reuse their high bits as selected-road flags.
        next[edge & !1] |= CHOSEN;
    }
    write_number(count);
    text(b"\n");
    for i in 0..m {
        if next[2 * i] & CHOSEN != 0 {
            write_number(u64::from(to[2 * i + 1] + 1));
            text(b" ");
            write_number(u64::from(to[2 * i] + 1));
            text(b"\n");
        }
    }
    0
}
