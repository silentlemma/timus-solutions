use std::ffi::{c_char, c_int};

const MAX_STATIONS: usize = 200;
const MAX_POINTS: usize = MAX_STATIONS + 2;
const WORD_BITS: usize = u64::BITS as usize;
const WORDS: usize = (MAX_POINTS + WORD_BITS - 1) / WORD_BITS;

extern "C" {
    fn scanf(format: *const c_char, ...) -> c_int;
    fn printf(format: *const c_char, ...) -> c_int;
}

unsafe fn integer() -> usize {
    let mut value: c_int = 0;
    scanf(b"%d\0".as_ptr().cast(), &mut value);
    value as usize
}

unsafe fn solve() {
    let (mut walk, mut metro) = (0.0f64, 0.0f64);
    scanf(b"%lf %lf\0".as_ptr().cast(), &mut walk, &mut metro);
    let n = integer();
    let (total, start, goal) = (n + 2, n, n + 1);
    let mut points = [(0.0f64, 0.0f64); MAX_POINTS];
    for point in points.iter_mut().take(n) {
        scanf(b"%lf %lf\0".as_ptr().cast(), &mut point.0, &mut point.1);
    }
    let mut linked = [[0u64; WORDS]; MAX_POINTS];
    let mut active = [false; MAX_POINTS];
    let mut edges = 0;
    loop {
        let (a, b) = (integer(), integer());
        if a == 0 && b == 0 {
            break;
        }
        let (a, b) = (a - 1, b - 1);
        linked[a][b / WORD_BITS] |= 1u64 << (b % WORD_BITS);
        linked[b][a / WORD_BITS] |= 1u64 << (a % WORD_BITS);
        active[a] = true;
        active[b] = true;
        edges += 1;
    }
    for point in points.iter_mut().take(total).skip(n) {
        scanf(b"%lf %lf\0".as_ptr().cast(), &mut point.0, &mut point.1);
    }
    if edges == 0 || walk == metro || points[start] == points[goal] {
        let answer =
            (points[start].0 - points[goal].0).hypot(points[start].1 - points[goal].1) / walk;
        printf(b"%.17g\n0\n\0".as_ptr().cast(), answer);
        return;
    }
    active[start] = true;
    active[goal] = true;
    let mut vertices = [0usize; MAX_POINTS];
    let mut count = 0;
    for v in 0..total {
        if active[v] {
            vertices[count] = v;
            count += 1;
        }
    }
    let mut distance = [f64::INFINITY; MAX_POINTS];
    let mut previous = [0u16; MAX_POINTS];
    let mut done = [false; MAX_POINTS];
    distance[start] = 0.0;
    loop {
        let mut u = usize::MAX;
        for &v in &vertices[..count] {
            if !done[v] && (u == usize::MAX || distance[v] < distance[u]) {
                u = v;
            }
        }
        if u == goal {
            break;
        }
        done[u] = true;
        for &v in &vertices[..count] {
            if !done[v] {
                let train = linked[u][v / WORD_BITS] & (1u64 << (v % WORD_BITS)) != 0;
                let speed = if train { metro } else { walk };
                let candidate = distance[u]
                    + (points[v].0 - points[u].0).hypot(points[v].1 - points[u].1) / speed;
                if candidate < distance[v] {
                    distance[v] = candidate;
                    previous[v] = u as u16;
                }
            }
        }
    }
    let mut path = [0i32; MAX_POINTS];
    let mut length = 0;
    let mut v = previous[goal] as usize;
    while v != start {
        path[length] = v as i32 + 1;
        length += 1;
        v = previous[v] as usize;
    }
    printf(
        b"%.17g\n%d\0".as_ptr().cast(),
        distance[goal],
        length as c_int,
    );
    for &v in path[..length].iter().rev() {
        printf(b" %d\0".as_ptr().cast(), v);
    }
    printf(b"\n\0".as_ptr().cast());
}

fn main() {
    // All variadic arguments have exactly the types required by their formats.
    unsafe { solve() }
}
