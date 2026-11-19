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

const UNREACHED: u32 = u32::MAX;
struct Edge {
    to: u32,
    next: u32,
}
fn bfs(head: &[u32], edges: &[Edge], source: usize, order: &mut Vec<u32>) -> Vec<u32> {
    let mut distance = vec![UNREACHED; head.len()];
    distance[source] = 0;
    order.clear();
    order.push(source as u32);
    let mut at = 0;
    while at < order.len() {
        let vertex = order[at] as usize;
        let mut edge = head[vertex];
        while edge != UNREACHED {
            let branch = &edges[edge as usize];
            let next = branch.to as usize;
            if distance[next] == UNREACHED {
                distance[next] = distance[vertex] + 1;
                order.push(branch.to);
            }
            edge = branch.next;
        }
        at += 1;
    }
    distance
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (count, edge_count) = (number() as usize, number() as usize);
    let mut head = vec![UNREACHED; count];
    let mut edges = Vec::with_capacity(2 * edge_count);
    for _ in 0..edge_count {
        let (a, b) = (number() as usize - 1, number() as usize - 1);
        for (from, to) in [(a, b), (b, a)] {
            edges.push(Edge {
                to: to as u32,
                next: head[from],
            });
            head[from] = (edges.len() - 1) as u32;
        }
    }
    let (start, finish, origin) = (
        number() as usize - 1,
        number() as usize - 1,
        number() as usize - 1,
    );
    let mut order = Vec::with_capacity(count);
    let clearance = bfs(&head, &edges, origin, &mut order);
    let depth = bfs(&head, &edges, start, &mut order);
    let mut best = vec![0u32; count];
    best[start] = clearance[start];
    for &vertex in &order {
        let vertex = vertex as usize;
        let mut edge = head[vertex];
        while edge != UNREACHED {
            let branch = &edges[edge as usize];
            let next = branch.to as usize;
            if depth[next] == depth[vertex] + 1 {
                best[next] = best[next].max(best[vertex].min(clearance[next]));
            }
            edge = branch.next;
        }
    }
    write_number(i64::from(best[finish]));
    write_byte(b'\n');

    0
}
