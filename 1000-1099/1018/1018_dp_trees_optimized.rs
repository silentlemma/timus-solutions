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

struct Edge {
    to: u8,
    next: i16,
    apples: i32,
}
fn solve(head: &[i16], edges: &[Edge], vertex: usize, parent: usize, limit: usize) -> Vec<i32> {
    let mut best = vec![0];
    let mut edge = head[vertex];
    while edge >= 0 {
        let branch = &edges[edge as usize];
        let child = usize::from(branch.to);
        if child != parent {
            let sub = solve(head, edges, child, vertex, limit);
            let old_size = best.len();
            let size = (old_size + sub.len()).min(limit + 1);
            best.resize(size, -1);
            // Descending totals leave every lower source state unchanged.
            for total in (1..size).rev() {
                for taken in 1..=sub.len().min(total) {
                    let before = total - taken;
                    if before < old_size {
                        best[total] =
                            best[total].max(best[before] + branch.apples + sub[taken - 1]);
                    }
                }
            }
        }
        edge = branch.next;
    }
    best
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (count, limit) = (number() as usize, number() as usize);
    let mut head = vec![-1; count];
    let mut edges = Vec::with_capacity(2 * (count - 1));
    for _ in 1..count {
        let (a, b, apples) = (
            number() as usize - 1,
            number() as usize - 1,
            number() as i32,
        );
        for (from, to) in [(a, b), (b, a)] {
            edges.push(Edge {
                to: to as u8,
                next: head[from],
                apples,
            });
            head[from] = (edges.len() - 1) as i16;
        }
    }
    write_number(i64::from(solve(&head, &edges, 0, count, limit)[limit]));
    write_byte(b'\n');

    0
}
