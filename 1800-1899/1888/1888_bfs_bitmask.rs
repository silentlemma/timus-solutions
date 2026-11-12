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

const MAX_PILOTS: usize = 50;
const MAX_YEARS: u8 = 50;

fn distances(
    source: usize,
    adj: &[u64; MAX_PILOTS],
    years: &mut [u8; MAX_PILOTS],
) -> Option<(u64, usize)> {
    let (mut frontier, mut seen, mut depth) = (1_u64 << source, 0_u64, 0);
    while frontier != 0 {
        seen |= frontier;
        let (mut next, mut vertices) = (0, frontier);
        while vertices != 0 {
            let vertex = vertices.trailing_zeros() as usize;
            if adj[vertex] & frontier != 0 {
                return None;
            }
            years[vertex] = (depth + 1) as u8;
            next |= adj[vertex];
            vertices &= vertices - 1;
        }
        frontier = next & !seen;
        if frontier != 0 {
            depth += 1;
        }
    }
    Some((seen, depth))
}

fn write_byte(c: u8) {
    // SAFETY: putchar accepts an unsigned character promoted to int, without pointers.
    unsafe {
        putchar(c as i32);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (n, p) = (number() as usize, number() as usize);
    let mut adj = [0_u64; MAX_PILOTS];
    for _ in 0..n {
        let (a, b) = (number() as usize - 1, number() as usize - 1);
        adj[a] |= 1_u64 << b;
        adj[b] |= 1_u64 << a;
    }
    let (mut unseen, mut first, mut components) = ((1_u64 << p) - 1, 0, 0);
    let mut years = [0_u8; MAX_PILOTS];
    while unseen != 0 {
        let source = unseen.trailing_zeros() as usize;
        let Some((component, _)) = distances(source, &adj, &mut years) else {
            for c in b"-1\n" {
                write_byte(*c);
            }
            return 0;
        };
        if components == 0 {
            first = component;
        }
        components += 1;
        unseen &= !component;
    }
    let mut spread = (MAX_YEARS - 1) as usize;
    if components > 1 {
        for (id, year) in years[..p].iter_mut().enumerate() {
            let parity = (*year - 1) & 1;
            *year = if first >> id & 1 != 0 {
                1 + parity
            } else {
                MAX_YEARS - parity
            };
        }
    } else {
        spread = 0;
        let mut best = years;
        let mut trial = [0_u8; MAX_PILOTS];
        for source in 0..p {
            let (_, far) = distances(source, &adj, &mut trial).unwrap();
            if far > spread {
                spread = far;
                best = trial;
            }
        }
        years = best;
    }
    write_number(spread as u64);
    write_byte(b'\n');
    for (id, &year) in years[..p].iter().enumerate() {
        if id != 0 {
            write_byte(b' ');
        }
        write_number(year as u64);
    }
    write_byte(b'\n');
    0
}
