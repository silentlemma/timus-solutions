use std::cmp::Ordering;
use std::io;

// x + 1 for a decimal string
fn inc(x: &[u8]) -> Vec<u8> {
    let mut b = x.to_vec();
    for k in (0..b.len()).rev() {
        if b[k] != b'9' {
            b[k] += 1;
            return b;
        }
        b[k] = b'0';
    }
    b.insert(0, b'1');
    b
}

// x - 1 for a positive decimal string
fn dec(x: &[u8]) -> Vec<u8> {
    let mut b = x.to_vec();
    let mut k = b.len() - 1;
    while b[k] == b'0' {
        b[k] = b'9';
        k -= 1;
    }
    b[k] -= 1;
    if b[0] == b'0' && b.len() > 1 {
        b.remove(0);
    }
    b
}

fn mul_small(x: &[u8], m: u32) -> Vec<u8> {
    let mut r = Vec::new();
    let mut carry = 0;
    for &c in x.iter().rev() {
        carry += (c - b'0') as u32 * m;
        r.push(b'0' + (carry % 10) as u8);
        carry /= 10;
    }
    while carry > 0 {
        r.push(b'0' + (carry % 10) as u8);
        carry /= 10;
    }
    r.reverse();
    r
}

fn add_small(x: &[u8], m: usize) -> Vec<u8> {
    let mut r = x.to_vec();
    for _ in 0..m {
        r = inc(&r);
    }
    r
}

// a - b for decimal strings with a >= b
fn sub(a: &[u8], b: &[u8]) -> Vec<u8> {
    let mut r = a.to_vec();
    let mut borrow = 0;
    for k in 0..a.len() {
        let pa = a.len() - 1 - k;
        let db = if k < b.len() {
            (b[b.len() - 1 - k] - b'0') as i32
        } else {
            0
        };
        let v = (a[pa] - b'0') as i32 - borrow - db;
        borrow = (v < 0) as i32;
        r[pa] = b'0' + ((v + 10) % 10) as u8;
    }
    match r.iter().position(|&c| c != b'0') {
        Some(lead) => r[lead..].to_vec(),
        None => vec![b'0'],
    }
}

fn compare(a: &[u8], b: &[u8]) -> Ordering {
    a.len().cmp(&b.len()).then_with(|| a.cmp(b))
}

// position in S of the digit s places before the start of x; the numbers
// below 10^(d-1) take (d-1)·10^(d-1) - R(d-1) digits, where R(t) is the
// repunit of t ones, which leaves d·x + 1 - R(d) for x itself
fn position(x: &[u8], before: usize) -> Vec<u8> {
    let d = x.len();
    sub(
        &add_small(&mul_small(x, d as u32), 2),
        &add_small(&vec![b'1'; d], before),
    )
}

// whether the number x can begin at position s of a, with its neighbours
// filling the rest of a on both sides
fn fits(a: &[u8], s: usize, x: &[u8]) -> bool {
    let n = a.len();
    let m = x.len().min(n - s);
    if a[s..s + m] != x[..m] {
        return false;
    }
    let mut pos = s + x.len();
    let mut cur = x.to_vec();
    while pos < n {
        cur = inc(&cur);
        let m = cur.len().min(n - pos);
        if a[pos..pos + m] != cur[..m] {
            return false;
        }
        pos += cur.len();
    }
    let mut pos = s;
    let mut cur = x.to_vec();
    while pos > 0 {
        cur = dec(&cur);
        if cur == b"0" {
            return false;
        }
        let m = pos.min(cur.len());
        if a[pos - m..pos] != cur[cur.len() - m..] {
            return false;
        }
        pos -= m;
    }
    true
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let a = line.trim().as_bytes();
    let n = a.len();
    // a inside one number, right after its first digit; position() takes the
    // number of digits before x plus one
    let mut one_a = vec![b'1'];
    one_a.extend_from_slice(a);
    let mut best = position(&one_a, 0);
    let mut consider = |s: usize, x: &[u8]| {
        if fits(a, s, x) {
            let k = position(x, s + 1);
            if compare(&k, &best) == Ordering::Less {
                best = k;
            }
        }
    };
    // some number lies in a completely
    for s in 0..n {
        if a[s] != b'0' {
            for e in s + 1..=n {
                consider(s, &a[s..e]);
            }
        }
    }
    // a is the end of y - 1 followed by the beginning of y; the last i digits
    // of y are those of y - 1 plus one, and they may overlap the known
    // beginning by j digits
    for i in 1..n {
        if a[i] == b'0' {
            continue;
        }
        let full = inc(&a[..i]);
        let tail = &full[full.len() - i..];
        for j in 0..=(n - i).min(i) {
            if a[n - j..] == tail[..j] {
                let mut y = a[i..].to_vec();
                y.extend_from_slice(&tail[j..]);
                consider(i, &y);
            }
        }
    }
    println!("{}", String::from_utf8(best).unwrap());
}
