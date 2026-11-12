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

const CYCLE_MULTIPLE: usize = 3;

fn find(parent: &mut [i32], mut v: usize) -> usize {
    let mut root = v;
    while parent[root] >= 0 {
        root = parent[root] as usize;
    }
    while v != root {
        let next = parent[v] as usize;
        parent[v] = root as i32;
        v = next;
    }
    root
}

fn connect(parent: &mut [i32], a: usize, s: usize, head: &[u32], next: &[u32]) -> bool {
    let mut b = head[s] as usize;
    while b != 0 {
        let (mut ra, mut rb) = (find(parent, a), find(parent, b));
        if ra == rb {
            return false;
        }
        if parent[ra] > parent[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        let size = parent[rb];
        parent[ra] += size;
        parent[rb] = ra as i32;
        b = next[b] as usize;
    }
    true
}

fn solve(k: usize) -> usize {
    let mut square = vec![0_u32; k];
    let mut root_head = vec![0_u32; k];
    let mut root_next = vec![0_u32; k];
    let mut written_head = vec![0_u32; k];
    let mut written_next = vec![0_u32];
    for s in 0..k {
        let remainder = (s as u64 * s as u64 % k as u64) as u32;
        if remainder != 0 {
            square[s] = k as u32 - remainder;
        }
        let target = square[s] as usize;
        root_next[s] = root_head[target];
        root_head[target] = (s + 1) as u32;
    }
    let mut parent = vec![0_i32];
    for a in 1..=CYCLE_MULTIPLE * k {
        parent.push(-1);
        let residue = a % k;
        if !connect(
            &mut parent,
            a,
            square[residue] as usize,
            &written_head,
            &written_next,
        ) {
            return a;
        }
        let mut node = root_head[residue] as usize;
        while node != 0 {
            let s = node - 1;
            if s != square[residue] as usize
                && !connect(&mut parent, a, s, &written_head, &written_next)
            {
                return a;
            }
            node = root_next[s] as usize;
        }
        written_next.push(written_head[residue]);
        written_head[residue] = a as u32;
    }
    unreachable!()
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let k = number() as usize;
    write_number(solve(k) as u64);
    // SAFETY: putchar takes a newline byte promoted to int, without pointers.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
